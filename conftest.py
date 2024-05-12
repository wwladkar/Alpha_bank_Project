import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help='Choose browser: \'--browser_name=chrome\' or \'--browser_name=firefox\' or '
                          '\'--browser_name=yandex\'')
    parser.addoption('--language',
                     action='store',
                     default='en',
                     help="Choose language: '--language=en' or '--language=ru'")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = OptionsChrome()
        options.add_argument("start-maximized")
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                   options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options_firefox = OptionsFirefox()
        options_firefox.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),
                                    options=options_firefox)
    elif browser_name == "yandex":
        print("\nstart Yandex browser for test..")
        yandex_path = r"C:\Users\User\Downloads\yandexdriver-24.1.0.2570-win64\yandexdriver.exe"  # path to YandexDriver
        yandex_options = OptionsChrome()
        yandex_options.binary_location = yandex_path
        yandex_options.add_argument("start-maximized")
        yandex_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                   options=yandex_options)

    else:
        raise pytest.UsageError("--browser_name should be chrome, firefox, or yandex")
    yield browser
    print("\nquit browser..")
    browser.quit()
