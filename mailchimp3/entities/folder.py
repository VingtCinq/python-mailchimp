from __future__ import unicode_literals
from ..baseapi import BaseApi


class Folder(BaseApi):

    def __init__(self, *args, **kwargs):
        super(Folder, self).__init__(*args, **kwargs)
        self.endpoint = 'file-manager/folders'

    def all(self, **queryparams):
        return self._mc_client._get(url=self.endpoint, **queryparams)

    def get(self, folder_id):
        """
        returns a specific folder's information.
        """
        return self._mc_client._get(url=self._build_path(folder_id))

    def update(self, folder_id, data):
        """
        updates a folder's information.
        """
        return self._mc_client._patch(url=self._build_path(folder_id), data=data)

    def delete(self, folder_id):
        """
        removes a folder from the File Manager.
        """
        return self._mc_client._delete(url=self._build_path(folder_id))


    def create(self, data):
        """
        creates a folder in the File Manager. Data should be a dictionary
        containing the name of the folder to create
        """
        return self._mc_client._post(url=self.endpoint, data=data)
