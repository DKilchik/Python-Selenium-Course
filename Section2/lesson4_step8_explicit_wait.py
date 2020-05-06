"""
Задание: ждем нужный текст на странице
1 Открыть страницу http://suninjuly.github.io/explicit_wait2.html
2 Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
3 Нажать на кнопку "Book"
4 Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
"""

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    text = '$100'

    # Дожидаемся нужной цены и кликаем на кнопку
    price = WebDriverWait(browser, 15).until(
        expected_conditions.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    button = browser.find_element_by_class_name('btn')
    button.click()

    # Вычисляем вырожение, вводим ответ в поле и жмем на кнопку
    x = browser.find_element_by_id('input_value')
    x = int(x.text)
    ans = calc(x)

    input_ans = browser.find_element_by_id('answer')
    input_ans.clear()
    input_ans.send_keys(ans)

    button_submit = browser.find_element_by_id('solve')
    button_submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
