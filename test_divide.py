import pytest
from app import divide


def test_divide_positive_numbers():
    assert divide(10, 2) == 5.0


def test_divide_negative_numerator():
    assert divide(-6, 3) == -2.0


def test_divide_zero_numerator():
    assert divide(0, 5) == 0.0


def test_divide_non_integer_result():
    assert divide(7, 2) == 3.5


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
