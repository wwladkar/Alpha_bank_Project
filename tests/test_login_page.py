from pages.login_page import LoginPage


def test_login(browser):
    login_page = LoginPage(browser)
    login_page.login("testuser", "password123")

    assert browser.current_url == "https://www.example.com/home"
