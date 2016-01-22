from ..baseapi import BaseApi


class Message(BaseApi):

    def __init__(self, *args, **kwargs):
        super(Message, self).__init__(*args, **kwargs)
        self.endpoint = 'conversations'

    def all(self, conversation_id):
        return self._mc_client._get(url=self._build_path(conversation_id, 'messages'))

    def get(self, conversation_id, message_id):
        return self._mc_client._get(url=self._build_path(conversation_id, 'messages', message_id))

    def create(self, conversation_id, data):
        return self._mc_client._post(url=self._build_path(conversation_id, 'messages'), data=data)
