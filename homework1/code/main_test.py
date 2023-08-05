import pytest

import static
from base import BaseFunc
from ui.locators import basic_locators

TIMEOUT = 10


@pytest.mark.UI
class TestUI(BaseFunc):

    def test_auth(self):
        self.login(static.login, static.password, TIMEOUT)

        assert self.find(basic_locators.USER_NAME_WRAP, TIMEOUT)

    @pytest.mark.parametrize(
        'mylogin, mypass', [('pycon', static.password),
                            (static.login, 'PASSWORDKEKS')
                            ]
    )
    def test_auth_neg(self, mylogin, mypass):
        self.login(mylogin, mypass, TIMEOUT)
        if "https://target-sandbox.my.com/" in self.driver.current_url:

            assert self.find(basic_locators.AUTH_WRONG_LOGIN, TIMEOUT)
        else:

            assert "Invalid login or password" in self.driver.page_source

    def test_logout(self):
        self.login(static.login, static.password, TIMEOUT)
        self.find(basic_locators.MAIN_PAGE, TIMEOUT)
        self.click(basic_locators.RIGHT_USER_MENU, TIMEOUT)
        self.click(basic_locators.RIGHT_MENU_LOGOUT, TIMEOUT)

        assert self.find(basic_locators.AUTH_BUTTON, TIMEOUT)

    def test_edit_profile(self, rand_profile_data):
        inn = rand_profile_data[0]
        fio = rand_profile_data[1]
        self.login(static.login, static.password, TIMEOUT)
        self.click(basic_locators.CENTER_MENU_PROFILE, TIMEOUT)
        self.input_placeholder(fio, basic_locators.FIO_PROFILE_INPUT, TIMEOUT)
        self.input_placeholder(inn, basic_locators.INN_PROFILE_INPUT, TIMEOUT)
        self.click(basic_locators.PROFILE_ACCEPT_BUTTON, TIMEOUT)
        self.find(basic_locators.SUCCESS_NOTIFY, TIMEOUT)
        self.driver.refresh()
        self.find(basic_locators.FIO_PROFILE_INPUT)

        assert fio in self.driver.page_source

    @pytest.mark.parametrize(
        'button_locator, assert_locator', [(basic_locators.CENTER_MENU_STATISTICS, basic_locators.STATISTICS_PAGE),
                                           (basic_locators.CENTER_MENU_PROFILE, basic_locators.PROFILE_PAGE)
                                           ]
    )
    def test_center_module_buttons(self, button_locator, assert_locator):
        self.login(static.login, static.password, TIMEOUT)
        self.click(button_locator, TIMEOUT)

        assert self.find(assert_locator, TIMEOUT)
