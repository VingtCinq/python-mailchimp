# coding=utf-8
"""
The List Twitter Leade Generation Cards API endpoint

Documentation: http://developer.mailchimp.com/documentation/mailchimp/reference/lists/twitter-lead-gen-cards/
Schema: https://api.mailchimp.com/schema/3.0/Lists/TwitterLeadGenCards/Instance.json
"""
from __future__ import unicode_literals

from mailchimp3.baseapi import BaseApi
from mailchimp3.helpers import check_url


class ListTwitterLeadGenerationCards(BaseApi):
    """
    Manage Twitter Lead Generation Cards for a specific MailChimp list.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(ListTwitterLeadGenerationCards, self).__init__(*args, **kwargs)
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
        data = {
            "name": string*,
            "title": string*,
            "cta_text": string*,
            "privacy_policy_url": string*,
            "image_url": string*,
            "twitter_account_id": string*
        }
        """
        self.list_id = list_id
        if 'name' not in data:
            raise KeyError('The twitter lead generation card must have a name')
        if 'title' not in data:
            raise KeyError('The twitter lead generation card must have a title')
        if 'cta_text' not in data:
            raise KeyError('The twitter lead generation card must have a cta_text')
        if len(data['cta_text']) > 20:
            raise ValueError('The twitter lead generation card cta_text must be 20 characters or less')
        if 'privacy_policy_url' not in data:
            raise KeyError('The twitter lead generation card must have a privacy_policy_url')
        check_url(data['privacy_policy_url'])
        if 'image_url' not in data:
            raise KeyError('The twitter lead generation card must have a image_url')
        check_url(data['image_url'])
        if 'twitter_account_id' not in data:
            raise KeyError('The twitter lead generation card must have a twitter_account_id')
        response = self._mc_client._post(url=self._build_path(list_id, 'twitter-lead-gen-cards'), data=data)
        if response is not None:
            self.twitter_card_id = response['id']
        else:
            self.twitter_card_id = None
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
