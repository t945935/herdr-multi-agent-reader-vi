from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, ConfigDict, field_validator

from . import db


@asynccontextmanager
async def lifespan(app):
    db.init_db()
    yield


app = FastAPI(title="Trình quản lý tác vụ Herdr", lifespan=lifespan)
STATIC = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=STATIC), name="static")


class CreateTask(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    title: str
    description: str = ""

    @field_validator("title")
    @classmethod
    def title_valid(cls, value):
        if not value.strip():
            raise ValueError("Tiêu đề tác vụ không được để trống")
        return value.strip()


class PatchTask(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    title: str | None = None
    description: str | None = None
    completed: bool | None = None

    @field_validator("title", "description", "completed")
    @classmethod
    def explicit_null_invalid(cls, value):
        if value is None:
            raise ValueError("Không hỗ trợ giá trị null được chỉ định rõ")
        return value

    @field_validator("title")
    @classmethod
    def title_valid(cls, value):
        return CreateTask.title_valid(value)


@app.get("/")
def index():
    return FileResponse(STATIC / "index.html")


@app.get("/api/tasks")
def list_tasks():
    return db.get_tasks()


@app.get("/api/tasks/{task_id}")
def get_task(task_id: int):
    task = db.get_task(task_id)
    if task is None:
        raise HTTPException(404, "Không tìm thấy tác vụ")
    return task


@app.post("/api/tasks", status_code=201)
def create_task(body: CreateTask):
    return db.create_task(**body.model_dump())


@app.patch("/api/tasks/{task_id}")
def update_task(task_id: int, body: PatchTask):
    task = db.update_task(task_id, **body.model_dump(exclude_unset=True))
    if task is None:
        raise HTTPException(404, "Không tìm thấy tác vụ")
    return task


@app.delete("/api/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    if not db.delete_task(task_id):
        raise HTTPException(404, "Không tìm thấy tác vụ")
    return Response(status_code=204)
