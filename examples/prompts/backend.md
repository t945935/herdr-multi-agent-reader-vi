# Backend

Chỉ sửa `examples/task_manager/main.py`. Khởi tạo bảng trong lifespan FastAPI; từ chối trường không biết và ép kiểu âm thầm. POST thành công 201, PATCH 200, DELETE 204, thiếu bản ghi 404, đầu vào không hợp lệ 422. Trường PATCH bị bỏ qua giữ giá trị cũ; null tường minh bị từ chối; description có thể xóa. Không sửa tệp thuộc Database.
