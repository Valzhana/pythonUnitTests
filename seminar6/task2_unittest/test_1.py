import unittest
from task1 import add, is_prime


class TestMyModule(unittest.TestCase):

    def test_add(self):
        """Тестирование функции сложения с положительными числами."""
        self.assertEqual(add(2, 3), 5, "Сложение 2 и 3 должно давать 5")

    def test_is_prime_true(self):
        self.assertTrue(is_prime(5), "5 должно быть простым числом")

    def test_is_prime_false(self):
        self.assertFalse(is_prime(4), "4 не должно быть простым числом")


if __name__ == '__main__':
    unittest.main(verbosity=2)