# coding=utf-8
"""
The Batch Operations API Endpoint

Documentation: http://developer.mailchimp.com/documentation/mailchimp/reference/batches/
Schema: https://api.mailchimp.com/schema/3.0/Batches/Instance.json
"""
from __future__ import unicode_literals

import json
from mailchimp3.baseapi import BaseApi
from mailchimp3.helpers import HTTP_METHOD_ACTION_MATCHING


class Batch(BaseApi):
    """
    Implements mailchimp batch operations: Use batch operations to complete multiple operations with a single call.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(Batch, self).__init__(*args, **kwargs)
        self.endpoint = 'batches'
        self.batch_id = None
        self.operation_status = None


    def create(self, data):
        """
        Begin processing a batch operations request.

        :param data: The request body parameters
        :type data: :py:class:`dict`
        """
        return self._mc_client._post(url=self._build_path(), data=data)


    def all(self, get_all=False, **queryparams):
        """
        Get a summary of batch requests that have been made.

        :param get_all: Should the query get all results
        :type get_all: :py:class:`bool`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        queryparams['count'] = integer
        queryparams['offset'] = integer
        """
        self.batch_id = None
        self.operation_status = None
        if get_all:
            return self._iterate(url=self._build_path(), **queryparams)
        else:
            return self._mc_client._get(url=self._build_path(), **queryparams)


    def get(self, batch_id, **queryparams):
        """
        Get the status of a batch request.

        :param batch_id: The unique id for the batch operation.
        :type batch_id: :py:class:`str`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        """
        self.batch_id = batch_id
        self.operation_status = None
        return self._mc_client._get(url=self._build_path(batch_id), **queryparams)


    def delete(self, batch_id):
        """
        Stops a batch request from running. Since only one batch request is
        run at a time, this can be used to cancel a long running request. The
        results of any completed operations will not be available after this
        call.

        :param batch_id: The unique id for the batch operation.
        :type batch_id: :py:class:`str`
        """
        self.batch_id = batch_id
        self.operation_status = None
        return self._mc_client._delete(url=self._build_path(batch_id))

    @staticmethod
    def _prepare_params(operations_list):
        """
        Prepares data to be sent to the API

        :param operations_list: list of dictionaries
        :type operations_list: :py:class:`list`
        operations_list = [{
            'action': 'create_or_update',
            'mailchimp_entity': instance of mailchimp entity, e.g. self.mailchimp.batches,
            'entity_params': list or tuple of params for building path e.g. ('lists', list_id, 'members', member_id),
            'data': {
                'email_address': subscriber_email,
                'status_if_new': 'subscribed',
                'merge_fields': {
                    'ID': subscriber_id,
                    'FNAME': subscriber_fname
                }
            }
        }]
        :returns: The prepared dict for use with the create command
        :rtype: :py:class:`dict`
        """
        operations = []
        for operation in operations_list:
            operations.append({
                'method': HTTP_METHOD_ACTION_MATCHING.get(operation.get('action', 'PUT')),
                'path': "/".join(operation['entity_params']),
                'body': '{}'.format(json.dumps(operation.get('data')))
            })

        return {
            'operations': operations
        }

    def execute(self, operations_list):
        """
        Executes batch operation and set its status

        :param operations_list: The list of operations to batch
        :type operations_list: :py:class:`list`
        operations_list = [{
            'action': 'create_or_update',
            'mailchimp_entity': instance of mailchimp entity, e.g. self.mailchimp.batches,
            'entity_params': list or tuple of params for building path e.g. ('lists', list_id, 'members', member_id),
            'data': {
                'email_address': subscriber_email,
                'status_if_new': 'subscribed',
                'merge_fields': {
                    'ID': subscriber_id,
                    'FNAME': subscriber_fname
                }
            }
        }]
        :returns: The operation status
        :rtype: :py:class:`int`
        """
        self.batch_id = None
        data = self._prepare_params(operations_list)
        self.operation_status = self.post(data=data)
        return self.operation_status
