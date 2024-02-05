from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_FIELD = (By.CSS_SELECTOR, "#username")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
