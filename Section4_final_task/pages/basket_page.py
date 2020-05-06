from .base_page import BasePage
from .locators import BasketLocators


class BasketPage(BasePage):

    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        current_url = self.browser.current_url
        assert 'basket' in current_url, "Substring 'basket' in missing in current URL!"

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketLocators.BASKET_ITEMS), "Basket should be empty,but it wasn't!"

    def should_be_empty_basket_correct_message(self):

        language = self.ask_current_localisation()
        if language == 'en':
            assert self.has_element_appeared(*BasketLocators.EMPTY_BASKET), \
                "Message about empty basket hasn't appeared! "
            message_text = self.browser.find_element(*BasketLocators.EMPTY_BASKET).text
            assert "Your basket is empty" in message_text, "Wrong message text about empty basket!"
        else:
            pass