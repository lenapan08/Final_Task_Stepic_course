from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
import pytest
import time

# # # @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
# #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
# #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
# #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
# #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
# #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
# #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
# #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
# #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
# #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
#
# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                                marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # pytest -s test_product_page.py
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser)
    product_page.open()
    product_page.add_to_basket()
    # product_page.solve_quiz_and_get_code()
    # time.sleep(3)
    product_page.good_in_basket()
    product_page.price_of_good_in_basket_true()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()



@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    # product_page.solve_quiz_and_get_code()
    product_page.should_be_disappeared_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.message_basket_empty()

@pytest.mark.xfail
def test_message_basket_empty_doesnt_appeare(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_empty()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = "M9576543m"
        page.register_new_user(email, password)
        page.should_be_authorized_user()
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_basket()
        product_page.good_in_basket()
        product_page.price_of_good_in_basket_true()

