import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--stand',
                     action='store',
                     default='test',
                     help="Choose stand: '--stand=test' or '--stand=dev'")


@pytest.fixture(scope="function")
def browser(request):
    stand = request.config.getoption("stand")

    if stand == "test":

        print("\nstart cbtest")
        options = OptionsChrome()
        options.add_argument("start-maximized")
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                   options=options)

    elif stand == "dev":

        print("\nstart cbdev")
        options = OptionsChrome()
        options.add_argument("start-maximized")
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                   options=options)

    else:
        raise pytest.UsageError("Choose stand: '--stand=test' or '--stand=dev'")
    yield browser
    print("\nquit browser..")
    browser.quit()
