"""
Задание: оформляем тесты в стиле unittest
Возьмите тесты из шага - https://stepik.org/lesson/138920/step/11?unit=196194
Создайте новый файл
Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
Запустите получившиеся тесты из файла
Просмотрите отчёт о запуске и найдите последнюю строчку
Отправьте эту строчку в качестве ответа на это задание
"""

import unittest
from selenium import webdriver


class TestPage(unittest.TestCase):

    def test_first_page(self):
        link1 = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link1)

        input1 = browser.find_element_by_css_selector(".first_block > .first_class > .form-control")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block > .second_class > .form-control")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('.third')
        input3.send_keys("Petrov@test.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_second_page(self):
        link2 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link2)

        input1 = browser.find_element_by_css_selector(".first_block > .first_class > .form-control")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block > .second_class > .form-control")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('.third')
        input3.send_keys("Petrov@test.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()
