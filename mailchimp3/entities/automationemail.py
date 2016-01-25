from ..baseapi import BaseApi


class AutomationEmail(BaseApi):

    def __init__(self, *args, **kwargs):
        super(AutomationEmail, self).__init__(*args, **kwargs)
        self.endpoint = 'automations'

    def all(self, workflow_id):
        return self._mc_client._get(url=self._build_path(workflow_id, 'emails'))

    def get(self, workflow_id, email_id):
        """
        returns a summary of an automated email's setting and content.
        """
        return self._mc_client._get(url=self._build_path(workflow_id, 'emails', email_id))

    def pause(self, workflow_id, email_id):
        return self._mc_client._post(
            url=self._build_path(workflow_id, 'emails', email_id, 'actions/pause-all-emails'))

    def start(self, workflow_id, email_id):
        return self._mc_client._post(
            url=self._build_path(workflow_id, 'emails', email_id, 'actions/start-all-emails'))
