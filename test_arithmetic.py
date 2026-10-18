import pytest
from app import arithmetic


class TestArithmeticAddition:
    def test_positive_numbers(self):
        assert arithmetic(2, '+', 3) == 5

    def test_negative_numbers(self):
        assert arithmetic(-1, '+', -2) == -3

    def test_floats(self):
        assert arithmetic(1.5, '+', 2.5) == 4.0

    def test_zero(self):
        assert arithmetic(0, '+', 0) == 0


class TestArithmeticSubtraction:
    def test_positive_numbers(self):
        assert arithmetic(10, '-', 3) == 7

    def test_negative_result(self):
        assert arithmetic(3, '-', 10) == -7

    def test_floats(self):
        assert arithmetic(5.5, '-', 2.5) == 3.0


class TestArithmeticMultiplication:
    def test_positive_numbers(self):
        assert arithmetic(4, '*', 5) == 20

    def test_by_zero(self):
        assert arithmetic(100, '*', 0) == 0

    def test_negative(self):
        assert arithmetic(-3, '*', 7) == -21

    def test_floats(self):
        assert arithmetic(2.5, '*', 4) == 10.0


class TestArithmeticDivision:
    def test_even_division(self):
        assert arithmetic(10, '/', 2) == 5.0

    def test_float_result(self):
        assert arithmetic(7, '/', 2) == 3.5

    def test_negative(self):
        assert arithmetic(-9, '/', 3) == -3.0

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            arithmetic(1, '/', 0)


class TestArithmeticUnsupported:
    def test_unsupported_operator(self):
        with pytest.raises(ValueError):
            arithmetic(1, '^', 2)

    def test_empty_string_operator(self):
        with pytest.raises(ValueError):
            arithmetic(1, '', 2)

    def test_word_operator(self):
        with pytest.raises(ValueError):
            arithmetic(1, 'add', 2)
