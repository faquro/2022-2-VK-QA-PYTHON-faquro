from selenium.webdriver import ActionChains

from ..locators.basic_locators import Account_Page_Locators
from .base_page import BasePage


class AccountPage(BasePage):
    locators = Account_Page_Locators()

    def go_to_api(self):
        self.click(self.locators.GO_TO_API_LINK)
        return self.driver

    def go_to_internet(self):
        self.click(self.locators.GO_TO_INTERNET_LINK)
        return self.driver

    def go_to_smtp(self):
        self.click(self.locators.GO_TO_SMTP_LINK)
        return self.driver

    def go_to_home(self):
        self.click(self.locators.HOME_LINK)
        return self.driver

    def go_to_python(self):
        self.click(self.locators.PYTHON_LINK)
        return self.driver

    def go_to_python_history(self):
        main_item = self.find(self.locators.PYTHON_LINK)
        sub_item = self.find(self.locators.PYTHON_HISTORY_LINK)
        ActionChains(self.driver).move_to_element(main_item).click(sub_item).perform()

    def go_to_flask(self):
        main_item = self.find(self.locators.PYTHON_LINK)
        sub_item = self.find(self.locators.FLASK_LINK)
        ActionChains(self.driver).move_to_element(main_item).click(sub_item).perform()

    def go_to_centos(self):
        main_item = self.find(self.locators.LINUX_LINK)
        sub_item = self.find(self.locators.CENTOS_LINK)
        ActionChains(self.driver).move_to_element(main_item).click(sub_item).perform()

    def go_to_news(self):
        main_item = self.find(self.locators.NETWORK_LINK)
        sub_item = self.find(self.locators.NEWS_LINK)
        ActionChains(self.driver).move_to_element(main_item).click(sub_item).perform()

    def go_to_download(self):
        main_item = self.find(self.locators.NETWORK_LINK)
        sub_item = self.find(self.locators.DOWNLOAD_LINK)
        ActionChains(self.driver).move_to_element(main_item).click(sub_item).perform()

    def go_to_examples(self):
        main_item = self.find(self.locators.NETWORK_LINK)
        sub_item = self.find(self.locators.EXAMPLES_LINK)
        ActionChains(self.driver).move_to_element(main_item).click(sub_item).perform()

    def logout(self):
        self.click(self.locators.LOGOUT_LINK)
        return self.driver
