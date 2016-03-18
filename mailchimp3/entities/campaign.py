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

    def create(self, data):
        return self._mc_client._post(url=self.endpoint, data=data)

    def patch(self, campaign_id, data):
        return self._mc_client._patch(url=self._build_path(campaign_id), data=data)

    # Pro feature
    def cancel(self, campaign_id):
        return self._mc_client._post(url=self._build_path(campaign_id, 'actions', 'cancel-send'))

    def send(self, campaign_id):
        return self._mc_client._post(url=self._build_path(campaign_id, 'actions', 'send'), data={})

    def set_content(self, campaign_id, data):
        return self._mc_client._put(url=self._build_path(campaign_id, 'content'), data=data)

    def get_content(self, campaign_id, **kwargs):
        return self._mc_client._get(url=self._build_path(campaign_id, 'content'), **kwargs)

    def feedbacks(self):
        feedback_api = Feedback()
        return feedback_api.all(self.campaign_id)
