# Database

Chỉ sửa `examples/task_manager/db.py`. Cung cấp `init_db`, `get_tasks`, `get_task`, `create_task`, `update_task`, `delete_task`. Test có thể thay `DB_PATH`; luôn đóng kết nối, dùng transaction khi ghi và truyền SQL dạng tham số. Tên cột động chỉ lấy từ danh sách cho phép cố định. Trả `None`/`False` khi thiếu bản ghi; không che lỗi database bằng danh sách rỗng.
