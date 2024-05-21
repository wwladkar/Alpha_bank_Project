from pages.start_page import StartPage


#def test_click_person_button(browser):
#    start_page = StartPage(browser)
#    start_page.click_person_button()

#    assert browser.current_url == "https://alfabank.ru/"


#def test_click_s_m_business_button(browser):
#    start_page = StartPage(browser)
#    start_page.click_s_m_business_button()

#    assert browser.current_url == "https://alfabank.ru/sme/"


#def test_click_for_corporations_button(browser):
#    start_page = StartPage(browser)
#    start_page.click_for_corporations_button()

#    assert browser.current_url == "https://alfabank.ru/corporate/"


#def test_click_for_financial_button(browser):
#    start_page = StartPage(browser)
#    start_page.click_for_financial_button()

#    assert browser.current_url == "https://alfabank.ru/financial/"


def test_click_alpha_club_button(browser):
    start_page = StartPage(browser)
    start_page.click_more_button()
    start_page.click_alpha_club_button()

    assert browser.current_url == "https://alfabank.ru/a-club/"


#def test_click_atms_button(browser):
#    start_page = StartPage(browser)
#    start_page.click_atms_button()

#    assert browser.current_url == "https://www.sberbank.com/ru/oib_atm?tab=atm"
