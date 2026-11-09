"""Chương 6: xác thực biên nhận bàn giao rõ ràng, không dựa vào lời khẳng định của tác nhân."""

import argparse
import hashlib
import json
from pathlib import Path


def validate(record, root):
    required = {"task_id", "from", "to", "completed", "next", "artifacts"}
    if not isinstance(record, dict) or not required <= record.keys():
        raise ValueError("Thiếu trường bàn giao bắt buộc")
    if any(not isinstance(record[key], str) or not record[key].strip()
           for key in ["task_id", "from", "to", "completed", "next"]):
        raise ValueError("Các trường văn bản bàn giao không được để trống")
    if not isinstance(record["artifacts"], list) or not record["artifacts"]:
        raise ValueError("Bàn giao phải có hiện vật")
    root = Path(root).resolve()
    for artifact in record["artifacts"]:
        if not isinstance(artifact, dict) or set(artifact) != {"path", "sha256"}:
            raise ValueError("Mỗi hiện vật cần đường dẫn và SHA-256")
        path = (root / artifact["path"]).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            raise ValueError("Đường dẫn hiện vật phải trỏ đến tệp bên trong dự án")
        if hashlib.sha256(path.read_bytes()).hexdigest() != artifact["sha256"]:
            raise ValueError("Hash hiện vật không khớp")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    validate(json.loads(args.record.read_text()), args.root)
    print("Đã chấp nhận bàn giao")
