from selenium.webdriver.common.by import By


class Login_Page_Locators:
    AUTH_BUTTON = (By.XPATH, '//*[starts-with(@class, "responseHead-module-button")]')
    EMAIL_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    AUTH_ACCEPT_BUTTON = (By.XPATH, '//*[starts-with(@class, "authForm-module-button")]')
    USER_NAME_WRAP = (By.XPATH, '//*[starts-with(@class, "right-module-userNameWrap")]')


class Dashboard_Page_Locators:
    SEGMENTS_LINK = (By.XPATH, '//a[@href="/segments"]')
    CREATE_CAMPAIGN_BUTTON = (
    By.XPATH, '//div[contains(@class, "dashboard-module-createButtonWrap")]/div[contains(@data-test, "button")]')
    CLEAR_CAMPAIGN_TITLE = (By.XPATH, "//div[@class='input__clear js-input-clear']")
    TITLE_CAMPAIGN_INPUT = (By.XPATH, "//input[contains(@class, 'input__inp')]")
    TRAFFIC_TYPE_ITEM = (By.XPATH, "//div[contains(@class, '_traffic')]")
    URL_INPUT = (By.XPATH, "//input[contains(@class, 'mainUrl-module-searchInput')]")
    ADV_FORMAT = (By.ID, "patterns_banner_4")
    TITLE_INPUT = (By.XPATH, "//input[@placeholder='Введите заголовок объявления']")
    DESCRIPTION_INPUT = (By.XPATH, "//textarea[contains(@class, 'roles-module-roleTextarea')]")
    UPLOAD_IMAGE = (By.XPATH, '//div[contains(@class, "roles-module-uploadButton")]')
    UPLOAD_IMAGE_INPUT = (By.XPATH, "//input[@data-test='image_240x400']")
    NO_CAMPAIGN = (By.XPATH, '//*[contains(@class, "button-module-textWrapper") and contains(text(), "0")]')
    CREATE_CAMPAIGN_SUBMIT = (By.XPATH, "//div[contains(@class, 'js-save-button-wrap')]")
    CAMPAIGNS_TABLE = (By.XPATH, "//div[contains(@class, 'main-module-TableWrapper')]")
    CHECKBOX_CAMPAIGN = (By.XPATH, "//input[contains(@class, 'name-module-checkbox')]")
    CAMPAIGN_CONTROLS_MODULE = (By.XPATH, "//div[contains(@class, 'tableControls-module-selectItem')]")
    REMOVE_CAMPAIGN = (By.XPATH, "//li[@data-id='8']")

    def create_campaign_cell_locator(self, campaign_name):
        return (By.XPATH, f"//a[contains(@class, 'nameCell-module-campaignNameLink') " f"and @title='{campaign_name}']")


class Segments_Page_Locators:
    SEGMENT_PAGE = (By.XPATH, '//*[contains(@class, "instruction-module-wrapper")]')
    SEGMENT_NAME = (By.XPATH, '//*[contains(@class, "cells-module-nameCell")]/a[@title="test"]')
    GROUP_VK_OK = (By.XPATH, '//a[@href="/segments/groups_list"]')
    SEGMENT_LIST = (By.XPATH, '//a[@href="/segments/segments_list"]')
    GROUP_VK_OK_INPUT = (By.XPATH, '//input[contains(@class ,"multiSelectSuggester-module-searchInput")]')
    GROUP_VK_OK_SELECT = (
    By.XPATH, '//*[contains(@class ,"optionListTitle-module-control") and contains( @ data-test, "select_all")]')
    GROUP_VK_OK_ADD = (By.XPATH, '//*[contains(@class,"button-module-textWrapper")]')
    REMOVE_SOURCE_ICON = (By.XPATH, '//div[contains(@class, "js-remove-source")]')
    REMOVE_SOURCE_CONFIRM_BUTTON = (By.XPATH, '//button[contains(@class, "button_confirm-remove")]')
    HAS_SEGMENTS = (By.XPATH, '//*[contains(@class, "segmentsTable-module-idCellCheckbox")]')
    NEW_SEGMENT_LINK = (By.XPATH, '//*[@href="/segments/segments_list/new/"]')
    NEW_SEGMENT_LINK_BUTTON = (By.XPATH, '//*[contains(@class, "button_submit")]')
    SEGMENT_SOURCE_CHECKBOX = (By.XPATH, "//input[contains(@class, 'adding-segments-source__checkbox')]")
    ADD_SEGMENT_BUTTON = (By.XPATH, "//div[contains(@class, 'adding-segments-modal__btn')]")
    TITLE_SEGMENT_INPUT = (By.XPATH, "//div[@class='input input_create-segment-form'] //input")
    CREATE_SEGMENT_BUTTON = (By.XPATH, "//button[contains(@class, 'button_submit')]")
    SEGMENTS_TABLE = (By.XPATH, "//div[contains(@class, 'page_segments__tbl-wrap')]")
    REMOVE_SEGMENT_ICON = (By.XPATH, "//span[contains(@class, 'cells-module-removeCell')]")
    REMOVE_SEGMENT_CONFIRM_BUTTON = (By.XPATH, "//button[contains(@class, 'button_confirm-remove')]")

    def create_segment_cell_locator(self, segment_name):
        return (By.XPATH, f'//*[contains(@class, "cells-module-nameCell")]/a[@title="{segment_name}"]')

    def create_segment_type_locator(self, segment_type):
        return (By.XPATH, f'//*[contains(@class, "adding-segments-item") and contains(text(), "{segment_type}")]')

    def create_link_added_locator(self, url):
        return (By.XPATH, f'//a[@href="{url}"]')
