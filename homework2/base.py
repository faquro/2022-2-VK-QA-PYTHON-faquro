import pytest
from _pytest.fixtures import FixtureRequest

from .ui.pages.dashboard_page import DashboardPage


class BaseFunc:
    is_authorized = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self,
              driver,
              config,
              base_page,
              request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.base_page = base_page

        if self.is_authorized:
            self.dashboard_page: DashboardPage = request.getfixturevalue(
                'dashboard_page'
            )
