# coding=utf-8
"""
The Lists API endpoint

Documentation: http://developer.mailchimp.com/documentation/mailchimp/reference/lists/
Schema: https://api.mailchimp.com/schema/3.0/Lists/Instance.json
"""
from __future__ import unicode_literals

from mailchimp3.baseapi import BaseApi
from mailchimp3.entities.listabusereport import ListAbuseReport
from mailchimp3.entities.listactivity import ListActivity
from mailchimp3.entities.listclient import ListClient
from mailchimp3.entities.listgrowthhistory import ListGrowthHistory
from mailchimp3.entities.listinterestcategory import ListInterestCategory
from mailchimp3.entities.listmember import ListMember
from mailchimp3.entities.listmergefield import ListMergeField
from mailchimp3.entities.listsegment import ListSegment
from mailchimp3.entities.listtwitter import ListTwitter
from mailchimp3.entities.listwebhook import ListWebhook


class List(BaseApi):
    """
    A MailChimp list is a powerful and flexible tool that helps you manage your contacts.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(List, self).__init__(*args, **kwargs)
        self.endpoint = 'lists'
        self.list_id = None
        self.abusereport = ListAbuseReport(self)
        self.activity = ListActivity(self)
        self.client = ListClient(self)
        self.growthhistory = ListGrowthHistory(self)
        self.interestcategory = ListInterestCategory(self)
        self.member = ListMember(self)
        self.mergefield = ListMergeField(self)
        self.segment = ListSegment(self)
        self.twitter = ListTwitter(self)
        self.webhook = ListWebhook(self)


    def create(self, data):
        """
        Create a new list in your MailChimp account.

        :param data: The request body parameters
        :type data: :py:class:`dict`
        """
        response = self._mc_client._post(url=self._build_path(), data=data)
        self.list_id = response['id']
        return response


    def all(self, get_all=False, **queryparams):
        """
        Get information about all lists in the account.

        :param get_all: Should the query get all results
        :type get_all: :py:class:`bool`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        queryparams['count'] = integer
        queryparams['offset'] = integer
        queryparams['before_date_created'] = string
        queryparams['since_date_created'] = string
        queryparams['before_campaign_last_sent'] = string
        queryparams['since_campaign_last_sent'] = string
        queryparams['email'] = string
        """
        if get_all:
            return self._iterate(url=self._build_path(), **queryparams)
        else:
            return self._mc_client._get(url=self._build_path(), **queryparams)


    def get(self, list_id, **queryparams):
        """
        Get information about a specific list in your MailChimp account.
        Results include list members who have signed up but haven’t confirmed
        their subscription yet and unsubscribed or cleaned.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        """
        self.list_id = list_id
        return self._mc_client._get(url=self._build_path(list_id), **queryparams)


    def update(self, list_id, data):
        """
        Update the settings for a specific list.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:class:`dict`
        """
        self.list_id = list_id
        return self._mc_client._patch(url=self._build_path(list_id), data=data)


    def delete(self, list_id):
        """
        Delete a list from your MailChimp account. If you delete a list,
        you’ll lose the list history—including subscriber activity,
        unsubscribes, complaints, and bounces. You’ll also lose subscribers’
        email addresses, unless you exported and backed up your list.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        """
        self.list_id = list_id
        return self._mc_client._delete(url=self._build_path(list_id))

