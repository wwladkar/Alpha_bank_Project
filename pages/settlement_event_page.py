from pages.base_page import BasePage
#from pages.locators import DevSwiftPageLocators, TestSwiftPageLocators


class SettlementEventPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = f'{BasePage.sber_url}#/portal/enrichment/enrichment/list/JUQwJUEwJUQwJUIwJUQxJTgxJUQxJTg3JUQwJUI1JUQxJTgyJUQwJUJEJUQwJUJFJUQwJUI1JTIwJUQxJTgxJUQwJUJFJUQwJUIxJUQxJThCJUQxJTgyJUQwJUI4JUQwJUI1'

    def settlement_event(self, stand="dev"):
        # if stand == "test":
        # swift_page_locators = TestSwiftPageLocators
        # elif stand == "dev":
        # swift_page_locators = DevSwiftPageLocators
        self.open(self.url)