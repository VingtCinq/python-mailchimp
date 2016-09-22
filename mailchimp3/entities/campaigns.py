# coding=utf-8
"""
The Campaigns API endpoint

Documentation: http://developer.mailchimp.com/documentation/mailchimp/reference/campaigns/
Schema: https://api.mailchimp.com/schema/3.0/Campaigns/Instance.json
"""
from __future__ import unicode_literals

from mailchimp3.baseapi import BaseApi
from mailchimp3.entities.campaignaction import CampaignAction
from mailchimp3.entities.campaigncontent import CampaignContent
from mailchimp3.entities.campaignfeedback import CampaignFeedback
from mailchimp3.entities.campaignsendchecklist import CampaignSendChecklist


class Campaign(BaseApi):
    """
    Campaigns are how you send emails to your MailChimp list. Use the
    Campaigns API calls to manage campaigns in your MailChimp account.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(Campaign, self).__init__(*args, **kwargs)
        self.endpoint = 'campaigns'
        self.campaign_id = None
        self.action = CampaignAction(self)
        self.content = CampaignContent(self)
        self.feedback = CampaignFeedback(self)
        self.sendchecklist = CampaignSendChecklist(self)


    def create(self, data):
        """
        Create a new MailChimp campaign.

        :param data: The request body parameters
        :type data: :py:class:`dict`
        """
        response = self._mc_client._post(url=self._build_path(), data=data)
        self.campaign_id = response['id']
        return response


    def all(self, get_all=False, **queryparams):
        """
        Get all campaigns in an account.

        :param get_all: Should the query get all results
        :type get_all: :py:class:`bool`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        queryparams['count'] = integer
        queryparams['offset'] = integer
        queryparams['type'] = []
        queryparams['status'] = []
        queryparams['before_send_time'] = string
        queryparams['since_send_time'] = string
        queryparams['before_create_time'] = string
        queryparams['since_create_time'] = string
        queryparams['list_id'] = string
        """
        self.campaign_id = None
        if get_all:
            return self._iterate(url=self._build_path(), **queryparams)
        else:
            return self._mc_client._get(url=self._build_path(), **queryparams)


    def get(self, campaign_id, **queryparams):
        """
        Get information about a specific campaign.

        :param campaign_id: The unique id for the campaign.
        :type campaign_id: :py:class:`str`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        """
        self.campaign_id = campaign_id
        return self._mc_client._get(url=self._build_path(campaign_id), **queryparams)


    def update(self, campaign_id, data):
        """
        Update some or all of the settings for a specific campaign.

        :param campaign_id: The unique id for the campaign.
        :type campaign_id: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:class:`dict`
        """
        self.campaign_id = campaign_id
        return self._mc_client._patch(url=self._build_path(campaign_id), data=data)


    def delete(self, campaign_id):
        """
        Remove a campaign from your MailChimp account.

        :param campaign_id: The unique id for the campaign.
        :type campaign_id: :py:class:`str`
        """
        self.campaign_id = campaign_id
        return self._mc_client._delete(url=self._build_path(campaign_id))
