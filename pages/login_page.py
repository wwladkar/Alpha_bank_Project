from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = BasePage.alpha_url

    def open_browser(self):
        self.open(self.url)

    def login(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

