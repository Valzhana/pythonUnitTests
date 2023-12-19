import pytest


# Фикстура для предоставления данных для тестов
@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]


# Параметризованный тест, который будет запущен несколько раз с разными данными
@pytest.mark.parametrize("x, y, expected", [(1, 1, 2), (2, 2, 4), (3, 3, 6)])
def test_add(x, y, expected):
    assert x + y == expected


# Тест, использующий фикстуру
def test_sum(sample_data):
    assert sum(sample_data) == 15


# Пример маркера, который позволяет категоризировать тесты
@pytest.mark.slow
def test_slow_function():
    pass  # Предполагаем, что это медленный тест