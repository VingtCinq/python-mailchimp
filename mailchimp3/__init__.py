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
from mailchimp3.entities.list import List
from mailchimp3.entities.listabusereport import ListAbuseReport
from mailchimp3.entities.listactivity import ListActivity
from mailchimp3.entities.listclient import ListClient
from mailchimp3.entities.listgrowthhistory import ListGrowthHistory
from mailchimp3.entities.listinterestcategory import ListInterestCategory
from mailchimp3.entities.listinterestcategoryinterest import ListInterestCategoryInterest
from mailchimp3.entities.listmember import ListMember
from mailchimp3.entities.listmemberactivity import ListMemberActivity
from mailchimp3.entities.listmembergoal import ListMemberGoal
from mailchimp3.entities.listmembernote import ListMemberNote
from mailchimp3.entities.listmergefield import ListMergeField
from mailchimp3.entities.listsegment import ListSegment
from mailchimp3.entities.listsegmentmember import ListSegmentMember
from mailchimp3.entities.listtwitter import ListTwitter
from mailchimp3.entities.listwebhook import ListWebhook
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
        self.automationactions = self.automations.actions
        self.automationemails = self.automations.emails
        self.automationemailactions = self.automations.emails.actions
        self.automationemailqueue = self.automations.emails.queue
        self.automationeremovedsubscribers = self.automations.removedsubscribers
        # Batch operations
        self.batches = self.batch_operations = Batches(self)
        # Campaign Folders
        self.campaignfolders = CampaignFolders(self)
        # Campaigns
        self.campaigns = Campaigns(self)
        self.campaignactions = self.campaigns.actions
        self.campaigncontent = self.campaigns.content
        self.campaignfeedback = self.campaigns.feedback
        self.campaignsendchecklist = self.campaigns.sendchecklist
        # Conversations - Paid feature
        self.conversations = Conversations(self)
        self.conversationmessages = self.messages = self.conversations.messages
        # E-commerce Stores
        self.store = self.ecommerce = Stores(self)
        self.storecarts = self.carts = self.store.carts
        self.storecartlines = self.cartlines = self.store.carts.lines
        self.storecustomers = self.customers = self.store.customers
        self.storeorders = self.orders = self.store.orders
        self.storeorderlines = self.orderlines = self.store.orders.lines
        self.storeproducts = self.products = self.store.products
        self.storeproductvariants = self.productvariants = self.store.products.variants
        # File Manager Files
        self.files = FileManagerFiles(self)
        # File Manager Folders
        self.folders = FileManagerFolders(self)
        # Lists
        self.list = List(self)
        self.listabuse = self.listabusereport = self.list.abusereport
        self.listactivity = self.list.activity
        self.client = self.listclient = self.list.client
        self.growth = self.listgrowthhistory = self.list.growthhistory
        self.category = self.listinterestcategory = self.list.interestcategory
        self.interest = self.interestcategoryinterest = self.list.interestcategory.interest
        self.member = self.listmember = self.list.member
        self.memberactivity = self.listmemberactivity = self.list.member.activity
        self.goal = self.listmembergoal = self.list.member.goal
        self.note = self.listmembernote = self.list.member.note
        self.mergefield = self.listmergefield = self.list.mergefield
        self.segment = self.listsegment = self.list.segment
        self.segmentmember = self.listsegmentmember = self.list.segment.member
        self.twitter = self.listtwitter = self.list.twitter
        self.webhook = self.listwebhook = self.list.webhook
        # Reports
        self.report = Report(self)
        self.reportabuse = self.report.abuse
        self.advice = self.reportadvice = self.report.advice
        self.clickdetail = self.reportclickdetail = self.report.clickdetail
        self.clickdetailmember = self.reportclickdetailmember = self.report.clickdetail.member
        self.domainperformance = self.reportdomainperformance = self.report.domainperformance
        self.eepurl = self.reporteepurl = self.report.eepurl
        self.reportactivity = self.reportemailactivity = self.report.emailactivity
        self.location = self.reportlocation = self.report.location
        self.sentto = self.reportsentto = self.report.sentto
        self.subreport = self.reportsubreport = self.report.subreport
        self.reportunsubscribed = self.report.unsubscribe
        # Template Folders
        self.templatefolder = TemplateFolder(self)
        # Templates
        self.template = Template(self)
        self.templatedefaultcontent = self.template.defaultcontent
