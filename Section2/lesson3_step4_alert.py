"""
Задание: принимаем alert
1 Открыть страницу http://suninjuly.github.io/alert_accept.html
2 Нажать на кнопку
3 Принять confirm
4 На новой странице решить капчу для роботов, чтобы получить число с ответом
"""
import math
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем на кнопку
    button = browser.find_element_by_class_name('btn-primary')
    button.click()

    # Конфирмим
    confirm = browser.switch_to.alert
    confirm.accept()

    # Считаем значение вырожения
    x = browser.find_element_by_id('input_value')
    input_val = x.text
    value = calc(int(input_val))

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
