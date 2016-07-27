from __future__ import unicode_literals
from ..baseapi import BaseApi


class ReportUnsubscribed(BaseApi):

    """
    Reports Unsubscribed Collection
        A list of unsubscribes for a specific campaign (for various reasons).
        http://developer.mailchimp.com/documentation/mailchimp/http://kb.mailchimp.com/api/resources/reports/unsubscribes
    """

    def __init__(self, *args, **kwargs):
        super(ReportUnsubscribed, self).__init__(*args, **kwargs)
        self.endpoint = 'reports'

    def all(self, campaign_id, **queryparams):
        """
        Returns report of all usubscribes a reason for a given campaign
        """
        return self._mc_client._get(url=self._build_path(campaign_id, 'unsubscribed'), **queryparams)

    def get(self, campaign_id, subscriber_hash):
        """
        Returns ususubscribe report for a spefic member (given the capaign_id and the md5 hash of the member email)
        """
        return self._mc_client._get(url=self._build_path(campaign_id, 'unsubscribed', subscriber_hash))
