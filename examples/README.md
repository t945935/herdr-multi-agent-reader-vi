# Chạy các ví dụ

Chạy mọi lệnh từ thư mục gốc đã giải nén bằng Python 3.12; cài dependency qua `pip install -r requirements.txt`.

| Chương | Điểm vào | Trọng tâm nghiệm thu |
| --- | --- | --- |
| 1 | `calculator.py` | Phép tính, chia cho không, kiểu dữ liệu |
| 2 | `grades.py` | Biên điểm, môn thiếu, đồng hạng |
| 3 | `../scripts/probe_herdr.py --live` | Tạo, đọc, chờ và dọn pane |
| 4 | `../scripts/team.py` | Giao việc, task_id, chấp nhận hiện vật |
| 5 | `prompts/reviewer-a.md`, `reviewer-b.md` | Đánh giá độc lập, quyết định Manager |
| 6 | `handoff.py` | Tệp, phạm vi dự án và SHA-256 |
| 7 | `task_manager/` | CRUD, xác thực, giao diện, lưu bền |
| 8 | `research.py` | Luận điểm, nguồn, trích dẫn, độ bất định |
| 9 | `pipeline.py` | Mã thoát, timeout, dừng khi lỗi |
| 10 | `queue.py` | Khử trùng lặp, lease, phục hồi, đồng thời |

Khởi chạy website bằng `.venv/bin/python -m uvicorn examples.task_manager.main:app --host 0.0.0.0 --port 8000`. Test ngoại tuyến không cần tài khoản mô hình; giao tác nhân thật cần Herdr và CLI đã đăng nhập.
