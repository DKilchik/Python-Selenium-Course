"""
Задание: переход на новую вкладку
1 Открыть страницу http://suninjuly.github.io/redirect_accept.html
2 Нажать на кнопку
3 Переключиться на новую вкладку
4 Пройти капчу для робота и получить число-ответ
"""

import math
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Жмем на кнопку
    button = browser.find_element_by_class_name('trollface')
    button.click()

    # Переходим на вторую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Ждем загрузки
    time.sleep(1)

    # Считаем значение вырожения
    x = browser.find_element_by_id('input_value')
    x = int(x.text)
    value = calc(x)

    # Вставляем значение в поле
    input1 = browser.find_element_by_id('answer')
    input1.clear()
    input1.send_keys(value)

    # Сабмитим
    button = browser.find_element_by_class_name('btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()