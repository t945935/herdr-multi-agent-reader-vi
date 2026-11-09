# QA: hệ thống chấm điểm

Đọc giao diện `examples/grades.py` và các ca hiện có trong `tests/test_contracts.py`. Tự kiểm tra hợp đồng. Không sửa mã, không xóa test hiện có, không đọc tự đánh giá Developer, không khởi chạy tác nhân khác.

Chỉ thêm/sửa `tests/test_grades_review.py`; ghi báo cáo `reports/grade-qa.md`. Kiểm tra đúng ba môn, biên 0/100/60, bool/NaN/chuỗi, dữ liệu rỗng, tên, hạng hòa 1/1/3, độ chính xác chưa làm tròn và tính bất biến của đầu vào.

Dùng pytest. Nếu test hiện có đã bao phủ đủ, nêu tiêu chí và chỉ thêm phần còn thiếu có giá trị; không lặp test y hệt. Không kiểm tra FastAPI, SQLite hoặc CRUD website: đây là tác vụ chấm điểm.

Chạy test, lưu đúng lệnh, mã thoát, phát hiện và mục chưa chạy. Dùng `task_id`/`completion_path` Manager thêm trong biên nhận, liệt kê báo cáo và tệp test trong `artifacts`.
