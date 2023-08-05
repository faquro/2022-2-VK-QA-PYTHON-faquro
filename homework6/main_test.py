import os

import pytest

from homework6.mysql.builder import MySQLBuilder
from homework6.mysql.models import TotalRequestCount, RequestCountByType, Top_FrequentURL, Top_4XX_Error, Top_5XX_Error
from homework6.static import top, top_4XX, top_5XX


class MySQLBase:

    def prepare(self):
        pass

    def get_filepath(self, file_name):
        return os.path.join(self.repo_root, file_name)

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client, repo_root):
        self.mysql = mysql_client
        self.repo_root = repo_root
        file_path = self.get_filepath('access.vk')
        self.mysql_builder: MySQLBuilder = MySQLBuilder(mysql_client, path=file_path)
        self.prepare()


class TestCountTotal(MySQLBase):

    def prepare(self):
        self.mysql_builder.count_total()

    def test_total_request_count(self):
        result = self.mysql.session.query(TotalRequestCount).all()
        assert len(result) == 1


class TestCountByType(MySQLBase):

    def prepare(self):
        self.mysql_builder.count_by_type()

    def test_request_count_by_type(self):
        result = self.mysql.session.query(RequestCountByType)
        assert len(result.all()) == 4


class TestTop(MySQLBase):

    def prepare(self):
        self.mysql_builder.top()

    def test_top_frequent_urls(self):
        result = self.mysql.session.query(Top_FrequentURL)
        assert len(result.all()) == top


class TestTop_4XX(MySQLBase):

    def prepare(self):
        self.mysql_builder.top_4xx_requests()

    def test_top_4XX_error(self):
        result = self.mysql.session.query(Top_4XX_Error).all()
        assert len(result) == top_4XX


class TestTop_5XX(MySQLBase):

    def prepare(self):
        self.mysql_builder.top_5xx_users()

    def test_top_5XX_error(self):
        result = self.mysql.session.query(Top_5XX_Error)
        assert len(result.all()) == top_5XX
