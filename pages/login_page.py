from locators import LoginPageLocators
from base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.example.com/login"

    def login(self, username, password):
        self.open(self.url)
        self.enter_text(LoginPageLocators.USERNAME_FIELD, username)
        self.enter_text(LoginPageLocators.PASSWORD_FIELD, password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)