# coding=utf-8
"""
The Reports API endpoint

Documentation: http://developer.mailchimp.com/documentation/mailchimp/reference/reports/
Schema: https://api.mailchimp.com/schema/3.0/Reports/Instance.json
"""
from __future__ import unicode_literals

from mailchimp3.baseapi import BaseApi
from mailchimp3.entities.reportabuse import ReportAbuse
from mailchimp3.entities.reportadvice import ReportAdvice
from mailchimp3.entities.reportclickdetail import ReportClickDetail
from mailchimp3.entities.reportdomainperformance import ReportDomainPerformance
from mailchimp3.entities.reporteepurl import ReportEepURL
from mailchimp3.entities.reportemailactivity import ReportEmailActivity
from mailchimp3.entities.reportlocation import ReportLocation
from mailchimp3.entities.reportsentto import ReportSentTo
from mailchimp3.entities.reportsubreport import ReportSubReport
from mailchimp3.entities.reportunsubscribe import ReportUnsubscribe


class Report(BaseApi):
    """
    Manage campaign reports for your MailChimp account. All Reports endpoints
    are read-only. MailChimp’s campaign and Automation reports analyze clicks,
    opens, subscribers’ social activity, e-commerce data, and more.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(Report, self).__init__(*args, **kwargs)
        self.endpoint = 'reports'
        self.campaign_id = None
        self.abuse = ReportAbuse(self)
        self.advice = ReportAdvice(self)
        self.clickdetail = ReportClickDetail(self)
        self.domainperformance = ReportDomainPerformance(self)
        self.eepurl = ReportEepURL(self)
        self.emailactivity = ReportEmailActivity(self)
        self.location = ReportLocation(self)
        self.sentto = ReportSentTo(self)
        self.subreport = ReportSubReport(self)
        self.unsubscribe = ReportUnsubscribe(self)


    def all(self, get_all=False, **queryparams):
        """
        Get campaign reports.

        :param get_all: Should the query get all results
        :type get_all: :py:class:`bool`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        queryparams['count'] = integer
        queryparams['offset'] = integer
        queryparams['type'] = []
        queryparams['before_send_time'] = string
        queryparams['since_send_time'] = string
        """
        self.campaign_id = None
        if get_all:
            return self._iterate(url=self._build_path(), **queryparams)
        else:
            return self._mc_client._get(url=self._build_path(), **queryparams)


    def get(self, campaign_id, **queryparams):
        """
        Get report details for a specific sent campaign.

        :param campaign_id: The unique id for the campaign.
        :type campaign_id: :py:class:`str`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        """
        self.campaign_id = campaign_id
        return self._mc_client._get(url=self._build_path(campaign_id), **queryparams)
