"""
Задание: параметризация тестов
открыть страницу
ввести правильный ответ
нажать кнопку "Отправить"
дождаться фидбека о том, что ответ правильный
проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
"""
import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


# Функция определяющая ответ
def foo():
    answer = math.log(int(time.time()))
    return float(answer)


# Фикстура для инициации браузера и закрытия окна после теста
@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
@pytest.mark.smoke
def test_optional_message(lesson, browser):
    link = 'https://stepik.org/lesson/' + lesson + '/step/1'
    browser.get(link)

    # Вызываем функцию расчета, передаем переменной ответ
    ans = foo()

    # Вводим в поле ответ и отправляем его
    input1 = WebDriverWait(browser, 10).until \
        (expected_conditions.presence_of_element_located((By.CLASS_NAME, 'textarea')))

    input1.clear()
    input1.send_keys(str(ans))

    send = browser.find_element_by_class_name('submit-submission')
    send.click()
    time.sleep(1)

    # Считываем текст сообщения
    optional_message = WebDriverWait(browser, 10).until \
        (expected_conditions.presence_of_element_located((By.CLASS_NAME, 'smart-hints__hint')))

    message = optional_message.text

    # Проверяем текст
    assert message == 'Correct!'
