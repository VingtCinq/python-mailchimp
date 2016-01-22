from ..baseapi import BaseApi


class Report(BaseApi):

    def __init__(self, *args, **kwargs):
        super(Report, self).__init__(*args, **kwargs)
        self.endpoint = 'reports'

    def all(self, **kwargs):
        """
        Returns a list of reports.
        """
        return self._mc_client._get(url=self.endpoint, **kwargs)

    def get(self, report_id):
        """
        Returns a report for a specific campaign.
        """
        return self._mc_client._get(url=self._build_path(report_id))
