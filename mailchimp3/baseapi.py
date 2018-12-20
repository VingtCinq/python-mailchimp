# coding=utf-8
"""
The base API object that allows constructions of various endpoint paths
"""
from __future__ import unicode_literals
from itertools import chain

from mailchimp3.helpers import merge_results


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
        Build path with endpoint and args

        :param args: Tokens in the endpoint URL
        :type args: :py:class:`unicode`
        """
        return '/'.join(chain((self.endpoint,), map(str, args)))

    def _list_result(self, url, get_all, iterate, **queryparams):
        """
        Simplify list by returning the single page, all pages or iterates.

        :param get_all: Should the query get all results
        :type get_all: :py:class:`bool`
        :param iterate: Should the query iterate over each page.
        :type iterate: :py:class:`bool`
        """
        if get_all and iterate:
            raise ValueError("Both get_all and iterate can't be True.")
        if get_all:
            return self._all(url=url, **queryparams)
        elif iterate:
            return self._iterate(url=url, **queryparams)
        else:
            return self._mc_client._get(url=url, **queryparams)

    def _iterate(self, url, **queryparams):
        """
        Iterate over pages for the given url. Feed in the result of self._build_path as the url.

        :param url: The url of the endpoint
        :type url: :py:class:`str`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        queryparams['count'] = integer
        queryparams['offset'] = integer
        """
        # fields as a query string parameter should be a string with
        # comma-separated substring values to pass along to
        # self._mc_client._get(). It should also contain total_items whenever
        # the parameter is employed, which is forced here.
        if 'fields' in queryparams:
            if 'total_items' not in queryparams['fields'].split(','):
                queryparams['fields'] += ',total_items'
        # Remove offset and count if provided in queryparams
        # to avoid 'multiple values for keyword argument' TypeError
        queryparams.pop("offset", None)
        queryparams.pop("count", None)
        # Fetch results from mailchimp, up to first 1000
        result = self._mc_client._get(url=url, offset=0, count=1000, **queryparams)
        total = result['total_items']
        # Fetch further results if necessary
        if total > 1000:
            yield result
            for offset in range(1, int(total / 1000) + 1):
                yield self._mc_client._get(
                    url=url,
                    offset=int(offset * 1000),
                    count=1000,
                    **queryparams
                )
        else:  # Further results not necessary
            yield result

    def _all(self, url, **queryparams):
        """
        Iterate over all pages for the given url and return a single collection.
        Feed in the result of self._build_path as the url.

        :param url: The url of the endpoint
        :type url: :py:class:`str`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        queryparams['count'] = integer
        queryparams['offset'] = integer
        """
        result = {}
        for page in self._iterate(url, **queryparams):
            result = merge_results(result, page)
        return result
