"""
Задание: поиск элемента по XPath
1 В коде из шага 4 замените ссылку на  http://suninjuly.github.io/find_xpath_form.
2 Подберите уникальный XPath-селектор так, чтобы он находил только кнопку с текстом Submit.
XPath можете формулировать как угодно (по тексту, по структуре, по атрибутам) - главное, чтобы он работал.
3 Модифицируйте код из шага 3 таким образом, чтобы поиск кнопки происходил с помощью XPath.
4 Запустите ваш код.
"""

from selenium import webdriver
import time

link = 'http://suninjuly.github.io/find_xpath_form'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements_by_tag_name('input')
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_xpath('//button[contains(text(),"Submit")]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
