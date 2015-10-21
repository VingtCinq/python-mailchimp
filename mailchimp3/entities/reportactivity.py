from baseapi import BaseApi


class ReportActivity(BaseApi):

    def __init__(self, *args, **kwargs):
        super(ReportActivity, self).__init__(*args, **kwargs)
        self.endpoint = 'reports'

    def all(self, list_id):
        """
        returns a list of member's subscriber activity in a specific campaign
        """
        return self._mc_client._get(url=self._build_path(list_id, 'email-activity'))
