"""
Задание: работа с выпадающим списком
1 Открыть страницу http://suninjuly.github.io/selects1.html
2 Посчитать сумму заданных чисел
3 Выбрать в выпадающем списке значение равное расчитанной сумме
4 Нажать кнопку "Submit"
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Прочитаем числа и определим их сумму
    first_num = browser.find_element_by_id('num1')
    el1 = first_num.text
    second_num = browser.find_element_by_id('num2')
    el2 = second_num.text
    ans = int(el1) + int(el2)

    # Находим правильный ответ в выпадающем списке
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(ans))

    # Сабмитим
    button = browser.find_element_by_class_name('btn')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
