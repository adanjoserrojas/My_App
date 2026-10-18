from app import sum_two_numbers


def test_sum_positive_numbers():
    assert sum_two_numbers(2, 3) == 5


def test_sum_negative_and_positive():
    assert sum_two_numbers(-1, 1) == 0


def test_sum_zeros():
    assert sum_two_numbers(0, 0) == 0


def test_sum_floats():
    assert sum_two_numbers(1.5, 2.5) == 4.0


def test_sum_negative_numbers():
    assert sum_two_numbers(-3, -7) == -10
