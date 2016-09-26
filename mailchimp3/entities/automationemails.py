# coding=utf-8
"""
The Automation Emails endpoint

Note: This is a paid feature

Documentation: http://developer.mailchimp.com/documentation/mailchimp/reference/automations/emails/
Schema: https://api.mailchimp.com/schema/3.0/Automations/Emails/Instance.json
"""
from __future__ import unicode_literals

from mailchimp3.baseapi import BaseApi
from mailchimp3.entities.automationemailactions import AutomationEmailActions
from mailchimp3.entities.automationemailqueues import AutomationEmailQueues


class AutomationEmails(BaseApi):
    """
    Manage individual emails in an Automation workflow.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(AutomationEmails, self).__init__(*args, **kwargs)
        self.endpoint = 'automations'
        self.workflow_id = None
        self.email_id = None
        self.actions = AutomationEmailActions(self)
        self.queues = AutomationEmailQueues(self)


    # Paid feature
    def all(self, workflow_id):
        """
        Get a summary of the emails in an Automation workflow.

        :param workflow_id: The unique id for the Automation workflow.
        :type workflow_id: :py:class:`str`
        """
        self.workflow_id = workflow_id
        self.email_id = None
        return self._mc_client._get(url=self._build_path(workflow_id, 'emails'))


    # Paid feature
    def get(self, workflow_id, email_id):
        """
        Get information about an individual Automation workflow email.

        :param workflow_id: The unique id for the Automation workflow.
        :type workflow_id: :py:class:`str`
        :param email_id: The unique id for the Automation workflow email.
        :type email_id: :py:class:`str`
        """
        self.workflow_id = workflow_id
        self.email_id = email_id
        return self._mc_client._get(url=self._build_path(workflow_id, 'emails', email_id))
