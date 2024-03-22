import time

from pages.login_page import LoginPage
from pages.settlement_event_page import SettlementEventPage
from pages.swift_page import SwiftPage


def test_ovn_happy_path(browser):
    login_page = LoginPage(browser)
    login_page.login("********", "********")

    assert browser.current_url == f" {LoginPage.ezdoc_url} #/" or f"{LoginPage.ezdoc_url}#/portal/dashboard/dashboard"

    swift_page = SwiftPage(browser)
    swift_page.swift()
    time.sleep(10)

    assert browser.current_url == f"{SwiftPage.ezdoc_url}#/portal/swift/list/all"

    settlement_event_page = SettlementEventPage(browser)
    settlement_event_page.settlement_event()
    time.sleep(10)

    assert browser.current_url == (f"{SettlementEventPage.ezdoc_url}"
                                   f"#/portal/enrichment/enrichment/list/JUQwJUEwJUQwJUIwJUQxJTgxJUQxJTg3JUQwJUI1JUQxJTgyJUQwJUJEJUQwJUJFJUQwJUI1JTIwJUQxJTgxJUQwJUJFJUQwJUIxJUQxJThCJUQxJTgyJUQwJUI4JUQwJUI1")
