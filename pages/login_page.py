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
        field_email = self.browser.find_elements(*LoginPageLocators.LOG_IN_EMAIL_ADDRESS)
        assert (field_email is not None) == True, "Field email of form 'Log IN' doesnt present"
        field_pass = self.browser.find_elements(*LoginPageLocators.LOG_IN_PASSWORD)
        assert (field_pass is not None) == True, "Field password  of form 'Log IN' doesnt present"


    def should_be_register_form(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        field_email = self.browser.find_elements(*LoginPageLocators.REG_EMAIL_ADDRESS)
        assert (field_email is not None) == True, "Field email of form 'Register' doesnt present"
        field_pass = self.browser.find_elements(*LoginPageLocators.REG_PASSWORD)
        assert (field_pass is not None) == True, "Field password  of form 'Register' doesnt present"