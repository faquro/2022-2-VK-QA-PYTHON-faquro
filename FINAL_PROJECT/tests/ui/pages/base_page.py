from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


from ..locators.basic_locators import Login_Page_Locators

CLICK_RETRY = 3
BASE_TIMEOUT = 10


class BasePage(object):
    locators = Login_Page_Locators()

    def __init__(self, driver):
        self.driver = driver


    def find(self, locator, timeout=10):
        try:
            return self.wait(timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise NoSuchElementException

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def search(self, query):
        search = self.find(self.locators.QUERY_LOCATOR)
        search.clear()
        search.send_keys(query)
        self.click(self.locators.GO_LOCATOR)

    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def send_keys(self, locator, key, timeout=None):
        element = self.find(locator, timeout=timeout)
        element.send_keys(key)

    def go_to_registration(self):
        self.click(self.locators.CREATE_ACC_LINK)
        return self.driver

    def login(self, username, password):
        self.send_keys(self.locators.LOGIN_INPUT, username)
        self.send_keys(self.locators.PASS_INPUT, password)
        self.click(self.locators.LOGIN_BUTTON)
        return self.driver

    def is_login_page(self):
        return self.driver.current_url == f'http://myapp_final_project:8082/login'
