# Developer: hợp đồng chấm điểm

Đọc ca chấm điểm trong `examples/grades.py` và `tests/test_contracts.py` trước. Chỉ sửa `examples/grades.py`; không sửa test hiện có, mã website hay khởi chạy tác nhân khác.

Hợp đồng: đúng ba môn — Ngữ văn, Lịch sử, Toán. Điểm là `int`/`float` hữu hạn; từ chối bool, chuỗi, môn thiếu/thừa và giá trị ngoài 0–100. Trung bình từ 60 là đạt. Danh sách học sinh rỗng trả danh sách rỗng. Xếp theo tổng chưa làm tròn kiểu cạnh tranh, giữ thứ tự đầu vào khi hòa và không sửa dữ liệu nguồn.

Giữ giao diện `calculate_total`, `calculate_average`, `get_grade`, `rank_students`. Kiểm tra hợp đồng và chỉ sửa khi cần. Nếu đã đúng thì giữ nguyên triển khai và báo kiểm tra thay vì viết lại để tạo diff.

Chạy `.venv/bin/python -m pytest -q tests/test_contracts.py -k 'ranking or scores'`. Ghi lệnh thực tế, mã thoát, tệp đổi và mục chưa xử lý trong `reports/grade-developer.md`. Dùng `task_id`/`completion_path` Manager thêm để viết biên nhận.
