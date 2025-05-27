# теория
# проверка и запуск geckodriver
from selenium import webdriver

# Инициализация Firefox
driver = webdriver.Firefox()

try:
    # Открыть браузер
    driver.get("https://google.com")
    print("Открыта страница:", driver.title)

finally:
    # Закрыть браузер
    driver.quit()
    print("Браузер закрыт.")
