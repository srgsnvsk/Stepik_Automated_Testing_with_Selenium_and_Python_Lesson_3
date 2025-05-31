# теория
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption('--browser_name_lesson3_9', action='store', default='chrome',
                     help="Choose browser: '--browser_name=chrome' or '--browser_name=firefox'")
    
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: '--language=en' or '--language=ru'")
    
@pytest.fixture(scope="function")
def browser(request):
    browser_name_lesson3_9 = request.config.getoption("browser_name_lesson3_9")
    user_language = request.config.getoption("language")
    
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    
    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", user_language)

    browser = None
    if browser_name_lesson3_9 == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name_lesson3_9 == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name_lesson3_9 should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
