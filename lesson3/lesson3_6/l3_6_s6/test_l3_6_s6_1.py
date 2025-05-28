# теория
# проверка и запуск geckodriver

from selenium import webdriver
import time

# инициализируем драйвера браузера. 
# после этой команды откроется новое окно браузера
driver = webdriver.Firefox()
driver.get("https://stepik.org/lesson/25969/step/8")
time.sleep(5)
driver.quit()