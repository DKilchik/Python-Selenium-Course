from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    # Получаем опцию языка и открываем браузер
    options = webdriver.ChromeOptions()
    language = request.config.getoption('language')
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)

    # Закрытие браузера
    yield browser
    browser.quit()