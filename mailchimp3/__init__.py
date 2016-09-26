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
# Batche Operations
from mailchimp3.entities.batches import Batches
# Campaign Folders
from mailchimp3.entities.campaignfolders import CampaignFolders
# Campaigns
from mailchimp3.entities.campaigns import Campaigns
# Conversations
from mailchimp3.entities.conversations import Conversations
# E-commerce Stores
from mailchimp3.entities.stores import Stores
# File Manager Files
from mailchimp3.entities.filemanagerfiles import FileManagerFiles
# File Manager Folders
from mailchimp3.entities.filemanagerfolders import FileManagerFolders
# Lists
from mailchimp3.entities.lists import Lists
# Reports
from mailchimp3.entities.reports import Reports
# Template Folders
from mailchimp3.entities.templatefolders import TemplateFolders
# Templates
from mailchimp3.entities.template import Template


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
        self.report = Reports(self)
        # Template Folders
        self.templatefolders = TemplateFolders(self)
        # Templates
        self.template = Template(self)
