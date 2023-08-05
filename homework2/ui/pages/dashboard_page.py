import os

from selenium.common.exceptions import TimeoutException

from ..locators.basic_locators import Dashboard_Page_Locators
from ..pages.base_page import BasePage
from ..pages.segments_list_page import SegmentListPage


class DashboardPage(BasePage):
    locators = Dashboard_Page_Locators()

    def go_to_segments(self):
        self.click(Dashboard_Page_Locators.SEGMENTS_LINK)
        return SegmentListPage(self.driver)

    def add_campaign(self, campaign_name):
        url_for_campaign = 'https://kek.ru/'
        image_path = os.getcwd() + '/homework2/ui/pages/E66B11.jpg'
        self.click(self.locators.CREATE_CAMPAIGN_BUTTON)
        self.click(self.locators.TRAFFIC_TYPE_ITEM)
        self.send_keys(self.locators.URL_INPUT, url_for_campaign)
        self.click(self.locators.CLEAR_CAMPAIGN_TITLE)
        self.send_keys(self.locators.TITLE_CAMPAIGN_INPUT, campaign_name, has_to_be_clickable=True)
        self.click(self.locators.ADV_FORMAT)
        self.find(self.locators.UPLOAD_IMAGE)
        self.upload_file(*self.locators.UPLOAD_IMAGE_INPUT, image_path)
        self.click(self.locators.CREATE_CAMPAIGN_SUBMIT)

    def upload_file(self, by, locator, file_path):
        elem = self.driver.find_element(by, locator)
        elem.send_keys(file_path)

    def remove_campaign(self):
        self.click(self.locators.CHECKBOX_CAMPAIGN)
        self.click(self.locators.CAMPAIGN_CONTROLS_MODULE)
        self.click(self.locators.REMOVE_CAMPAIGN)
        self.find(self.locators.NO_CAMPAIGN)

    def campaign_exists(self, campaign_name):
        locator = self.locators.create_campaign_cell_locator(campaign_name)
        try:
            self.find(locator, timeout=10)
            return True
        except TimeoutException:
            return False
