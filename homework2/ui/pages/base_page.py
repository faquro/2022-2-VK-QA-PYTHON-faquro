import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ..locators.basic_locators import Login_Page_Locators


class BasePage(object):
    locators = Login_Page_Locators()

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=None, has_to_be_clickable=False):
        if has_to_be_clickable:
            return self.wait(timeout).until(
                EC.element_to_be_clickable(locator)
            )
        return self.wait(timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

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

    def send_keys(self, locator, key, timeout=5, has_to_be_clickable=False):
        element = self.find(locator, timeout=timeout,
                            has_to_be_clickable=has_to_be_clickable)
        element.clear()
        element.send_keys(key)

    def login(self, mylogin, mypass, timeout):
        self.click(self.locators.AUTH_BUTTON, timeout)
        email = self.find(self.locators.EMAIL_INPUT, timeout=timeout)
        email.send_keys(mylogin)
        password = self.find(self.locators.PASSWORD_INPUT, timeout=timeout)
        password.send_keys(mypass)
        self.click(self.locators.AUTH_ACCEPT_BUTTON, timeout)
        return self.driver

    def is_authorized(self):
        try:
            self.find(self.locators.AUTH_BUTTON)
            return True
        except TimeoutException:
            return False
