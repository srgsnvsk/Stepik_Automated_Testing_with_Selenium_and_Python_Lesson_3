# теория
# для запуска тестов выполнить команду pytest test_abs_project.py


def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"


def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"
