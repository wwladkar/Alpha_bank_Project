from pages.base_page import BasePage
from pages.locators import StartPageLocators


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = BasePage.sber_url

    def click_person_button(self):
        self.open(self.url)
        self.click_element(StartPageLocators.PERSON_BUTTON)

    def click_selfbusy_button(self):
        self.open(self.url)
        self.click_element(StartPageLocators.SELFBUSY_BUTTON)
