from pages.locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://cbdev-ez/#/portal/dashboard/dashboard"

    def login(self, username, password):
        self.open(self.url)
        self.enter_text(LoginPageLocators.USERNAME_FIELD, username)
        self.enter_text(LoginPageLocators.PASSWORD_FIELD, password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)