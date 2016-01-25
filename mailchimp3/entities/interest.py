from ..baseapi import BaseApi


class Interest(BaseApi):

    def __init__(self, *args, **kwargs):
        super(Interest, self).__init__(*args, **kwargs)
        self.endpoint = 'lists'

    def all(self, list_id, category_id):
        """
        returns the first 10 interests for the category.
        """
        return self._mc_client._get(url=self._build_path(list_id, 'interest-categories', category_id, 'interests'))

    def create(self, list_id, category_id, data):
        """
        creates a new interest, or  Group Name.
        """
        return self._mc_client._post(
            url=self._build_path(list_id, 'interest-categories', category_id, 'interests'), data=data)

    def get(self, list_id, category_id, interest_id):
        """
        returns information about a specific interest category, or Group Title.
        """
        return self._mc_client._get(
            url=self._build_path(list_id, 'interest-categories', category_id, 'interests', interest_id))

    def update(self, list_id, category_id, interest_id, data):
        """
        returns information about a specific interest category, or Group Title.
        """
        return self._mc_client._patch(
            url=self._build_path(list_id, 'interest-categories', category_id, 'interests', interest_id),
            data=data)

    def delete(self, list_id, category_id, interest_id):
        """
        returns information about a specific interest category, or Group Title.
        """
        return self._mc_client._delete(
            url=self._build_path(list_id, 'interest-categories', category_id, 'interests', interest_id))
