from selenium.webdriver.common.by import By


class StartPageLocators:
    PERSON_BUTTON = (By.CSS_SELECTOR, "a[title='Частным лицам']")
    S_M_BUSINESS_BUTTON = (By.CSS_SELECTOR, "a[title='Малому бизнесу и ИП']")
    FOR_CORPORATIONS_BUTTON = (By.CSS_SELECTOR, "a[title='Корпорациям']")
    CURRENCIES_BUTTON = (By.CSS_SELECTOR, r".kitt-header__links [href='https\:\/\/www\.sberbank\.ru\/ru\/quotes"
                                          r"\/currencies']")
    OFFICES_BUTTON = (By.CSS_SELECTOR, ".kitt-header__links > a:nth-of-type(2)")
    ATMS_BUTTON = (By.CSS_SELECTOR, ".kitt-header__links > a:nth-of-type(3)")



