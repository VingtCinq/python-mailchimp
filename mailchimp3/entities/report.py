from baseapi import BaseApi
from feedback import Feedback


class Report(BaseApi):

    def __init__(self, *args, **kwargs):
        super(Report, self).__init__(*args, **kwargs)
        self.endpoint = 'reports'
        self.report_id = None

    def all(self):
        return self._mc_client._get(url=self.endpoint)

    def get(self, report_id):
        self.report_id = report_id
        return self._mc_client._get(url=self._build_path(report_id))

    def delete(self, report_id):
        return self._mc_client._delete(url=self._build_path(report_id))

