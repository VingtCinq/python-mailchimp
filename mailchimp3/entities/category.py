from __future__ import unicode_literals
from ..baseapi import BaseApi


class Category(BaseApi):

    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)
        self.endpoint = 'lists'

    def all(self, list_id, **queryparams):
        """
        returns first 10 interest categories, or Group Titles, for a list.
        """
        return self._mc_client._get(url=self._build_path(list_id, 'interest-categories'), **queryparams)

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

    def update(self, list_id, category_id, data):
        """
        updates an existing interest category, or Group Title.
        """
        return self._mc_client._patch(url=self._build_path(list_id, 'interest-categories', category_id), data=data)

    def delete(self, list_id, category_id):
        """
        removes an existing interest category, or Group Title. from the list. This cannot be undone.
        """
        return self._mc_client._delete(url=self._build_path(list_id, 'interest-categories', category_id))
