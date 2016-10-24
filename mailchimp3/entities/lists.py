# coding=utf-8
"""
The Lists API endpoint

Documentation: http://developer.mailchimp.com/documentation/mailchimp/reference/lists/
Schema: https://api.mailchimp.com/schema/3.0/Lists/Instance.json
"""
from __future__ import unicode_literals

from mailchimp3.baseapi import BaseApi
from mailchimp3.entities.listabusereports import ListAbuseReports
from mailchimp3.entities.listactivity import ListActivity
from mailchimp3.entities.listclients import ListClients
from mailchimp3.entities.listgrowthhistory import ListGrowthHistory
from mailchimp3.entities.listinterestcategories import ListInterestCategories
from mailchimp3.entities.listmembers import ListMembers
from mailchimp3.entities.listmergefields import ListMergeFields
from mailchimp3.entities.listsegments import ListSegments
from mailchimp3.entities.listsignupforms import ListSignupForms
from mailchimp3.entities.listtwitterleadgenerationcards import ListTwitterLeadGenerationCards
from mailchimp3.entities.listwebhooks import ListWebhooks
from mailchimp3.helpers import check_email


class Lists(BaseApi):
    """
    A MailChimp list is a powerful and flexible tool that helps you manage your contacts.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(Lists, self).__init__(*args, **kwargs)
        self.endpoint = 'lists'
        self.list_id = None
        self.abuse_reports = ListAbuseReports(self)
        self.activity = ListActivity(self)
        self.clients = ListClients(self)
        self.growth_history = ListGrowthHistory(self)
        self.interest_categories = ListInterestCategories(self)
        self.members = ListMembers(self)
        self.merge_fields = ListMergeFields(self)
        self.segments = ListSegments(self)
        self.signup_forms = ListSignupForms(self)
        self.twitter_cards = ListTwitterLeadGenerationCards(self)
        self.webhooks = ListWebhooks(self)


    def create(self, data):
        """
        Create a new list in your MailChimp account.

        :param data: The request body parameters
        :type data: :py:class:`dict`
        data = {
            "name": string*,
            "contact": object*
            {
                "company": string*,
                "address1": string*,
                "city": string*,
                "state": string*,
                "zip": string*,
                "country": string*
            },
            "permision_reminder": string*,
            "campaign_defaults": object*
            {
                "from_name": string*,
                "from_email": string*,
                "subject": string*,
                "language": string*
            },
            "email_type_option": boolean
        }
        """
        try:
            test = data['name']
        except KeyError as error:
            error.message += ' The list must have a name'
            raise
        try:
            test = data['contact']
        except KeyError as error:
            error.message += ' The list must have a contact'
            raise
        try:
            test = data['contact']['company']
        except KeyError as error:
            error.message += ' The list contact must have a company'
            raise
        try:
            test = data['contact']['address1']
        except KeyError as error:
            error.message += ' The list contact must have a address1'
            raise
        try:
            test = data['contact']['city']
        except KeyError as error:
            error.message += ' The list contact must have a city'
            raise
        try:
            test = data['contact']['state']
        except KeyError as error:
            error.message += ' The list contact must have a state'
            raise
        try:
            test = data['contact']['zip']
        except KeyError as error:
            error.message += ' The list contact must have a zip'
            raise
        try:
            test = data['contact']['country']
        except KeyError as error:
            error.message += ' The list contact must have a country'
            raise
        try:
            test = data['permission_reminder']
        except KeyError as error:
            error.message += ' The list must have a permission_reminder'
            raise
        try:
            test = data['campaign_defaults']
        except KeyError as error:
            error.message += ' The list must have a campaign_defaults'
            raise
        try:
            test = data['campaign_defaults']['from_name']
        except KeyError as error:
            error.message += ' The list campaign_defaults must have a from_name'
            raise
        try:
            test = data['campaign_defaults']['from_email']
        except KeyError as error:
            error.message += ' The list campaign_defaults must have a from_email'
            raise
        check_email(data['campaign_defaults']['from_email'])
        try:
            test = data['campaign_defaults']['subject']
        except KeyError as error:
            error.message += ' The list campaign_defaults must have a subject'
            raise
        try:
            test = data['campaign_defaults']['language']
        except KeyError as error:
            error.message += ' The list campaign_defaults must have a language'
            raise
        try:
            test = data['email_type_option']
        except KeyError as error:
            error.message += ' The list must have an email_type_option'
            raise
        if data['email_type_option'] not in [True, False]:
            raise TypeError('The list email_type_option must be True or False')
        response = self._mc_client._post(url=self._build_path(), data=data)
        self.list_id = response['id']
        return response


    def update_members(self, list_id, data):
        """
        Batch subscribe or unsubscribe list members.

        Only the members array is required in the request body parameters, but
        the description of it mentions both the email_address and status
        values, so those are going to be treated as required. The
        update_existing parameter will also be considered required to help
        prevent accidental updates to existing members and will default to
        false if not present.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:class:`dict`
        data = {
            "members": array*
            [
                {
                    "email_address": string*,
                    "status": string* (Must be one of 'subscribed', 'unsubscribed', 'cleaned', or 'pending')
                }
            ],
            "update_existing": boolean*
        }
        """
        self.list_id = list_id
        try:
            test = data['members']
            if not len(test) <= 500:
                raise ValueError('You may only batch sub/unsub 500 members at a time')
        except KeyError as error:
            error.message += ' The update must have at least one member'
            raise
        for member in data['members']:
            try:
                test = member['email_address']
            except KeyError as error:
                error.message += ' Each list member must have an email_address'
                raise
            check_email(member['email_address'])
            try:
                test = member['status']
            except KeyError as error:
                error.message += ' Each list member must have a status'
                raise
            if member['status'] not in ['subscribed', 'unsubscribed', 'cleaned', 'pending']:
                raise ValueError('The list member status must be one of "subscribed", "unsubscribed", "cleaned", or '
                                 '"pending"')
        try:
            test = data['update_existing']
        except KeyError:
            data['update_existing'] = False
        return self._mc_client._post(url=self._build_path(), data=data)


    def all(self, get_all=False, **queryparams):
        """
        Get information about all lists in the account.

        :param get_all: Should the query get all results
        :type get_all: :py:class:`bool`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        queryparams['count'] = integer
        queryparams['offset'] = integer
        queryparams['before_date_created'] = string
        queryparams['since_date_created'] = string
        queryparams['before_campaign_last_sent'] = string
        queryparams['since_campaign_last_sent'] = string
        queryparams['email'] = string
        """
        self.list_id = None
        if get_all:
            return self._iterate(url=self._build_path(), **queryparams)
        else:
            return self._mc_client._get(url=self._build_path(), **queryparams)


    def get(self, list_id, **queryparams):
        """
        Get information about a specific list in your MailChimp account.
        Results include list members who have signed up but haven’t confirmed
        their subscription yet and unsubscribed or cleaned.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        """
        self.list_id = list_id
        return self._mc_client._get(url=self._build_path(list_id), **queryparams)


    def update(self, list_id, data):
        """
        Update the settings for a specific list.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:class:`dict`
        data = {
            "name": string*,
            "contact": object*
            {
                "company": string*,
                "address1": string*,
                "city": string*,
                "state": string*,
                "zip": string*,
                "country": string*
            },
            "permision_reminder": string*,
            "campaign_defaults": object*
            {
                "from_name": string*,
                "from_email": string*,
                "subject": string*,
                "language": string*
            },
            "email_type_option": boolean
        }
        """
        self.list_id = list_id
        try:
            test = data['name']
        except KeyError as error:
            error.message += ' The list must have a name'
            raise
        try:
            test = data['contact']
        except KeyError as error:
            error.message += ' The list must have a contact'
            raise
        try:
            test = data['contact']['company']
        except KeyError as error:
            error.message += ' The list contact must have a company'
            raise
        try:
            test = data['contact']['address1']
        except KeyError as error:
            error.message += ' The list contact must have a address1'
            raise
        try:
            test = data['contact']['city']
        except KeyError as error:
            error.message += ' The list contact must have a city'
            raise
        try:
            test = data['contact']['state']
        except KeyError as error:
            error.message += ' The list contact must have a state'
            raise
        try:
            test = data['contact']['zip']
        except KeyError as error:
            error.message += ' The list contact must have a zip'
            raise
        try:
            test = data['contact']['country']
        except KeyError as error:
            error.message += ' The list contact must have a country'
            raise
        try:
            test = data['permission_reminder']
        except KeyError as error:
            error.message += ' The list must have a permission_reminder'
            raise
        try:
            test = data['campaign_defaults']
        except KeyError as error:
            error.message += ' The list must have a campaign_defaults'
            raise
        try:
            test = data['campaign_defaults']['from_name']
        except KeyError as error:
            error.message += ' The list campaign_defaults must have a from_name'
            raise
        try:
            test = data['campaign_defaults']['from_email']
        except KeyError as error:
            error.message += ' The list campaign_defaults must have a from_email'
            raise
        check_email(data['campaign_defaults']['from_email'])
        try:
            test = data['campaign_defaults']['subject']
        except KeyError as error:
            error.message += ' The list campaign_defaults must have a subject'
            raise
        try:
            test = data['campaign_defaults']['language']
        except KeyError as error:
            error.message += ' The list campaign_defaults must have a language'
            raise
        try:
            test = data['email_type_option']
        except KeyError as error:
            error.message += ' The list must have an email_type_option'
            raise
        if data['email_type_option'] not in [True, False]:
            raise TypeError('The list email_type_option must be True or False')
        return self._mc_client._patch(url=self._build_path(list_id), data=data)


    def delete(self, list_id):
        """
        Delete a list from your MailChimp account. If you delete a list,
        you’ll lose the list history—including subscriber activity,
        unsubscribes, complaints, and bounces. You’ll also lose subscribers’
        email addresses, unless you exported and backed up your list.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        """
        self.list_id = list_id
        return self._mc_client._delete(url=self._build_path(list_id))

