from ..baseapi import BaseApi


class ReportActivity(BaseApi):

    """
    Reports Email Activity
    http://kb.mailchimp.com/api/resources/reports/emailactivity/reports-email-activity-collection
    http://kb.mailchimp.com/api/resources/reports/emailactivity/reports-email-activity-instance
    """

    def __init__(self, *args, **kwargs):
        super(ReportActivity, self).__init__(*args, **kwargs)
        self.endpoint = 'reports'

    def all(self, list_id):
        """
        Returns a list of subscriber activity in a specific campaign.
        """
        return self._mc_client._get(url=self._build_path(list_id, 'email-activity'))

    def get(self, list_id, email_id):
        """
        returns a list of a member's subscriber activity in a specific campaign.
        """
        return self._mc_client._get(url=self._build_path(list_id, 'email-activity', email_id))
