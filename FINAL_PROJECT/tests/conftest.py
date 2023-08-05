import os
import random
import string
import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from .mysql.builder import MySQLBuilder
from .mysql.client import MysqlClient


def pytest_addoption(parser):
    parser.addoption('--url', default=f'http://myapp_final_project:8082')
    parser.addoption('--selenoid', default=f'http://selenoid_final_project:4444')


@pytest.fixture(scope="session")
def config(request):
    url = request.config.getoption('--url')
    selenoid = request.config.getoption('--selenoid')
    return {"url": url, "selenoid": selenoid}


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    selenoid_server = config["selenoid"]
    options = ChromeOptions()
    if selenoid_server:
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "108.0",
            "selenoid:options": {
                "enableVideo": False
            }
        }

        browser = webdriver.Remote(
            command_executor="http://0.0.0.0:4444/wd/hub",
            desired_capabilities=capabilities)
    else:
        manager = ChromeDriverManager(version='latest')
        browser = webdriver.Chrome(
            executable_path=manager.install(),
            options=options
        )
    browser.get(url)
    print(url)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope='session')
def mysql_client():
    mysql_client = MysqlClient(user='root', password='pass')
    mysql_client.connect()
    mysql_client.create_tables()
    yield mysql_client
    mysql_client.connection.close()


@pytest.fixture(scope='session')
def mysql_builder(mysql_client):
    builder = MySQLBuilder(mysql_client)
    return builder


@pytest.fixture(scope='function')
def userdata():
    base = string.ascii_lowercase
    name = ''.join(random.choice(base) for i in range(7))
    surname = ''.join(random.choice(base) for i in range(7))
    middle_name = ''.join(random.choice(base) for i in range(7))
    username = ''.join(random.choice(base) for i in range(7))
    password = ''.join(random.choice(base) for i in range(7))
    email = ''.join(random.choice(base) for i in range(7))
    email += '@myapp.ru'
    return {'name': name, 'surname': surname, 'middle_name': middle_name, 'username': username, 'email': email,
            'password': password, 'pass_repeat': password, }


@pytest.fixture(scope='function')
def random_string():
    base = string.ascii_lowercase
    return ''.join(random.choice(base) for i in range(7))


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'driver' in item.fixturenames:
                    web_driver = item.funcargs['driver']
                else:
                    print('Fail to take screen-shot')
                    return
            time.sleep(1)
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))
