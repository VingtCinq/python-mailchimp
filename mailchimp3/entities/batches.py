from __future__ import unicode_literals

import json
from ..baseapi import BaseApi
from ..helpers import HTTP_METHOD_ACTION_MATCHING


class Batches(BaseApi):
    """
    Implements mailchimp batch operations
    """
    def __init__(self, *args, **kwargs):
        super(Batches, self).__init__(*args, **kwargs)
        self.endpoint = 'batches'
        self.operation_status = None
        self.batch_id = None

    def post(self, data):

        return self._mc_client._post(url=self._build_path(), data=data)

    def get(self, batch_id):
        """
        Gets batch status by its id
        """
        self.batch_id = batch_id

        return self._mc_client._get(url=self._build_path(batch_id))

    @staticmethod
    def _prepare_params(operations_list):
        """
        Prepares data to be sent to the API

        :param operations_list: list of dictionaries
        {
            'action': 'create_or_update',
            'mailchimp_entity': instance of mailchimp entity, e.g. self.mailchimp.batches,
            'entity_params': list or tuple of params for building path e.g. ('lists', list_id, 'members', member_id),
            'data': {'email_address': subscriber_email,
                     'status_if_new': 'subscribed',
                     'merge_fields': {'ID': subscriber_id,
                                      'FNAME': subscriber_fname}
                     }
            }
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
        """
        data = self._prepare_params(operations_list)
        self.operation_status = self.post(data=data)

        return self.operation_status
