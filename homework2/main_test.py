import pytest

from .static import app_games, ok_vk, group_url
from .base import BaseFunc


@pytest.mark.UI
class TestUI(BaseFunc):

    def test_add_campaign(self):
        campaign_name = 'Test_company'
        self.dashboard_page.add_campaign(campaign_name)

        assert self.dashboard_page.campaign_exists(campaign_name)
        self.dashboard_page.remove_campaign()

    def test_add_segment(self):
        segment_name = "Test_Games"
        segment_type = app_games
        segments_page = self.dashboard_page.go_to_segments()
        segments_page.add_segment(segment_name, segment_type)

        assert segments_page.has_segments(segment_name)
        segments_page.remove_segment()

    def test_add_segment_vk(self):
        segment_name = "Test_VK"
        segment_type = ok_vk
        url = group_url
        segments_page = self.dashboard_page.go_to_segments()
        segments_page.add_group_list(url)

        assert segments_page.has_group_list(url)
        segments_page.add_segment(segment_name, segment_type)

        assert segments_page.has_segments(segment_name)
        segments_page.remove_segment()
        segments_page.remove_group()
