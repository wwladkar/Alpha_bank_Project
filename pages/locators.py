from selenium.webdriver.common.by import By


class StartPageLocators:
    PERSON_BUTTON = (By.CSS_SELECTOR, "[data-cga_click_segment='Частным клиентам']")
    SELFBUSY_BUTTON = (By.CSS_SELECTOR, "[aria-label] .kitt-header-sections__item_first:nth-of-type(2) [href]")
    S_M_BUSINESS_BUTTON = (By.CSS_SELECTOR, "[data-cga_click_segment='Малому бизнесу и ИП']")


class TestLoginPageLocators:
    USERNAME_FIELD = (By.CSS_SELECTOR, "[class='ng-tns-c43-697 ng-star-inserted']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[class='ng-tns-c43-698 ng-star-inserted']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-cga_click_segment='Малому бизнесу и ИП']")
