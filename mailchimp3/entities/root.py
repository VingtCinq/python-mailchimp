from ..baseapi import BaseApi
from .feedback import Feedback


class Root(BaseApi):

    def __init__(self, *args, **kwargs):
        super(Root, self).__init__(*args, **kwargs)
        self.endpoint = ''

    def get(self):
    	# TODO: Add query parameters
        return self._mc_client._get(url=self._build_path())
