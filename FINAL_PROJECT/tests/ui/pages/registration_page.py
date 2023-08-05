from .base_page import BasePage
from ..locators.basic_locators import Registration_Page_Locators


class RegistrationPage(BasePage):
    locators = Registration_Page_Locators()

    def find_input(self, locator):
        input_locators = [self.locators.USER_NAME_INPUT, self.locators.USER_SURNAME_INPUT,
                          self.locators.USER_MIDDLE_NAME_INPUT, self.locators.USERNAME_INPUT, self.locators.EMAIL_INPUT,
                          self.locators.PASS_INPUT, self.locators.REPEAT_PASS_INPUT]
        place = self.find(input_locators[locator])
        return place

    def register(self, userdata):
        self.click(self.locators.CREATE_ACC_LINK)
        self.send_keys(self.locators.USER_NAME_INPUT, userdata['name'])
        self.send_keys(self.locators.USER_SURNAME_INPUT, userdata['surname'])
        self.send_keys(self.locators.USER_MIDDLE_NAME_INPUT, userdata['middle_name'])
        self.send_keys(self.locators.USERNAME_INPUT, userdata['username'])
        self.send_keys(self.locators.PASS_INPUT, userdata['password'])
        self.send_keys(self.locators.REPEAT_PASS_INPUT, userdata['pass_repeat'])
        self.send_keys(self.locators.EMAIL_INPUT, userdata['email'])
        self.click(self.locators.ACCEPT)
        self.click(self.locators.REGISTER_BUTTON)

    def register_without_accept(self, userdata):
        self.click(self.locators.CREATE_ACC_LINK)
        self.send_keys(self.locators.USERNAME_INPUT, userdata['username'])
        self.send_keys(self.locators.PASS_INPUT, userdata['password'])
        self.send_keys(self.locators.REPEAT_PASS_INPUT, userdata['pass_repeat'])
        self.send_keys(self.locators.EMAIL_INPUT, userdata['email'])
        self.click(self.locators.REGISTER_BUTTON)

    def is_registration_page(self):
        return self.driver.current_url == f'http://myapp_final_project:8082/reg'

    def go_to_login(self):
        self.click(self.locators.CREATE_ACC_LINK)
        self.click(self.locators.GO_TO_LOGIN_LINK)
        return self.driver
