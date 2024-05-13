from selenium.webdriver.common.by import By


class StartPageLocators:
    PERSON_BUTTON = (By.CSS_SELECTOR, "a[title='Частным лицам']")
    S_M_BUSINESS_BUTTON = (By.CSS_SELECTOR, "a[title='Малому бизнесу и ИП']")
    FOR_CORPORATIONS_BUTTON = (By.CSS_SELECTOR, "a[title='Корпорациям']")
    FOR_FINANCIAL_BUTTON = (By.CSS_SELECTOR, "a[title='Финансовым организациям']")
    MORE_BUTTON = (By.CSS_SELECTOR, ".B3HYp > svg[role='img']")
    ALPHA_CLUB_BUTTON = (By.CSS_SELECTOR, "a[title='А-КЛУБ']")



