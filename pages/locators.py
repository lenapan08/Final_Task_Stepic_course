from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOG_IN_EMAIL_ADDRESS = (By.ID, "#id_login-username")
    LOG_IN_PASSWORD = (By.ID, "#id_login-password")
    REG_EMAIL_ADDRESS = (By.ID, "#id_registration-email")
    REG_PASSWORD = (By.ID, "#id_registration-password1")
    REG_CONFIRM_PASSWORD = (By.ID, "#id_registration-password2")
    FORM_LOG_IN = (By.ID, "#login_form")
    FORM_REGISTER = (By.ID, "#register_form")
