# теория
# проверка и запуск geckodriver
import pytest
from selenium import webdriver
import time

@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_stepik_page(browser): 
    browser.get("https://stepik.org/lesson/25969/step/8")
    print("Открыта страница:", browser.title)
    time.sleep(2)

# без фикстуры при открытии вкладки Testing в VS Code будет выполняться код