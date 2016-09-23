# coding=utf-8
"""
The List Twitter Leade Generation Cards API endpoint

Documentation: http://developer.mailchimp.com/documentation/mailchimp/reference/lists/twitter-lead-gen-cards/
Schema: https://api.mailchimp.com/schema/3.0/Lists/TwitterLeadGenCards/Instance.json
"""
from __future__ import unicode_literals

from mailchimp3.baseapi import BaseApi


class ListTwitter(BaseApi):
    """
    Manage Twitter Lead Generation Cards for a specific MailChimp list.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(ListTwitter, self).__init__(*args, **kwargs)
        self.endpoint = 'lists'
        self.list_id = None
        self.twitter_card_id = None


    def create(self, list_id, data):
        """
        Create a new Twitter Lead Generation Card for a specific list.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:class:`dict`
        """
        self.list_id = list_id
        response = self._mc_client._post(url=self._build_path(list_id, 'twitter-lead-gen-cards'), data=data)
        self.twitter_card_id = response['id']
        return response


    def all(self, list_id):
        """
        Get information about all Twitter Lead Generation Cards for a specific list.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        """
        self.list_id = list_id
        self.twitter_card_id = None
        return self._mc_client._get(url=self._build_path(list_id, 'twitter-lead-gen-cards'))


    def get(self, list_id, twitter_card_id):
        """
        Get information about a specific Twitter Lead Generation Card.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param twitter_card_id: The Twitter Lead Generation Card ID.
        :type twitter_card_id: :py:class:`str`
        """
        self.list_id = list_id
        self.twitter_card_id = twitter_card_id
        return self._mc_client._get(url=self._build_path(list_id, 'twitter-lead-gen-cards', twitter_card_id))
