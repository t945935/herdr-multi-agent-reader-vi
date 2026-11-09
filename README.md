# Gói tài nguyên — Điều phối nhóm tác nhân AI với Herdr

Phiên bản: 1.0.0

Gói công khai này cung cấp ví dụ chạy được, test, prompt và hướng dẫn bằng tiếng Việt để đi kèm sách; không chứa nội dung trả phí.

## Cài đặt và kiểm thử

Cần Python 3.12; chạy từ thư mục gốc đã giải nén:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest -q tests
```

Kết quả tham chiếu: 42 test đạt; có thể xuất hiện cảnh báo deprecated Starlette/httpx. Xem `examples/README.md` để biết ví dụ theo chương, chạy website và bài tập.

Happy eBook cung cấp gói này kèm sách; không cấp giấy phép open-source chung. Xem `RIGHTS.md`.
