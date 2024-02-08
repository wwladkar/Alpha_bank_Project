import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--stand',
                     action='store',
                     default='dev',
                     help="Choose stand: '--stand=test' or '--stand=dev'")


def stand(request):
    stand_name = request.config.getoption("stand")
    return stand_name


@pytest.fixture(scope="function")
def browser():
    options = OptionsChrome()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                              options=options)
    yield driver
    print("\nquit browser..")
    driver.quit()
