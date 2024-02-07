from pages.base_page import BasePage
from pages.locators import DevLoginPageLocators, TestLoginPageLocators


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{BasePage.ezdoc_url}#/portal/dashboard/dashboard"

    def login(self, username, password, login_page_locators=None):

        stand = "dev"

        if stand == "test":
            login_page_locators = TestLoginPageLocators
        elif stand == "dev":
            login_page_locators = DevLoginPageLocators
        self.open(self.url)
        self.enter_text(login_page_locators.USERNAME_FIELD, username)
        self.enter_text(login_page_locators.PASSWORD_FIELD, password)
        self.click_element(login_page_locators.LOGIN_BUTTON)
