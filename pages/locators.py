from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini span.btn-group a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_EMPTY_MESSAGE = (By.XPATH, "//p[contains(text(), 'basket is empty')]")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "form#basket_formset")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    RIGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_ADDED_PRODUCT = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.product_main > h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")
