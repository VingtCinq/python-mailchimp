from ..baseapi import BaseApi


class Category(BaseApi):

    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)
        self.endpoint = 'lists'

    def all(self, list_id):
        """
        returns first 10 interest categories, or Group Titles, for a list.
        """
        return self._mc_client._get(url=self._build_path(list_id, 'interest-categories'))

    def create(self, list_id, data):
        """
        creates a new interest categories, or Group Title.
        """
        return self._mc_client._post(url=self._build_path(list_id, 'interest-categories'), data=data)

    def get(self, list_id, category_id):
        """
        returns information about a specific interest category, or Group Title.
        """
        return self._mc_client._get(url=self._build_path(list_id, 'interest-categories', category_id))
