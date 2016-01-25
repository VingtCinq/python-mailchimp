from ..baseapi import BaseApi


class ReportAbuse(BaseApi):

    """
    Reports Abuse Collection
        A list of abuse complaints for a specific campaign.
        http://kb.mailchimp.com/api/resources/reports/abuse/reports-abuse-collection
    Reports Abuse Instance
        A specific abuse report associated with a specific campaign.
        http://kb.mailchimp.com/api/resources/reports/abuse/reports-abuse-instance
    """

    def __init__(self, *args, **kwargs):
        super(ReportAbuse, self).__init__(*args, **kwargs)
        self.endpoint = 'reports'

    def all(self, campaign_id):
        """
        Returns the last 10 abuse reports by date.
        """
        return self._mc_client._get(url=self._build_path(campaign_id, 'abuse-report'))

    def get(self, campaign_id, abuse_id):
        """
        Returns an individual abuse report.
        """
        return self._mc_client._get(url=self._build_path(campaign_id, 'abuse-report', abuse_id))
