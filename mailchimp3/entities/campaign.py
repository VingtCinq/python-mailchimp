from ..baseapi import BaseApi
from .feedback import Feedback


class Campaign(BaseApi):

    def __init__(self, *args, **kwargs):
        super(Campaign, self).__init__(*args, **kwargs)
        self.endpoint = 'campaigns'
        self.campaign_id = None

    def all(self, **kwargs):
        return self._mc_client._get(url=self.endpoint, **kwargs)

    def get(self, campaign_id):
        self.campaign_id = campaign_id
        return self._mc_client._get(url=self._build_path(campaign_id))

    def delete(self, campaign_id):
        return self._mc_client._delete(url=self._build_path(campaign_id))

    def feedbacks(self):
        return Feedback.all(self.campaign_id)
