from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "Not message about empty basket"

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "There are products in basket"
