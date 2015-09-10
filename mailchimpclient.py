"""
Mailchimp v3 Api SDK

"""
import requests
from requests.auth import HTTPBasicAuth
from urlparse import urljoin


class MailChimpClient(object):
    """
    MailChimp class to communicate with the v3 API
    """
    def __init__(self, mc_user, mc_secret):
        """
        Initialize the class with you user_id and secret_key
        """
        super(MailChimpClient, self).__init__()
        self.auth = HTTPBasicAuth(mc_user, mc_secret)
        datacenter = mc_secret.split('-').pop()
        self.base_url = 'https://%s.api.mailchimp.com/3.0/' % datacenter

    def _post(self, url, json=None):
        url = urljoin(self.base_url, url)
        print url
        r = requests.post(url, auth=self.auth, json=json)
        return r.json()

    def _get(self, url):
        url = urljoin(self.base_url, url)
        print url
        r = requests.get(url, auth=self.auth)
        return r.json()

    def _delete(self, url):
        url = urljoin(self.base_url, url)
        print url
        r = requests.delete(url, auth=self.auth)
        return r.json()

    def _patch(self, url, data=None):
        url = urljoin(self.base_url, url)
        print url
        r = requests.patch(url, auth=self.auth, json=data)
        return r.json()
