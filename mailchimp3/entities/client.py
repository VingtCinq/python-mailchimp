from ..baseapi import BaseApi


class Client(BaseApi):

    def __init__(self, *args, **kwargs):
        super(Client, self).__init__(*args, **kwargs)
        self.endpoint = 'lists'

    def all(self, list_id):
        """
        returns top 10 email clients based on subscriber count.
        """
        return self._mc_client._get(url=self._build_path(list_id, 'clients'))
