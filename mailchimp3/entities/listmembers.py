# coding=utf-8
"""
The List Members API endpoint

Documentation: http://developer.mailchimp.com/documentation/mailchimp/reference/lists/members/
Schema: https://api.mailchimp.com/schema/3.0/Lists/Members/Instance.json
"""
from __future__ import unicode_literals

from mailchimp3.baseapi import BaseApi
from mailchimp3.entities.listmemberactivity import ListMemberActivity
from mailchimp3.entities.listmembergoal import ListMemberGoal
from mailchimp3.entities.listmembernote import ListMemberNote


class ListMember(BaseApi):
    """
    Manage members of a specific MailChimp list, including currently
    subscribed, unsubscribed, and bounced members.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(ListMember, self).__init__(*args, **kwargs)
        self.endpoint = 'lists'
        self.list_id = None
        self.subscriber_hash = None
        self.activity = ListMemberActivity(self)
        self.goal = ListMemberGoal(self)
        self.note = ListMemberNote(self)


    def create(self, list_id, data):
        """
        Add a new member to the list.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:class:`dict`
        """
        self.list_id = list_id
        response = self._mc_client._post(url=self._build_path(list_id, 'members'), data=data)
        self.subscriber_hash = response['id']
        return response


    def all(self, list_id, get_all=False, **queryparams):
        """
        Get information about members in a specific MailChimp list.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param get_all: Should the query get all results
        :type get_all: :py:class:`bool`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        queryparams['count'] = integer
        queryparams['offset'] = integer
        queryparams['email_type'] = string
        queryparams['status'] = string
        queryparams['before_timestamp_opt'] = string
        queryparams['since_timestamp_opt'] = string
        queryparams['before_last_changed'] = string
        queryparams['since_last_changed'] = string
        queryparams['unique_email_id'] = string
        queryparams['vip_only'] = boolean
        """
        self.list_id = list_id
        self.subscriber_hash = None
        if get_all:
            return self._iterate(url=self._build_path(list_id, 'members'), **queryparams)
        else:
            return self._mc_client._get(url=self._build_path(list_id, 'members'), **queryparams)


    def get(self, list_id, subscriber_hash, **queryparams):
        """
        Get information about a specific list member, including a currently
        subscribed, unsubscribed, or bounced member.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param subscriber_hash: The MD5 hash of the lowercase version of the
          list member’s email address.
        :type subscriber_hash: :py:class:`str`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        """
        self.list_id = list_id
        self.subscriber_hash = subscriber_hash
        return self._mc_client._get(url=self._build_path(list_id, 'members', subscriber_hash), **queryparams)


    def update(self, list_id, subscriber_hash, data):
        """
        Update information for a specific list member.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param subscriber_hash: The MD5 hash of the lowercase version of the
          list member’s email address.
        :type subscriber_hash: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:class:`dict`
        """
        self.list_id = list_id
        self.subscriber_hash = subscriber_hash
        return self._mc_client._patch(url=self._build_path(list_id, 'members', subscriber_hash), data=data)


    def create_or_update(self, list_id, subscriber_hash, data):
        """
        Add or update a list member.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param subscriber_hash: The MD5 hash of the lowercase version of the
          list member’s email address.
        :type subscriber_hash: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:class:`dict`
        """
        self.list_id = list_id
        self.subscriber_hash = subscriber_hash
        return self._mc_client._put(url=self._build_path(list_id, 'members', subscriber_hash), data=data)


    def delete(self, list_id, subscriber_hash):
        """
        Delete a member from a list.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param subscriber_hash: The MD5 hash of the lowercase version of the
          list member’s email address.
        :type subscriber_hash: :py:class:`str`
        """
        self.list_id = list_id
        self.subscriber_hash = subscriber_hash
        return self._mc_client._delete(url=self._build_path(list_id, 'members', subscriber_hash))
