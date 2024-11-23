# решение задачи

import pytest
import json
import os
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\n\033[34mStart browser for test..\033[0m")
    browser = webdriver.Chrome()
    yield browser
    print("\n\033[34mQuit browser..\033[0m")
    browser.quit()


@pytest.fixture(scope="session")
def load_config():
    current_dir = os.path.dirname(__file__)
    config_path = os.path.join(current_dir, "config.json")
    with open(config_path, "r") as config_file:
        config = json.load(config_file)
    return config

