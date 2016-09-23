# coding=utf-8
"""
The List Segment Members API endpoint

Documentation: http://developer.mailchimp.com/documentation/mailchimp/reference/lists/segments/members/
Schema: https://api.mailchimp.com/schema/3.0/Lists/Members/Instance.json
"""
from __future__ import unicode_literals

from mailchimp3.baseapi import BaseApi


class ListSegmentMember(BaseApi):
    """
    Manage list members in a saved segment.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(ListSegmentMember, self).__init__(*args, **kwargs)
        self.endpoint = 'lists'
        self.list_id = None
        self.segment_id = None
        self.subscriber_hash = None


    def create(self, list_id, segment_id, data):
        """
        Add a member to a static segment.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param segment_id: The unique id for the segment.
        :type segment_id: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:class:`dict`
        """
        self.list_id = list_id
        self.segment_id = segment_id
        response = self._mc_client._post(url=self._build_path(list_id, 'segments', segment_id, 'members'), data=data)
        self.subscriber_hash = response['id']
        return response


    def all(self, list_id, segment_id, get_all=False, **queryparams):
        """
        Get information about members in a saved segment.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param segment_id: The unique id for the segment.
        :type segment_id: :py:class:`str`
        :param get_all: Should the query get all results
        :type get_all: :py:class:`bool`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        queryparams['count'] = integer
        queryparams['offset'] = integer
        """
        self.list_id = list_id
        self.segment_id = segment_id
        self.subscriber_hash = None
        if get_all:
            return self._iterate(url=self._build_path(list_id, 'segments', segment_id, 'members'), **queryparams)
        else:
            return self._mc_client._get(url=self._build_path(list_id, 'segments', segment_id, 'members'), **queryparams)


    def delete(self, list_id, segment_id, subscriber_hash):
        """
        Remove a member from the specified static segment.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param segment_id: The unique id for the segment.
        :type segment_id: :py:class:`str`
        :param subscriber_hash: The MD5 hash of the lowercase version of the
          list member’s email address.
        :type subscriber_hash: :py:class:`str`
        """
        self.list_id = list_id
        self.segment_id = segment_id
        self.subscriber_hash = subscriber_hash
        return self._mc_client._delete(
            url=self._build_path(list_id, 'segments', segment_id, 'members', subscriber_hash)
        )
