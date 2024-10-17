# теория

import unittest  # библиотека Python для написания и запуска тестов


# unittest.TestCase - это наследованный класс
# он предоставляет готовые методы и функциональность для написания и выполнения тестов
class TestAbs(unittest.TestCase):
    def test_abs1(self):
        # assertEqual - это метод проверки
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    # unittest.main() - это функция для автоматического запуска всех тестов и вывода результатов
    unittest.main()
