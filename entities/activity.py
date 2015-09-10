from baseapi import BaseApi


class Activity(BaseApi):

    def __init__(self, *args, **kwargs):
        super(Activity, self).__init__(*args, **kwargs)
        self.endpoint = 'lists'

    def all(self, list_id):
        """
        returns up to 180 days of list activity.
        """
        return self._mc_client._get(url=self._build_path(list_id, 'activity'))
