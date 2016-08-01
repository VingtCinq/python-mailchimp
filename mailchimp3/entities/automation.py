# coding=utf-8
"""
The Automations API endpoint

Note: This is a paid feature

Documentation: http://developer.mailchimp.com/documentation/mailchimp/reference/automations/
Schema: https://api.mailchimp.com/schema/3.0/Automations/Instance.json
"""
from __future__ import unicode_literals

from mailchimp3.baseapi import BaseApi
from mailchimp3.entities.automationaction import AutomationAction
from mailchimp3.entities.automationemail import AutomationEmail
from mailchimp3.entities.automationeremovedsubscriber import AutomationRemovedSubscriber


class Automation(BaseApi):
    """
    Manage Automation workflows.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(Automation, self).__init__(*args, **kwargs)
        self.endpoint = 'automations'
        self.workflow_id = None
        self.action = AutomationAction(self)
        self.email = AutomationEmail(self)
        self.removedsubscriber = AutomationRemovedSubscriber(self)


    # Paid feature
    def all(self, get_all=False, **queryparams):
        """
        Get a summary of an account’s Automations.

        :param get_all: Should the query get all results
        :type get_all: :py:class:`bool`
        :param queryparams: the query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        """
        self.workflow_id = None
        if get_all:
            return self._iterate(url=self._build_path(), **queryparams)
        else:
            return self._mc_client._get(url=self._build_path(), **queryparams)


    # Paid feature
    def get(self, workflow_id):
        """
        Get a summary of an individual Automation workflow’s settings and
        content.

        :param workflow_id: The unique id for the Automation workflow
        :type workflow_id: :py:class:`str`
        """
        self.workflow_id = workflow_id
        return self._mc_client._get(url=self._build_path(workflow_id))
