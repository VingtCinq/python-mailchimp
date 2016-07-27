from __future__ import unicode_literals
from ..baseapi import BaseApi


class Goal(BaseApi):

    def __init__(self, *args, **kwargs):
        super(Goal, self).__init__(*args, **kwargs)
        self.endpoint = 'lists'

    def all(self, list_id, email_id, **queryparams):
        """
        returns the last 50 Goal events for a subscriber on a specific list.
        """
        return self._mc_client._get(url=self._build_path(list_id, 'members', email_id, 'goals'), **queryparams)
