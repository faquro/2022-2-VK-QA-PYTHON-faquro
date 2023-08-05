import pytest

from .static import ADMIN_USER, ADMIN_PASSWORD
#import static
from .ui.pages.account_page import AccountPage
from .ui.pages.base_page import BasePage
from .ui.pages.registration_page import RegistrationPage


class BaseCase:
    is_authorized = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self,
              driver,
              config,
              mysql_builder):
        self.driver = driver
        self.config = config
        self.base_page = BasePage(driver)
        self.registration_page = RegistrationPage(driver)
        self.account_page = AccountPage(driver)
        self.mysql_builder = mysql_builder

        if self.is_authorized:
            self.base_page.login(ADMIN_USER, ADMIN_PASSWORD)
