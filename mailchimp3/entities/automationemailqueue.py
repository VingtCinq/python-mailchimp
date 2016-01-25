from ..baseapi import BaseApi


class AutomationEmailQueue(BaseApi):

    def __init__(self, *args, **kwargs):
        super(AutomationEmailQueue, self).__init__(*args, **kwargs)
        self.endpoint = 'automations'

    def all(self, workflow_id, email_id):
        """
        Returns a list of queued subscribers for an automated email.
        """
        return self._mc_client._get(url=self._build_path(workflow_id, 'emails', email_id, 'queue'))

    def get(self, workflow_id, email_id):
        """
        returns a summary of an automated email's setting and content.
        """
        return self._mc_client._get(url=self._build_path(workflow_id, 'emails', email_id, 'queue'))

    def create(self, workflow_id='', email_id='', data=''):
        """
        Adds a subscriber to the queue of an automated email.
        """
        return self._mc_client._post(
            url=self._build_path(workflow_id, 'emails', email_id, 'actions/pause-all-emails'),
            data=data)
