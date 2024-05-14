from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver


class BasePage:
    alpha_url = 'https://alfabank.ru/'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # Устанавливаем время ожидания в 10 секунд

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def hover_element(self, locator):
        element = self.find_element(locator)
        ActionChains(driver).move_to_element(element).perform()

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def hover_and_click_element(self, locator):
        element = self.find_element(locator)
        ActionChains(driver).move_to_element(element).perform()
        element.click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)
