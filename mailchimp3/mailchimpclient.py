# coding=utf-8
"""
Mailchimp v3 Api SDK

Documentation: http://developer.mailchimp.com/documentation/mailchimp/
"""
from __future__ import unicode_literals
import functools

import requests
from requests.auth import HTTPBasicAuth
# Handle library reorganisation Python 2 > Python 3.
try:
    from urllib.parse import urljoin
    from urllib.parse import urlencode
except ImportError:
    from urlparse import urljoin
    from urllib import urlencode

import logging

_logger = logging.getLogger('mailchimp3.client')

def _enabled_or_noop(fn):
    @functools.wraps(fn)
    def wrapper(self, *args, **kwargs):
        if self.enabled:
            return fn(self, *args, **kwargs)
    return wrapper


class MailChimpClient(object):
    """
    MailChimp class to communicate with the v3 API
    """
    def __init__(self, mc_user=None, mc_secret=None, enabled=True, timeout=None,
                 request_hooks=None, request_headers=None, access_token=None):
        """
        Initialize the class with you user_id and secret_key.

        If `enabled` is not True, these methods become no-ops. This is
        particularly useful for testing or disabling with configuration.

        :param mc_user: Mailchimp user id
        :type mc_user: :py:class:`str`
        :param mc_secret: Mailchimp secret key
        :type mc_secret: :py:class:`str`
        :param enabled: Whether the API should execute any requests
        :type enabled: :py:class:`bool`
        :param timeout: (optional) How long to wait for the server to send
            data before giving up, as a float, or a :ref:`(connect timeout,
            read timeout) <timeouts>` tuple.
        :type timeout: float or tuple
        :param request_hooks: (optional) Hooks for :py:func:`requests.requests`.
        :type request_hooks: :py:class:`dict`
        :param request_headers: (optional) Headers for
            :py:func:`requests.requests`.
        :type request_headers: :py:class:`dict`
        :param access_token: OAuth2 access token
        :type enabled: :py:class:`string`
        """
        super(MailChimpClient, self).__init__()
        self.enabled = enabled
        self.timeout = timeout
        if access_token:
            self.auth = MailchimpOAuth(access_token)
            try:
                self.base_url = self.auth.get_base_url() + '/3.0/'
            except requests.exceptions.RequestException:
                raise Exception("Failed to successfully authenticate and obtain metadata")
        elif mc_user and mc_secret:
            self.auth = HTTPBasicAuth(mc_user, mc_secret)
            datacenter = mc_secret.split('-').pop()
            self.base_url = 'https://{}.api.mailchimp.com/3.0/'.format(datacenter)
        else:
            raise Exception("You must provide either access_token or a username and api_key")
        self.request_headers = request_headers or requests.utils.default_headers()
        self.request_hooks = request_hooks or requests.hooks.default_hooks()


    def _make_request(self, **kwargs):
        _logger.info(u'{method} Request: {url}'.format(**kwargs))
        if kwargs.get('json'):
            _logger.info('PAYLOAD: {json}'.format(**kwargs))

        response = requests.request(**kwargs)

        _logger.info(u'{method} Response: {status} {text}'\
            .format(method=kwargs['method'], status=response.status_code, text=response.text))

        return response

    @_enabled_or_noop
    def _post(self, url, data=None):
        """
        Handle authenticated POST requests

        :param url: The url for the endpoint including path parameters
        :type url: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:data:`none` or :py:class:`dict`
        :returns: The JSON output from the API or an error message
        """
        url = urljoin(self.base_url, url)
        try:
            r = self._make_request(**dict(
                method='POST',
                url=url,
                json=data,
                auth=self.auth,
                timeout=self.timeout,
                hooks=self.request_hooks,
                headers=self.request_headers
            ))
        except requests.exceptions.RequestException as e:
            raise e
        else:
            r.raise_for_status()
            if r.status_code == 204:
                return None
            return r.json()


    @_enabled_or_noop
    def _get(self, url, **queryparams):
        """
        Handle authenticated GET requests

        :param url: The url for the endpoint including path parameters
        :type url: :py:class:`str`
        :param queryparams: The query string parameters
        :returns: The JSON output from the API
        """
        url = urljoin(self.base_url, url)
        if len(queryparams):
            url += '?' + urlencode(queryparams)
        try:
            r = self._make_request(**dict(
                method='GET',
                url=url,
                auth=self.auth,
                timeout=self.timeout,
                hooks=self.request_hooks,
                headers=self.request_headers
            ))
        except requests.exceptions.RequestException as e:
            raise e
        else:
            r.raise_for_status()
            return r.json()


    @_enabled_or_noop
    def _delete(self, url):
        """
        Handle authenticated DELETE requests

        :param url: The url for the endpoint including path parameters
        :type url: :py:class:`str`
        :returns: The JSON output from the API
        """
        url = urljoin(self.base_url, url)
        try:
            r = self._make_request(**dict(
                method='DELETE',
                url=url,
                auth=self.auth,
                timeout=self.timeout,
                hooks=self.request_hooks,
                headers=self.request_headers
            ))
        except requests.exceptions.RequestException as e:
            raise e
        else:
            r.raise_for_status()
            if r.status_code == 204:
                return
            return r.json()


    @_enabled_or_noop
    def _patch(self, url, data=None):
        """
        Handle authenticated PATCH requests

        :param url: The url for the endpoint including path parameters
        :type url: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:data:`none` or :py:class:`dict`
        :returns: The JSON output from the API
        """
        url = urljoin(self.base_url, url)
        try:
            r = self._make_request(**dict(
                method='PATCH',
                url=url,
                json=data,
                auth=self.auth,
                timeout=self.timeout,
                hooks=self.request_hooks,
                headers=self.request_headers
            ))
        except requests.exceptions.RequestException as e:
            raise e
        else:
            r.raise_for_status()
            return r.json()


    @_enabled_or_noop
    def _put(self, url, data=None):
        """
        Handle authenticated PUT requests

        :param url: The url for the endpoint including path parameters
        :type url: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:data:`none` or :py:class:`dict`
        :returns: The JSON output from the API
        """
        url = urljoin(self.base_url, url)
        try:
            r = self._make_request(**dict(
                method='PUT',
                url=url,
                json=data,
                auth=self.auth,
                timeout=self.timeout,
                hooks=self.request_hooks,
                headers=self.request_headers
            ))
        except requests.exceptions.RequestException as e:
            raise e
        else:
            r.raise_for_status()
            return r.json()
class MailchimpOAuth(requests.auth.AuthBase):

    def __init__(self, access_token):
        self._access_token = access_token

    def __call__(self, r):
        r.headers['Authorization'] = 'OAuth ' + self._access_token
        return r

    def get_metadata(self):
        try:
            r = requests.get('https://login.mailchimp.com/oauth2/metadata', auth=self)
        except requests.exceptions.RequestException:
            raise
        else:
            r.raise_for_status()
            rj = r.json()
            if "error" in rj:
                raise requests.exceptions.RequestException("Invalid token")
            return rj

    def get_base_url(self):
        try:
            return self.get_metadata()['api_endpoint']
        except requests.exceptions.RequestException :
            raise
