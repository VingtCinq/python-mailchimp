from ..baseapi import BaseApi


class Automation(BaseApi):

    def __init__(self, *args, **kwargs):
        super(Automation, self).__init__(*args, **kwargs)
        self.endpoint = 'automations'

    def all(self):
        return self._mc_client._get(url=self.endpoint)

    def get(self, workflow_id):
        return self._mc_client._get(url=self._build_path(workflow_id))

    def pause(self, workflow_id):
        return self._mc_client._post(url=self._build_path(workflow_id, 'actions/pause-all-emails'))

    def start(self, workflow_id):
        return self._mc_client._post(url=self._build_path(workflow_id, 'actions/start-all-emails'))
