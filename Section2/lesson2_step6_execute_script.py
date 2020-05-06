"""
Задание на execute_script
1 Открыть страницу http://SunInJuly.github.io/execute_script.html.
2 Считать значение для переменной x.
3 Посчитать математическую функцию от x.
4 Проскроллить страницу вниз.
5 Ввести ответ в текстовое поле.
6 Выбрать checkbox "I'm the robot".
7 Переключить radiobutton "Robots rule!".
8 Нажать на кнопку "Submit".
"""

from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим x и просчитываем значение вырожения
    input_value = browser.find_element_by_id('input_value')
    x = input_value.text
    y = calc(int(x))

    # Прокручиваем страницу вниз
    browser.execute_script("window.scrollBy(0, 100);")

    # Вводим ответ в поле
    ans = browser.find_element_by_id('answer')
    ans.clear()
    ans.send_keys(y)

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
