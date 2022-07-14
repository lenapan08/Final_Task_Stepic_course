from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.TITTLE_ITERMS_IN_BASKET), "Items in basket, but shouldnt"

    def message_basket_empty(self):
        text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text
        assert "empty" in text, "Basket doesnt empty"

    def should_not_be_basket_empty(self):
        text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text
        assert "empty" not in text, "Basket empty"