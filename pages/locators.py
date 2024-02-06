from selenium.webdriver.common.by import By


class DevLoginPageLocators:
    USERNAME_FIELD = (By.CSS_SELECTOR, "#username")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[type='submit']")


class TestLoginPageLocators:
    USERNAME_FIELD = (By.CSS_SELECTOR, "[class='ng-tns-c43-697 ng-star-inserted']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[class='ng-tns-c43-698 ng-star-inserted']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-testid='loginButton']")
