from __future__ import unicode_literals
from ..baseapi import BaseApi


class Conversation(BaseApi):

    def __init__(self, *args, **kwargs):
        super(Conversation, self).__init__(*args, **kwargs)
        self.endpoint = 'conversations'

    def all(self, **queryparams):
        return self._mc_client._get(url=self.endpoint, **queryparams)

    def get(self, conversation_id):
        return self._mc_client._get(url=self._build_path(conversation_id))
