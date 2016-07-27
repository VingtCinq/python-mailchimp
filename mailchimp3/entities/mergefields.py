from __future__ import unicode_literals
from ..baseapi import BaseApi


class MergeFields(BaseApi):

    def __init__(self, *args, **kwargs):
        super(MergeFields, self).__init__(*args, **kwargs)
        self.endpoint = 'lists'

    def all(self, list_id, **queryparams):
        """
        returns the first 10 merge-fields for a specific list.
        """
        return self._mc_client._get(url=self._build_path(list_id, 'merge-fields'), **queryparams)

    def get(self, list_id, merge_field_id):
        """
        returns the specified list merge_field.
        """
        return self._mc_client._get(url=self._build_path(list_id, 'merge-fields', merge_field_id))

    def update(self, list_id, merge_field_id, data):
        """
        updates an existing list merge_field.
        """
        return self._mc_client._patch(url=self._build_path(list_id, 'merge-fields', merge_field_id), data=data)

    def delete(self, list_id, merge_field_id):
        """
        removes an existing list merge_field from the list. This cannot be undone.
        """
        return self._mc_client._delete(url=self._build_path(list_id, 'merge-fields', merge_field_id))

    def create(self, list_id, data):
        """
        adds a new merge_field to the list.
        """
        return self._mc_client._post(url=self._build_path(list_id, 'merge-fields'), data=data)
