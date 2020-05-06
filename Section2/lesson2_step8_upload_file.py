"""
Задание: загрузка файла
1 Открыть страницу http://suninjuly.github.io/file_input.html
2 Заполнить текстовые поля: имя, фамилия, email
3 Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
4 Нажать кнопку "Submit"
"""
from selenium import webdriver
import time
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем поля
    input1 = browser.find_element_by_name('firstname')
    input1.clear()
    input1.send_keys('Имя')

    input2 = browser.find_element_by_name('lastname')
    input2.clear()
    input2.send_keys('Фамилия')

    input3 = browser.find_element_by_name('email')
    input3.clear()
    input3.send_keys('mail@test.ru')

    # Загружаем файл

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'new.txt')  # добавляем к этому пути имя файла

    attach = browser.find_element_by_id('file')
    attach.send_keys(file_path)

    # Сабмитим
    button = browser.find_element_by_class_name('btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
