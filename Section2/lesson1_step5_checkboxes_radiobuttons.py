"""
Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
1 Открыть страницу http://suninjuly.github.io/math.html.
2 Считать значение для переменной x.
3 Посчитать математическую функцию от x (код для этого приведён ниже).
4 Ввести ответ в текстовое поле.
5 Отметить checkbox "I'm the robot".
6 Выбрать radiobutton "Robots rule!".
7 Нажать на кнопку Submit.
"""

import math
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значение x и вычисляем значение вырожения
    x_element = browser.find_element_by_css_selector('.form-group :nth-child(2)')
    x = x_element.text
    y = calc(x)

    # Вставляем значение вырожения в поле ввода
    input = browser.find_element_by_id('answer')
    input.clear()
    input.send_keys(y)

    # Проставляем галку в чекбоксе
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    # Выбираем радиобатон
    radio = browser.find_element_by_id('robotsRule')
    radio.click()

    # Сабмитим
    button = browser.find_element_by_class_name('btn')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
