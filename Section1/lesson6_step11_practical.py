from selenium import webdriver
import time

# Команда для запуска: python lesson6_step11.py


try:
    link = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнение обязательных полей
    input1 = browser.find_element_by_css_selector('.first_block :nth-child(1) input')
    input1.clear()  # Чистим поле перед вводом
    input1.send_keys("Ivan")

    input3 = browser.find_element_by_css_selector('.first_block :nth-child(2) input')
    input3.clear()
    input3.send_keys("test@gmail.com")

    input4 = browser.find_element_by_css_selector('.second_block :nth-child(1) input')
    input4.clear()
    input4.send_keys('1' * 7)

    input5 = browser.find_element_by_css_selector('.second_block :nth-child(2) input')
    input5.clear()
    input5.send_keys("Russia")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text



finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
