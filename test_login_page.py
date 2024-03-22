from pages.login_page import LoginPage


def test_login(browser):
    login_page = LoginPage(browser)
    login_page.login("********", "********")

    assert browser.current_url == f" {LoginPage.ezdoc_url} #/" or f"{LoginPage.ezdoc_url}#/portal/dashboard/dashboard"
