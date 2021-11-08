from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None , help='Выбери язык браузера')


@pytest.fixture()
def browser(request):
    browser_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    browser = webdriver.Chrome(options=options)
    print('..:: STARTING BROWSER ::..')

    yield browser
    print('..:: CLOSING BROWSER ::..')
    browser.quit()
