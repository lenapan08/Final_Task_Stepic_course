from .pages.product_page import ProductPage
import pytest
import time


def test_guest_can_add_product_to_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # pytest -s test_product_page.py
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    # product_page.solve_quiz_and_get_code()
    # time.sleep(10)
    product_page.good_in_basket()
    product_page.price_of_good_in_basket_true()