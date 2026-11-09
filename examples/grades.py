"""Hợp đồng dùng chung ở chương 2/4/5/6; xếp hạng cạnh tranh dựa trên tổng chưa làm tròn."""

from collections.abc import Mapping
from math import isfinite

SUBJECTS = frozenset({"Ngữ văn", "Lịch sử", "Toán"})


def validate_scores(scores):
    if not isinstance(scores, Mapping) or set(scores) != SUBJECTS:
        raise ValueError("scores phải có đúng các môn Ngữ văn, Lịch sử và Toán")
    for value in scores.values():
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("Điểm phải là số, không được là bool")
        if not isfinite(value) or not 0 <= value <= 100:
            raise ValueError("Điểm phải hữu hạn và nằm trong khoảng 0 đến 100")
    return scores


def calculate_total(scores):
    return sum(validate_scores(scores).values())


def calculate_average(scores):
    return calculate_total(scores) / 3


def get_grade(average):
    if isinstance(average, bool) or not isinstance(average, (int, float)):
        raise ValueError("Điểm trung bình phải là số")
    if not isfinite(average) or not 0 <= average <= 100:
        raise ValueError("Điểm trung bình phải trong khoảng 0 đến 100")
    return "Đạt" if average >= 60 else "Chưa đạt"


def rank_students(students):
    if not isinstance(students, list):
        raise ValueError("students phải là danh sách")
    rows = []
    for student in students:
        if not isinstance(student, Mapping):
            raise ValueError("Mỗi học sinh phải là đối tượng")
        name = student.get("name")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Cần có tên học sinh")
        total = calculate_total(student.get("scores"))
        average = total / 3
        rows.append({"name": name.strip(), "scores": dict(student["scores"]),
                     "total": total, "average": average, "grade": get_grade(average)})
    rows.sort(key=lambda row: row["total"], reverse=True)
    previous = None
    rank = 0
    for index, row in enumerate(rows, 1):
        if previous is None or row["total"] != previous:
            rank = index
        previous = row["total"]
        row["rank"] = rank
    return rows
