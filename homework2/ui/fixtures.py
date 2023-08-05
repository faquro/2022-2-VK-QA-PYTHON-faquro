import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from ..static import login, password

from ..ui.pages.base_page import BasePage
from ..ui.pages.dashboard_page import DashboardPage


class UnsupportedBrowserType(Exception):
    pass


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def dashboard_page(driver, base_page):
    return DashboardPage(base_page.login(login, password, 10))


def get_driver(config, browser_name):
    options = webdriver.ChromeOptions()
    if config is not False:
        options.add_argument('headless')
    browser = webdriver.Chrome(executable_path=ChromeDriverManager(version="105.0.5195.19").install(),
                               options=options
                               )
    return browser


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    headless = config['headless']
    browser_type = config['browser']
    browser = get_driver(headless, browser_type)
    browser.get(url)
    browser.set_window_size(1920, 1080)
    yield browser
    browser.quit()
