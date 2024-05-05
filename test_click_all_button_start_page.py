from pages.start_page import StartPage


def test_click_person_button(browser):
    start_page = StartPage(browser)
    start_page.click_person_button()

    assert browser.current_url == "https://www.sberbank.ru/ru/person"


#def test_click_self_employed_button(browser):
#    start_page = StartPage(browser)
#    start_page.click_self_employed_button()

#    assert browser.current_url == "https://www.sberbank.com/ru/svoedelo/start"


#def test_click_s_m_business_button(browser):
#    start_page = StartPage(browser)
#    start_page.click_s_m_business_button()

#    assert browser.current_url == "https://www.sberbank.com/ru/s_m_business"


#def test_click_currencies_button(browser):
#    start_page = StartPage(browser)
#    start_page.click_currencies_button()

#    assert browser.current_url == "https://www.sberbank.ru/ru/quotes/currencies"


#def test_click_offices_button(browser):
#    start_page = StartPage(browser)
#    start_page.click_offices_button()

#    assert browser.current_url == "https://www.sberbank.com/ru/oib?tab=vsp"


#def test_click_atms_button(browser):
#    start_page = StartPage(browser)
#    start_page.click_atms_button()

#    assert browser.current_url == "https://www.sberbank.com/ru/oib_atm?tab=atm"
