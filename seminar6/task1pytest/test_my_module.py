# import pytest
# from my_module import add
#
#
# def test_add():
#     assert add(2, 3) == 5, "Должно быть 5"
#
#
# def test_add_negative_numbers():
#     assert add(-1, -1) == -2, "Должно быть -2"
#
#
# def test_add_floats():
#     assert add(1.2, 2.3) == 3.5, "Должно быть 3.5"
#
#
# def test_add_strings_raises_typeerror():
#     with pytest.raises(TypeError):
#         add("hello", "world")

import pytest
from my_module import multiply, is_even, get_username, divide, is_palindrome


def test_multiply():
    assert multiply(3, 4) == 12, "3 умноженное на 4 должно быть 12"


def test_multiply_negative():
    assert multiply(-2, 3) == -6, "Умножение на отрицательное число"


def test_is_even():
    assert is_even(4), "4 должно быть четным"


def test_is_even_false():
    assert not is_even(5), "5 не должно быть четным"


def test_get_username():
    assert get_username(10) == "user_10", "Имя пользователя для ID 10 должно быть user_10"


def test_get_username_with_negative_raises_error():
    with pytest.raises(ValueError):
        get_username(-1)


def test_divide():
    assert divide(8, 2) == 4, "8 разделенное на 2 должно быть 4"


def test_divide_zero_raises_error():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)


def test_is_palindrome():
    assert is_palindrome("radar"), "'radar' должно быть палиндромом"


def test_is_palindrome_false():
    assert not is_palindrome("python"), "'python' не должно быть палиндромом"