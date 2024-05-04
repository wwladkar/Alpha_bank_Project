from pages.start_page import StartPage


def test_click_person_button(browser):
    start_page = StartPage(browser)
    start_page.click_person_button()

    assert browser.current_url == f"{StartPage.sber_url}/ru/person"


def test_click_selfbusy_button(browser):
    start_page = StartPage(browser)
    start_page.click_selfbusy_button()

    assert browser.current_url == f"{StartPage.sber_url}/ru/svoedelo"


def test_click_s_m_business_button(browser):
    start_page = StartPage(browser)
    start_page.click_s_m_business_button()

    assert browser.current_url == "https://www.sberbank.com/ru/s_m_business"