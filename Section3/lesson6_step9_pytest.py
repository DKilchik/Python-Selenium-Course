"""
Задание: запуск автотестов для разных языков интерфейса
Создайте GitHub-репозиторий, в котором будут лежать файлы conftest.py и test_items.py.
Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.
Реализуйте в файле conftest.py логику запуска браузера с указанным языком пользователя. Браузер должен объявляться в
фикстуре browser и передаваться в тест как параметр.
В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в
корзину. Например, можно проверять товар,
доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
Тест должен запускаться с параметром language следующей командой:
pytest --language=es test_items.py
и проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.
Отправить ссылку на данный репозиторий в качестве ответа на данное задание.
Отправить решение на рецензирование другим учащимся. Не забудьте, что решение на рецензирование можно отправить
только один раз.
Проверьте решения минимум трех других учащихся, чтобы получить баллы за задание.
Это задание с peer-review, поэтому кроме формальных критериев другие учащиеся могут проверять корректность
написания вашего

"""

import math
from selenium import webdriver
import time


# Команда для запуска тестового примера: python test_example.py

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
