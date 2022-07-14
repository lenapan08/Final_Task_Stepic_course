from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET = (By.LINK_TEXT, "View basket")

class BasketPageLocators():
    TITTLE_ITERMS_IN_BASKET = (By.CSS_SELECTOR, "h2.col-sm-6.h3")
    BASKET_EMPTY = (By.CSS_SELECTOR, "div#content_inner p")

class LoginPageLocators():
    LOG_IN_EMAIL_ADDRESS = (By.ID, "#id_login-username")
    LOG_IN_PASSWORD = (By.ID, "#id_login-password")
    REG_EMAIL_ADDRESS = (By.CSS_SELECTOR, "input#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password1")
    REG_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password2")
    BUTTON_REGISTER = (By.XPATH, '//button[@value = "Register"]')
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
