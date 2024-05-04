import time

from pages.start_page import LoginPage
from pages.settlement_event_page import SettlementEventPage
from pages.swift_page import SwiftPage


def test_ovn_happy_path(browser):
    login_page = LoginPage(browser)
    login_page.login("VKarpushkin", "kbepY5uLy")

    assert browser.current_url == f" {LoginPage.sber_url} #/" or f"{LoginPage.sber_url}#/portal/dashboard/dashboard"

    swift_page = SwiftPage(browser)
    swift_page.swift()
    time.sleep(10)

    assert browser.current_url == f"{SwiftPage.sber_url}#/portal/swift/list/all"

    settlement_event_page = SettlementEventPage(browser)
    settlement_event_page.settlement_event()
    time.sleep(10)

    assert browser.current_url == (f"{SettlementEventPage.sber_url}"
                                   f"#/portal/enrichment/enrichment/list/JUQwJUEwJUQwJUIwJUQxJTgxJUQxJTg3JUQwJUI1JUQxJTgyJUQwJUJEJUQwJUJFJUQwJUI1JTIwJUQxJTgxJUQwJUJFJUQwJUIxJUQxJThCJUQxJTgyJUQwJUI4JUQwJUI1")
