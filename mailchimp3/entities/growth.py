from ..baseapi import BaseApi


class Growth(BaseApi):

    def __init__(self, *args, **kwargs):
        super(Growth, self).__init__(*args, **kwargs)
        self.endpoint = 'lists'

    def all(self, list_id):
        """
        returns 10 months worth of growth history.
        """
        return self._mc_client._get(url=self._build_path(list_id, 'growth-history'))

    def get(self, list_id, month):
        """
        returns a specific list's growth report for the specified month.
        """
        return self._mc_client._get(url=self._build_path(list_id, 'growth-history', month))
