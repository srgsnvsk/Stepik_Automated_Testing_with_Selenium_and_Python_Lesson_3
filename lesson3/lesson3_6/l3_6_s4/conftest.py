# решение задачи

import pytest
import json
import os
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


# Конструкция с указанием пути к текущему файлу (conftest.py) нужна для Testing средства тестирования VS Code
# Иначе будет ошибка FileNotFoundError: [Errno 2] No such file or directory: 'config.json'
# scope="session" будет запущен один раз за всю сессию тестирования
# Результат скопа session будет доступен для всех тестов, которые используют load_config
@pytest.fixture(scope="session")
def load_config():
    # Получаем путь к директории, где лежит conftest.py
    current_dir = os.path.dirname(__file__)
    # Строим путь к файлу config.json в этой же директории
    config_path = os.path.join(current_dir, "config.json")
    # Открываем файл по пути где находится config.json в режиме чтения
    with open(config_path, "r") as config_file:
        # Считываем содержимое файла и сохраняем в переменной
        config = json.load(config_file)
    # Возвращаем загруженные файлы из конфигурации
    return config


# Конструкция без указания пути к текущему файлу, если не нужен запуск по кнопочке в VS Code и достаточно запуска тестов через консоль
# @pytest.fixture(scope="session")
# def load_config():
#     with open("config.json", "r") as config_file:
#         config = json.load(config_file)
#     return config
