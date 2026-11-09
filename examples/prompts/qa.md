# QA website

Chỉ sửa `tests/`. Test phải theo yêu cầu, không hạ đặc tả để làm test đạt. Cô lập SQLite bằng `tmp_path` và khởi chạy `TestClient` trong lifespan ứng dụng. Bao phủ CRUD, kiểu dữ liệu, null, trường lạ, mục không tồn tại và dữ liệu còn sau khởi động lại. Chạy test và ghi lệnh, phiên bản, mã thoát cùng tóm tắt lỗi thực tế.
