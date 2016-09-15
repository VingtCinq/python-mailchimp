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
from mailchimp3.entities.automation import Automation
from mailchimp3.entities.automationaction import AutomationAction
from mailchimp3.entities.automationemail import AutomationEmail
from mailchimp3.entities.automationemailaction import AutomationEmailAction
from mailchimp3.entities.automationemailqueue import AutomationEmailQueue
from mailchimp3.entities.automationeremovedsubscriber import AutomationRemovedSubscriber
# Batche Operations
from mailchimp3.entities.batch import Batch
# Campaign Folders
from mailchimp3.entities.campaignfolder import CampaignFolder
# Campaigns
from mailchimp3.entities.campaign import Campaign
from mailchimp3.entities.campaignaction import CampaignAction
from mailchimp3.entities.campaigncontent import CampaignContent
from mailchimp3.entities.campaignfeedback import CampaignFeedback
from mailchimp3.entities.campaignsendchecklist import CampaignSendChecklist
# Conversations
from mailchimp3.entities.conversation import Conversation
from mailchimp3.entities.conversationmessage import ConversationMessage
# E-commerce Stores
from mailchimp3.entities.store import Store
from mailchimp3.entities.storecart import StoreCart
from mailchimp3.entities.storecartline import StoreCartLine
from mailchimp3.entities.storecustomer import StoreCustomer
from mailchimp3.entities.storeorder import StoreOrder
from mailchimp3.entities.storeorderline import StoreOrderLine
from mailchimp3.entities.storeproduct import StoreProduct
from mailchimp3.entities.storeproductvariant import StoreProductVariant
# File Manager Files
from mailchimp3.entities.file import File
# File Manager Folders
from mailchimp3.entities.folder import Folder
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
        self.root = Root(self)
        # Authorized Apps
        self.authorized_app = AuthorizedApps(self)
        # Automation - Paid feature
        self.automation = Automation(self)
        self.automationaction = self.automation.action
        self.automationemail = self.automation.email
        self.automationemailaction = self.automation.email.action
        self.automationemailqueue = self.automation.email.queue
        self.automationeremovedsubscriber = self.automation.removedsubscriber
        # Batch operations
        self.batch = Batch(self)
        # Campaign Folders
        self.campaignfolder = CampaignFolder(self)
        # Campaigns
        self.campaign = Campaign(self)
        self.campaignaction = self.campaign.action
        self.campaigncontent = self.campaign.content
        self.campaignfeedback = self.campaign.feedback
        self.campaignsendchecklist = self.campaign.sendchecklist
        # Conversations - Paid feature
        self.conversation = Conversation(self)
        self.message = self.conversationmessage = self.conversation.message
        # E-commerce Stores
        self.store = self.ecommerce = Store(self)
        self.cart = self.storecart = self.store.cart
        self.cartline = self.storecartline = self.store.cart.line
        self.customer = self.storecustomer = self.store.customer
        self.order = self.storeorder = self.store.order
        self.orderline = self.storeorderline = self.store.order.line
        self.product = self.storeproduct = self.store.product
        self.productvariant = self.storeproductvariant = self.store.product.variant
        # File Manager Files
        self.file = File(self)
        # File Manager Folders
        self.folder = Folder(self)
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
