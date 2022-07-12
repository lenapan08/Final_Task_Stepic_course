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

class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, "button.btn.btn-add-to-basket")
    GOOD_IN_BASKET = (By.XPATH, "//div[@text = ' has been added to your basket.']")
    NAME_BOOK_IN_BASKET = (By.CSS_SELECTOR, "div.alert-success:nth-child(1) strong")
    TITTLE_OF_BOOK = (By.CSS_SELECTOR, "div.product_main h1")
    PRICE_OF_BOOK = (By.CSS_SELECTOR, "div.product_main p.price_color")
    PRICE_OF_BOOK_IN_BASKET = (By.CSS_SELECTOR, "div.alert-info div p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success:nth-child(1)")
