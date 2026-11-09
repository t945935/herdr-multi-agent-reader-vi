"""Chương 1: hợp đồng nhỏ gọn cho bài tập phát triển/đánh giá."""

from math import isfinite


def _number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Cần giá trị số; không chấp nhận bool")
    if not isfinite(value):
        raise ValueError("Cần giá trị hữu hạn")
    return value


def add(a, b):
    return _number(a) + _number(b)


def subtract(a, b):
    return _number(a) - _number(b)


def multiply(a, b):
    return _number(a) * _number(b)


def divide(a, b):
    a, b = _number(a), _number(b)
    if b == 0:
        raise ZeroDivisionError("Không thể chia cho không")
    return a / b
