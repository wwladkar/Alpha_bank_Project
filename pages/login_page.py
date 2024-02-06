from pages.locators import TestLoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{BasePage.ezdoc_url}#/portal/dashboard/dashboard"

    def login(self, username, password):
        self.open(self.url)
        self.enter_text(TestLoginPageLocators.USERNAME_FIELD, username)
        self.enter_text(TestLoginPageLocators.PASSWORD_FIELD, password)
        self.click_element(TestLoginPageLocators.LOGIN_BUTTON)
