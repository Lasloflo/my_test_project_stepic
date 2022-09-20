from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    def add_product_in_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()


    def shuold_be_messege_product_has_been_added(self):
        product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        product_added_name = self.browser.find_element(*ProductPageLocators.NAME_ADDED_PRODUCT).text
        assert product_name == product_added_name, f"Product {product_name} maybe is not added in basket"

    def is_basket_total(self):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert basket_total == price_product, "Basket total is not price product"

    # упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "element message is appeared"

    # будет ждать до тех пор, пока элемент не исчезнет
    def should_be_disappear_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "element message is not disappeared"
