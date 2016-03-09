from ..baseapi import BaseApi
from .feedback import Feedback


class Root(BaseApi):

    def __init__(self, *args, **kwargs):
        super(Campaign, self).__init__(*args, **kwargs)
        self.endpoint = ''

    def get(self, data):
        self.campaign_id = campaign_id
        return self._mc_client._get(url=self._build_path(campaign_id))
