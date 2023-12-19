import unittest


class TestMathOperations(unittest.TestCase):

    def test_is_square_of(self):
        test_cases = [
            (1, 1),
            (2, 4),
            (3, 9),
            (4, 16),
            (5, 25),
            (6, 36),
            (7, 49)  # Этот тест должен пройти успешно
            # Можно добавить больше случаев для проверки
        ]

        for base, square in test_cases:
            with self.subTest(base=base, square=square):
                self.assertEqual(base ** 2, square)


if __name__ == '__main__':
    unittest.main()