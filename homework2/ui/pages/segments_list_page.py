import time

from selenium.common.exceptions import TimeoutException

from ..locators.basic_locators import Segments_Page_Locators
from ..pages.base_page import BasePage


class SegmentListPage(BasePage):
    locators = Segments_Page_Locators()

    def add_segment(self, segment_name, segment_type):
        segment_locator = self.locators.create_segment_type_locator(segment_type)
        self.click(self.locators.SEGMENT_LIST)
        if self.check_exist(*self.locators.HAS_SEGMENTS) == 0:
            add_segment_button = self.locators.NEW_SEGMENT_LINK
        else:
            add_segment_button = self.locators.NEW_SEGMENT_LINK_BUTTON
        self.click(add_segment_button)
        self.click(segment_locator)
        self.click(self.locators.SEGMENT_SOURCE_CHECKBOX)
        self.click(self.locators.ADD_SEGMENT_BUTTON)
        self.input_placeholder(segment_name, self.locators.TITLE_SEGMENT_INPUT)
        self.click(self.locators.CREATE_SEGMENT_BUTTON)

    def input_placeholder(self, text, locator, timeout=5):
        input = self.find(locator, timeout=timeout)
        input.clear()
        input.send_keys(text)

    def check_exist(self, by, locator):
        time.sleep(5)
        return len(self.driver.find_elements(by, locator))

    def add_group_list(self, url):
        self.click(self.locators.GROUP_VK_OK)
        self.input_placeholder(url, self.locators.GROUP_VK_OK_INPUT, 5)
        self.click(self.locators.GROUP_VK_OK_SELECT)
        self.click(self.locators.GROUP_VK_OK_ADD)

    def remove_segment(self):
        self.click(self.locators.SEGMENT_LIST)
        self.click(self.locators.REMOVE_SEGMENT_ICON)
        self.click(self.locators.REMOVE_SEGMENT_CONFIRM_BUTTON)

    def remove_group(self):
        self.click(self.locators.GROUP_VK_OK)
        self.click(self.locators.REMOVE_SOURCE_ICON)
        self.click(self.locators.REMOVE_SOURCE_CONFIRM_BUTTON)

    def has_segments(self, segment_name):
        locator = self.locators.create_segment_cell_locator(segment_name)
        try:
            self.find(locator)
            return True
        except TimeoutException:
            return False

    def has_group_list(self, url):
        group_locator = self.locators.create_link_added_locator(url)
        try:
            self.find(group_locator)
            return True
        except TimeoutException:
            return False
