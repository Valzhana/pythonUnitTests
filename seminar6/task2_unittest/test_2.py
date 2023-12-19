import unittest
from ddt import ddt, data, unpack
from task1 import add


@ddt
class TestAdd(unittest.TestCase):

    @data((2, 3, 5), (4, 5, 9), (-1, 1, 0))
    @unpack
    def test_add(self, a, b, expected):

        result = add(a, b)
        self.assertEqual(result, expected, f"Сложение {a} и {b} должно давать {expected}")


if __name__ == '__main__':
    unittest.main()