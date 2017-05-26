# coding=utf-8
"""
The base API object that allows constructions of various endpoint paths
"""
from __future__ import unicode_literals
from itertools import chain

from mailchimp3.helpers import  merge_results

class BaseApi(object):
    """
    Simple class to buid path for entities
    """
    def __init__(self, mc_client):
        """
        Initialize the class with you user_id and secret_key

        :param mc_client: The mailchimp client connection
        :type mc_client: :mod:`mailchimp3.mailchimpclient.MailChimpClient`
        """
        super(BaseApi, self).__init__()
        self._mc_client = mc_client
        self.endpoint = ''


    def _build_path(self, *args):
        """
        Build path width endpoint and args

        :param args: Tokens in the endpoint URL
        :type args: :py:class:`unicode`
        """
        return '/'.join(chain((self.endpoint,), args))


    def _iterate(self, url, **kwargs):
        """
        Iterate over all pages for the given url. Feed in the result of self._build_path as the url.

        :param url: The url of the endpoint
        :type url: :py:class:`str`
        :param kwargs: The query string parameters
        kwargs['fields'] = []
        kwargs['exclude_fields'] = []
        kwargs['count'] = integer
        kwargs['offset'] = integer
        """
        #fields as a kwarg ought to be a string with comma-separated substring
        #values to pass along to self._mc_client._get(). it also ought to
        #contain total_items whenever the kwarg is employed, this is enforced
        if 'fields' in kwargs:
            if 'total_items' not in kwargs['fields'].split(','):
                kwargs['fields'] += ',total_items'
        # Remove offset and count if provided in kwargs
        # to avoid 'multiple values for keyword argument' TypeError
        kwargs.pop("offset", None)
        kwargs.pop("count", None)
        #Fetch results from mailchimp, up to first 5000
        result = self._mc_client._get(url=url, offset=0, count=5000, **kwargs)
        total = result['total_items']
        #Fetch further results if necessary
        if total > 5000:
            for offset in range(1, int(total / 5000) + 1):
                result = merge_results(result, self._mc_client._get(
                    url=url,
                    offset=int(offset*5000),
                    count=5000,
                    **kwargs
                ))
            return result
        else:  # Further results not necessary
            return result
