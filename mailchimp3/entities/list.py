from ..baseapi import BaseApi


class List(BaseApi):

    def __init__(self, *args, **kwargs):
        super(List, self).__init__(*args, **kwargs)
        self.endpoint = 'lists'
        self.list_id = None

    def all(self):
        """
        returns list of subscriber lists in the account.
        """
        return self._mc_client._get(url=self.endpoint)

    def get(self, list_id):
        """
        returns information about a specific list.
        """
        self.list_id = list_id
        return self._mc_client._get(url=self._build_path(list_id))

    def update(self, list_id, data):
        """
        updates an existing list's settings.
        """
        self.list_id = list_id
        return self._mc_client._patch(url=self._build_path(list_id), data=data)

    def delete(self, list_id):
        """
        removes the list and its members from the account.
        """
        self.list_id = list_id
        return self._mc_client._delete(url=self._build_path(list_id))

    def create(self, data):
        """
        creates a new list.
        """
        return self._mc_client._post(url=self.endpoint, data=data)