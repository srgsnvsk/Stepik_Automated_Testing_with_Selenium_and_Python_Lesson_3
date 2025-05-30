# теория
# проверка и запуск geckodriver

from selenium import webdriver
import time

# инициализируем драйвера браузера. 
# после этой команды откроется новое окно браузера
if __name__ == "__main__":  # Запуск только при прямом вызове файла
    driver = webdriver.Firefox()
    driver.get("https://stepik.org/lesson/25969/step/8")
    time.sleep(5)
    driver.quit()

# без констуркции `if __name__` при открытии вкладки Testing в VS Code будет выполняться код