from pages.base_page import BasePage
from pages.locators import StartPageLocators


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = BasePage.alpha_url

    def click_person_button(self):
        self.open(self.url)
        self.click_element(StartPageLocators.PERSON_BUTTON)

    def click_s_m_business_button(self):
        self.open(self.url)
        self.click_element(StartPageLocators.S_M_BUSINESS_BUTTON)

    def click_for_corporations_button(self):
        self.open(self.url)
        self.click_element(StartPageLocators.FOR_CORPORATIONS_BUTTON)

    def click_currencies_button(self):
        self.open(self.url)
        self.click_element(StartPageLocators.CURRENCIES_BUTTON)

    def click_offices_button(self):
        self.open(self.url)
        self.click_element(StartPageLocators.OFFICES_BUTTON)

    def click_atms_button(self):
        self.open(self.url)
        self.click_element(StartPageLocators.ATMS_BUTTON)
