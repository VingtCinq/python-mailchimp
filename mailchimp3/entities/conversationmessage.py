# coding=utf-8
"""
The Conversation Messages API endpoint

Note: This is a paid feature

Documentation: http://developer.mailchimp.com/documentation/mailchimp/reference/conversations/messages/
Schema: https://api.mailchimp.com/schema/3.0/Conversations/Messages/Instance.json
"""
from __future__ import unicode_literals

from mailchimp3.baseapi import BaseApi


class ConversationMessage(BaseApi):
    """
    Manage messages in a specific campaign conversation.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(ConversationMessage, self).__init__(*args, **kwargs)
        self.endpoint = 'conversations'
        self.conversation_id = None
        self.message_id = None


    # Paid feature
    def create(self, conversation_id, data):
        """
        Post a new message to a conversation.

        :param conversation_id: The unique id for the conversation.
        :type conversation_id: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:class:`dict`
        """
        self.conversation_id = conversation_id
        response =  self._mc_client._post(url=self._build_path(conversation_id, 'messages'), data=data)
        self.message_id = response['id']
        return response


    # Paid feature
    def all(self, conversation_id, **queryparams):
        """
        Get messages from a specific conversation.

        :param conversation_id: The unique id for the conversation.
        :type conversation_id: :py:class:`str`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = p[
        queryparams['is_read'] = string
        queryparams['before_timestamp'] = string
        queryparams['since_timestamp'] = string
        """
        self.conversation_id = conversation_id
        self.message_id = None
        return self._mc_client._get(url=self._build_path(conversation_id, 'messages'), **queryparams)


    # Paid feature
    def get(self, conversation_id, message_id, **queryparams):
        """
        Get an individual message in a conversation.

        :param conversation_id: The unique id for the conversation.
        :type conversation_id: :py:class:`str`
        :param message_id: The unique id for the conversation message.
        :type message_id: :py:class:`str`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        """
        self.conversation_id = conversation_id
        self.message_id = message_id
        return self._mc_client._get(url=self._build_path(conversation_id, 'messages', message_id), **queryparams)
