from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
    REGISTRATION_MAIL_INPUT = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD_INPUT = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, ".register_form .btn-lg")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ADDED_PRODUCT_IN_ALERT = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) .alertinner strong")
    BASKET_TOTAL_VALUE_ALERT = (By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) ")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    OPEN_BASKET = (By.CSS_SELECTOR, ".btn-group :nth-child(1).btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketLocators():
    BASKET_ITEMS = (By.CLASS_NAME, ".basket-items")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p ")