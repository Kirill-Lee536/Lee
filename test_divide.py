import pytest
from app import divide

def test_divide_by_non_zero():
    """Проверяем деление на ненулевое число"""
    assert divide(10, 2) == 5
    assert divide(10, 1) == 10

def test_divide_by_zero():
    """Проверяем деление на ноль — должно вызывать исключение"""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0) 
