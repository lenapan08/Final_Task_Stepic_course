from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        login_url = self.browser.current_url
        assert ("login" in login_url) == True, "'Login' doesnt in URL"


    def should_be_login_form(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # field_email = self.browser.find_elements(*LoginPageLocators.LOG_IN_EMAIL_ADDRESS)
        # assert (len(field_email) > 0) == True, "Field email  of form 'Log IN' doesnt present"
        field_pass = self.browser.find_elements(*LoginPageLocators.LOG_IN_PASSWORD)
        assert (len(field_pass) > 0) == True, "Field password  of form 'Log IN' doesnt present"


    def should_be_register_form(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        element = self.browser.find_element(*LoginPageLocators.FORM_REGISTER)
        assert (element > 0) == True, "Title of form 'Log IN' is present"