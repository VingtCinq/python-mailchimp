from ..baseapi import BaseApi


class Feedback(BaseApi):

    def __init__(self, *args, **kwargs):
        super(Feedback, self).__init__(*args, **kwargs)
        self.endpoint = 'campaigns'

    def all(self, campaign_id):
        return self._mc_client._get(url=self._build_path(campaign_id, 'feedback'))

    def get(self, campaign_id, feedback_id):
        return self._mc_client._get(url=self._build_path(campaign_id, 'feedback', feedback_id))

    def delete(self, campaign_id, feedback_id):
        return self._mc_client._delete(url=self._build_path(campaign_id, 'feedback', feedback_id))

    def update(self, campaign_id, feedback_id):
        return self._mc_client._patch(url=self._build_path(campaign_id, 'feedback', feedback_id))

    def create(self, campaign_id, data):
        return self._mc_client._post(url=self._build_path(campaign_id, 'feedback'), data=data)
