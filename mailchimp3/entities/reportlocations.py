# coding=utf-8
"""
The Location Report API endpoint

Documentation: http://developer.mailchimp.com/documentation/mailchimp/reference/reports/locations/
Schema: https://api.mailchimp.com/schema/3.0/Reports/Locations/Collection.json
"""
from __future__ import unicode_literals

from mailchimp3.baseapi import BaseApi


class ReportLocations(BaseApi):
    """
    Get top open locations for a specific campaign.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(ReportLocations, self).__init__(*args, **kwargs)
        self.endpoint = 'reports'
        self.campaign_id = None


    def all(self, campaign_id, **queryparams):
        """
        Get top open locations for a specific campaign.

        :param campaign_id: The unique id for the campaign.
        :type campaign_id: :py:class:`str`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        """
        self.campaign_id = campaign_id
        return self._mc_client._get(url=self._build_path(campaign_id, 'locations'), **queryparams)
