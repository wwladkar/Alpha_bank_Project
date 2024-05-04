from selenium.webdriver.common.by import By


class StartPageLocators:
    PERSON_BUTTON = (By.CSS_SELECTOR, "[data-cga_click_segment='Частным клиентам']")
    SELF_EMPLOYED_BUTTON = (By.CSS_SELECTOR, "[aria-label] .kitt-header-sections__item_first:nth-of-type(2) [href]")
    S_M_BUSINESS_BUTTON = (By.CSS_SELECTOR, "[data-cga_click_segment='Малому бизнесу и ИП']")
    CURRENCIES_BUTTON = (By.CSS_SELECTOR, ".kitt-header__links [href='https\:\/\/www\.sberbank\.ru\/ru\/quotes\/currencies']")
    OFFICES_BUTTON = (By.CSS_SELECTOR, ".kitt-header__links > a:nth-of-type(2)")
    ATMS_BUTTON = (By.CSS_SELECTOR, ".kitt-header__links > a:nth-of-type(3)")



