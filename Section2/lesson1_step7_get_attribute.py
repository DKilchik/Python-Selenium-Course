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
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим значение атрибута valuex и вычисляем выражение
    value = browser.find_element_by_id('treasure')
    x = value.get_attribute('valuex')
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
