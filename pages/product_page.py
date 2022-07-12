from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def add_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        button_basket.click()


    def good_in_basket(self):
        good_in_basket = self.browser.find_element(*ProductPageLocators.NAME_BOOK_IN_BASKET)
        text = good_in_basket.text
        title_of_book = self.browser.find_element(*ProductPageLocators.TITTLE_OF_BOOK)
        text_2 = title_of_book.text
        assert text in text_2

    def price_of_good_in_basket_true(self):
        price_good = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK)
        price_1 = price_good.text
        price_good_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK_IN_BASKET)
        price_2 = price_good_in_basket.text
        assert price_1 in price_2

    def should_not_be_success_message(self):
        no_element = self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
        assert no_element == True, "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message doesnt is presented, " \
                                                                              "but should be"
    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message disappear, " \
                                                                   "but it should  not  appeared"
