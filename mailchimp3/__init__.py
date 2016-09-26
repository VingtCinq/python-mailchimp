# coding=utf-8
"""
Mailchimp v3 Api SDK

Documentation at http://developer.mailchimp.com/documentation/mailchimp/reference/overview/
"""
# API Client
from mailchimp3.mailchimpclient import MailChimpClient
# API Root
from mailchimp3.entities.root import Root
# Authorized Apps
from mailchimp3.entities.authorizedapps import AuthorizedApps
# Automations
from mailchimp3.entities.automations import Automations
from mailchimp3.entities.automationactions import AutomationActions
from mailchimp3.entities.automationemails import AutomationEmails
from mailchimp3.entities.automationemailactions import AutomationEmailActions
from mailchimp3.entities.automationemailqueue import AutomationEmailQueue
from mailchimp3.entities.automationremovedsubscribers import AutomationRemovedSubscribers
# Batche Operations
from mailchimp3.entities.batches import Batches
# Campaign Folders
from mailchimp3.entities.campaignfolders import CampaignFolders
# Campaigns
from mailchimp3.entities.campaigns import Campaigns
from mailchimp3.entities.campaignactions import CampaignActions
from mailchimp3.entities.campaigncontent import CampaignContent
from mailchimp3.entities.campaignfeedback import CampaignFeedback
from mailchimp3.entities.campaignsendchecklist import CampaignSendChecklist
# Conversations
from mailchimp3.entities.conversations import Conversations
from mailchimp3.entities.conversationmessages import ConversationMessages
# E-commerce Stores
from mailchimp3.entities.stores import Stores
from mailchimp3.entities.storecarts import StoreCarts
from mailchimp3.entities.storecartlines import StoreCartLines
from mailchimp3.entities.storecustomers import StoreCustomers
from mailchimp3.entities.storeorders import StoreOrders
from mailchimp3.entities.storeorderlines import StoreOrderLines
from mailchimp3.entities.storeproducts import StoreProducts
from mailchimp3.entities.storeproductvariants import StoreProductVariants
# File Manager Files
from mailchimp3.entities.filemanagerfiles import FileManagerFiles
# File Manager Folders
from mailchimp3.entities.filemanagerfolders import FileManagerFolders
# Lists
from mailchimp3.entities.lists import Lists
from mailchimp3.entities.listabusereports import ListAbuseReports
from mailchimp3.entities.listactivity import ListActivity
from mailchimp3.entities.listclients import ListClients
from mailchimp3.entities.listgrowthhistory import ListGrowthHistory
from mailchimp3.entities.listinterestcategories import ListInterestCategories
from mailchimp3.entities.listinterestcategoryinterest import ListInterestCategoryInterest
from mailchimp3.entities.listmembers import ListMembers
from mailchimp3.entities.listmemberactivity import ListMemberActivity
from mailchimp3.entities.listmembergoals import ListMemberGoals
from mailchimp3.entities.listmembernotes import ListMemberNotes
from mailchimp3.entities.listmergefields import ListMergeFields
from mailchimp3.entities.listsegments import ListSegments
from mailchimp3.entities.listsegmentmembers import ListSegmentMembers
from mailchimp3.entities.listtwitterleadgenerationcards import ListTwitterLeadGenerationCards
from mailchimp3.entities.listwebhooks import ListWebhooks
# Reports
from mailchimp3.entities.report import Report
from mailchimp3.entities.reportabuse import ReportAbuse
from mailchimp3.entities.reportadvice import ReportAdvice
from mailchimp3.entities.reportclickdetail import ReportClickDetail
from mailchimp3.entities.reportclickdetailmember import ReportClickDetailMember
from mailchimp3.entities.reportdomainperformance import ReportDomainPerformance
from mailchimp3.entities.reporteepurl import ReportEepURL
from mailchimp3.entities.reportemailactivity import ReportEmailActivity
from mailchimp3.entities.reportlocation import ReportLocation
from mailchimp3.entities.reportsentto import ReportSentTo
from mailchimp3.entities.reportsubreport import ReportSubReport
from mailchimp3.entities.reportunsubscribe import ReportUnsubscribe
# Template Folders
from mailchimp3.entities.templatefolder import TemplateFolder
# Templates
from mailchimp3.entities.template import Template
from mailchimp3.entities.templatedefaultcontent import TemplateDefaultContent


class MailChimp(MailChimpClient):
    """
    MailChimp class to communicate with the v3 API
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the class with your user_id and secret_key and attach all
        of the endpoints
        """
        super(MailChimp, self).__init__(*args, **kwargs)
        # API Root
        self.root = self.apiroot = Root(self)
        # Authorized Apps
        self.authorizedapps = AuthorizedApps(self)
        # Automations - Paid feature
        self.automations = Automations(self)
        # Batch operations
        self.batches = self.batch_operations = Batches(self)
        # Campaign Folders
        self.campaignfolders = CampaignFolders(self)
        # Campaigns
        self.campaigns = Campaigns(self)
        # Conversations - Paid feature
        self.conversations = Conversations(self)
        # E-commerce Stores
        self.stores = self.ecommerce = Stores(self)
        # File Manager Files
        self.files = FileManagerFiles(self)
        # File Manager Folders
        self.folders = FileManagerFolders(self)
        # Lists
        self.lists = Lists(self)
        # Reports
        self.report = Report(self)
        # Template Folders
        self.templatefolder = TemplateFolder(self)
        # Templates
        self.template = Template(self)
