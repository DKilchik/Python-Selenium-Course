from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_correct_product_name_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_in_message = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_IN_ALERT).text
        assert product_in_message == product_name, "The message contains incorrect product name!"

    def basket_value_should_be_equal_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_value = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_VALUE_ALERT).text
        assert product_price == basket_value, "Wrong basket value in message!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message hasn't disappeared yet!"