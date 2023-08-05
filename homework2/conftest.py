from homework2.ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption('--url', default='https://target-sandbox.my.com/')
    parser.addoption('--headless', action='store_true')


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "UI: mark test to run only UI"
    )


@pytest.fixture(scope='session')
def config(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption('--url')
    headless = request.config.getoption("--headless")
    return {"browser": browser, "url": url, "headless": headless}
