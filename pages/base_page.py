from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import stand


class BasePage:
    stand = "dev"

    if stand == "test":
        ezdoc_url = "http://192.168.00.00:00000/"
    elif stand == "dev":
        ezdoc_url = "http://xxxxx-xx/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # Устанавливаем время ожидания в 10 секунд

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)
