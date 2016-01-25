from ..baseapi import BaseApi


class ListAbuse(BaseApi):

    def __init__(self, *args, **kwargs):
        super(ListAbuse, self).__init__(*args, **kwargs)
        self.endpoint = 'lists'

    def all(self, list_id):
        """
        returns list of abuse complaints for a specific list.
        """
        return self._mc_client._get(url=self._build_path(list_id, 'abuse-report'))

    def get(self, list_id, abuse_id):
        """
        returns an individual abuse report.
        """
        return self._mc_client._get(url=self._build_path(list_id, 'abuse-report', abuse_id))
