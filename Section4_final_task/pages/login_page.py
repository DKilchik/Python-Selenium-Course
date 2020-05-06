from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, "Substring 'Login' is missing in URL!"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login Form is missing on the Login Page!"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration Form is missing on " \
                                                                              "the Login Page!"

    def register_new_user(self, email=None, password=None):
        """"Эта функция регистрирует нового пользователя.Если на вход не подавать данные email и password функция
        сгенерирует их сама."""

        if email is None:
            email = str(time.time()) + "@fakemail.org"

        registration_mail_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_MAIL_INPUT)
        registration_mail_input.clear()
        registration_mail_input.send_keys(email)

        if password is None:
            password = 'somestring'

        registration_pass_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT)
        registration_pass_input.clear()
        registration_pass_input.send_keys(password)
        registration_pass_confirm = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)
        registration_pass_confirm.clear()
        registration_pass_confirm.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()