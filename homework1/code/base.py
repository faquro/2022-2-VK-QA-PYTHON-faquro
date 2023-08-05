import random
import time

import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ui.locators import basic_locators


class BaseFunc:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    @pytest.fixture
    def rand_profile_data(self):
        inn = random.randint(100000000000, 999999999999)
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        fio = ''.join(random.choice(letters) for _ in range(random.randint(3, 15)))
        return inn, fio

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 10
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None) -> WebElement:
        for i in range(20):
            try:
                self.find(locator, timeout=timeout)
                elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                elem.click()
                break
            except Exception:
                time.sleep(0.5)
        else:
            raise TimeoutException("Кнопка не нажимается")

    def input_placeholder(self, text, locator, timeout):
        input = self.find(locator, timeout=timeout)
        input.clear()
        input.send_keys(text)

    def login(self, mylogin, mypass, timeout):
        self.click(basic_locators.AUTH_BUTTON, timeout)
        email = self.find(basic_locators.EMAIL_INPUT, timeout=timeout)
        email.send_keys(mylogin)
        password = self.find(basic_locators.PASSWORD_INPUT, timeout=timeout)
        password.send_keys(mypass)
        self.click(basic_locators.AUTH_ACCEPT_BUTTON, timeout)
