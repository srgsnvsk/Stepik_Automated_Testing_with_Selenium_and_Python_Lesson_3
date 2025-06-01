# решение задачи

# запуск теста в консоли:
# chrome: `cd lesson3\lesson3_10 && pytest -s -v --language=es test_items.py`

from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_must_see_add_product_button(browser):
    browser.get(link)
    time.sleep(5)
    btn_add = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button")
    assert btn_add.text == "Añadir al carrito", f"Ожидался текст \"Añadir al carrito\", но получили \"{btn_add.text}\""

