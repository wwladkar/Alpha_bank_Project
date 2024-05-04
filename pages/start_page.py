from pages.base_page import BasePage
from pages.locators import StartPageLocators


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = BasePage.sber_url

    def click_person_button(self):
        self.open(self.url)
        self.click_element(StartPageLocators.PERSON_BUTTON)

    def click_self_employed_button(self):
        self.open(self.url)
        self.click_element(StartPageLocators.SELF_EMPLOYED_BUTTON)

    def click_s_m_business_button(self):
        self.open(self.url)
        self.click_element(StartPageLocators.S_M_BUSINESS_BUTTON)
