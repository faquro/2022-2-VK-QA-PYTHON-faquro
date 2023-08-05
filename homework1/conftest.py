import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="https://target-sandbox.my.com/")
    parser.addoption('--headless', action='store_true')


@pytest.fixture()
def config(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    return {"browser": browser, "url": url, "headless": headless}


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "UI: mark test to run only UI"
    )


@pytest.fixture(scope='function')
def driver(config):
    browser = config["browser"]
    url = config["url"]
    options = webdriver.ChromeOptions()
    if config["headless"] is not False:
        options.add_argument('headless')
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager(version="105.0.5195.19").install(),
                                  chrome_options=options)
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.set_window_size(1280, 720)
    yield driver
    driver.quit()
