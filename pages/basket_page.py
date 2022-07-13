from .base_page import BasePage
from .locators import MainPageLocators
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def no_items_in_basket(self):
        basket = self.browser.find_element(*MainPageLocators.BASKET)
        basket.click()
        assert self.is_not_element_present(*BasketPageLocators.TITTLE_ITERMS_IN_BASKET), "Items in basket, but shouldnt"
