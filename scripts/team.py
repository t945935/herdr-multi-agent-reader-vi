#!/usr/bin/env python3
"""Dispatch to an already-started idle agent; verify a task-specific receipt."""
import argparse
import json
import os
import subprocess
import uuid
from pathlib import Path


def call(*args, timeout=310):
    done = subprocess.run(["herdr", *args], text=True, capture_output=True, timeout=timeout)
    if done.returncode:
        raise RuntimeError(done.stderr or done.stdout)
    return json.loads(done.stdout)["result"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("target")
    parser.add_argument("prompt", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if os.environ.get("HERDR_ENV") != "1":
        raise SystemExit("Hãy chạy bên trong Herdr")
    agent = call("agent", "get", args.target)["agent"]
    if agent["agent_status"] not in {"idle", "done"}:
        raise SystemExit("Tác nhân phải ở trạng thái idle/done trước khi bắt đầu tác vụ")
    path = args.output.resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise SystemExit("Chọn đường dẫn biên nhận mới, không dùng lại đường dẫn của tác vụ cũ")
    task_id = uuid.uuid4().hex
    prompt = args.prompt.read_text() + (
        f"\n\ntask_id của tác vụ này là {task_id}\ncompletion_path={path}\n"
        'Hãy thực hiện tác vụ thật rồi ghi JSON: {"task_id":"mã định danh ở trên","status":"completed",'
        '"summary":"sản phẩm bàn giao cụ thể và cách xác minh","artifacts":["đường dẫn hiện vật thực tế"]}。'
        "Nếu không thể hoàn thành tác vụ, dùng status=blocked và giải thích trong summary. Không khởi chạy tác nhân khác."
    )
    settled = call("agent", "prompt", args.target, prompt, "--wait", "--timeout", "300000")
    state = settled["agent"]["agent_status"]
    if state not in {"idle", "done"} or not path.is_file():
        raise SystemExit("Tác nhân đã ổn định nhưng chưa có biên nhận được chấp nhận; hãy kiểm tra agent get/read")
    receipt = json.loads(path.read_text())
    if receipt.get("task_id") != task_id or receipt.get("status") != "completed" or not receipt.get("summary"):
        raise SystemExit("Biên nhận không nghiệm thu tác vụ này")
    for artifact in receipt.get("artifacts", []):
        candidate = Path(artifact)
        if not candidate.is_absolute():
            candidate = Path.cwd() / candidate
        if not candidate.is_file():
            raise SystemExit(f"Thiếu hiện vật: {artifact}")
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
