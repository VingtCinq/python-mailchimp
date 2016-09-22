# coding=utf-8
"""
The Campaigns API endpoint

Documentation: http://developer.mailchimp.com/documentation/mailchimp/reference/campaigns/
Schema: https://api.mailchimp.com/schema/3.0/Campaigns/Instance.json
"""
from __future__ import unicode_literals

from mailchimp3.baseapi import BaseApi
from mailchimp3.entities.campaignactions import CampaignActions
from mailchimp3.entities.campaigncontent import CampaignContent
from mailchimp3.entities.campaignfeedback import CampaignFeedback
from mailchimp3.entities.campaignsendchecklist import CampaignSendChecklist
from mailchimp3.helpers import check_email


class Campaigns(BaseApi):
    """
    Campaigns are how you send emails to your MailChimp list. Use the
    Campaigns API calls to manage campaigns in your MailChimp account.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(Campaigns, self).__init__(*args, **kwargs)
        self.endpoint = 'campaigns'
        self.campaign_id = None
        self.actions = CampaignActions(self)
        self.content = CampaignContent(self)
        self.feedback = CampaignFeedback(self)
        self.sendchecklist = CampaignSendChecklist(self)


    def create(self, data):
        """
        Create a new MailChimp campaign.

        The ValueError raised by an invalid type in the data does not mention
        'absplit' as a potential value because the documentation indicates
        that the absplit type has been deprecated.

        :param data: The request body parameters
        :type data: :py:class:`dict`
        data = {
            "recipients": object*
            {
                "list_id": string*
            },
            "settings": object*
            {
                "subject_line": string*,
                "from_name": string*,
                "reply_to": string*
            },
            "variate_settings": object* (Required if type is "variate")
            {
                "winner_criteria": string* (Must be one of "opens", "clicks", "total_revenue", or "manual")
            },
            "rss_opts": object* (Required if type is "rss")
            {
                "feed_url": string*,
                "frequency": string* (Must be one of "daily", "weekly", or "monthly")
            },
            "type": string* (Must be one of "regular", "plaintext", "rss", "variate", or "absplit")
        }
        """
        for recipient in data['recipients']:
            if not recipient['list_id']:
                raise ValueError('You must provide a list_id for each recipient')
        if not data['settings']['subject_line']:
            raise ValueError('You must include a subject_line in your settings')
        if not data['settings']['from_name']:
            raise ValueError('You must include a from_name in your settings')
        if not data['settings']['reply_to']:
            raise ValueError('You must include a reply_to address in your settings')
        check_email(data['settings']['reply_to'])
        if not data['type'] in ['regular', 'plaintext', 'rss', 'variate', 'abspilt']:
            raise ValueError('Your type must be one of "regular", "plaintext", "rss", or "variate"')
        if data['type'] == 'variate':
            if data['variate_settings']['winner_criteria'] not in ['opens', 'clicks', 'total_revenue', 'manual']:
                raise ValueError('The winner_criteria must be one of "opens", "clicks", "total_revenue", or "manual"')
        if data['type'] == 'rss':
            if not data['rss_opts']['feed_url']:
                raise ValueError('You must provide the url of the RSS feed in feed_url in your rss_opts')
            if not data['rss_opts']['frequency'] in ['daily', 'weekly', 'monthly']:
                raise ValueError('Your rss_opts frequency must be one of "daily", "weekly", or "monthly"')
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
        queryparams['folder_id'] = string
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

        The type value for updating a campaign is not listed as one of the
        request body parameters, but it is listed as not read only in the
        output listed from the endpoint.

        No error checking for request body parameters as whether they are
        required or not is not clear from the documentation.

        :param campaign_id: The unique id for the campaign.
        :type campaign_id: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:class:`dict`
        data = {
            "recipients": object*
            {
                "list_id": string*
            },
            "settings": object*
            {
                "subject_line": string*,
                "from_name": string*,
                "reply_to": string*
            },
            "variate_settings": object* (Required if type is "variate")
            {
                "winner_criteria": string* (Must be one of "opens", "clicks", "total_revenue", or "manual")
            },
            "rss_opts": object* (Required if type is "rss")
            {
                "feed_url": string*,
                "frequency": string* (Must be one of "daily", "weekly", or "monthly")
            },
            "type": string* (Must be one of "regular", "plaintext", "rss", "variate", or "absplit")
        }
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
