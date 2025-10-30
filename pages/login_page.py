from base_page import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = BasePage.alpha_url

    def open_browser(self):
        self.open(self.url)

    def click_person_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

