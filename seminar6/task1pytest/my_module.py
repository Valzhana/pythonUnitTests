# def add(a, b):
#     return a + b


def multiply(a, b):
    return a * b


def is_even(number):
    return number % 2 == 0


def get_username(user_id):
    if user_id < 0:
        raise ValueError("User ID must be positive")
    return f"user_{user_id}"


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def is_palindrome(string):
    return string == string[::-1]