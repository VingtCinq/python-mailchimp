# coding=utf-8
"""
The E-commerce Stores API endpoint

Documentation: http://developer.mailchimp.com/documentation/mailchimp/reference/ecommerce/stores/
Schema: https://api.mailchimp.com/schema/3.0/Ecommerce/Stores/Instance.json
"""
from __future__ import unicode_literals

from mailchimp3.baseapi import BaseApi
from mailchimp3.entities.storecart import StoreCart
from mailchimp3.entities.storecustomer import StoreCustomer
from mailchimp3.entities.storeorder import StoreOrder
from mailchimp3.entities.storeproduct import StoreProduct


class Store(BaseApi):
    """
    Connect your E-commerce Store to MailChimp to take advantage of powerful
    reporting and personalization features and to learn more about your
    customers.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(Store, self).__init__(*args, **kwargs)
        self.endpoint = 'ecommerce/stores'
        self.store_id = None
        self.cart = StoreCart(self)
        self.customer = StoreCustomer(self)
        self.order = StoreOrder(self)
        self.product = StoreProduct(self)

    def create(self, data):
        """
        Add a new store to your MailChimp account.

        :param data: The request body parameters
        :type data: :py:class:`dict`
        """
        response = self._mc_client._post(url=self._build_path(), data=data)
        self.store_id = response['id']
        return response


    def all(self, get_all=False, **queryparams):
        """
        Get information about all stores in the account.

        :param get_all: Should the query get all results
        :type get_all: :py:class:`bool`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        queryparams['count'] = integer
        queryparams['offset'] = integer
        """
        self.store_id = None
        if get_all:
            return self._iterate(url=self._build_path(), **queryparams)
        else:
            return self._mc_client._get(url=self._build_path(), **queryparams)


    def get(self, store_id, **queryparams):
        """
        Get information about a specific store.

        :param store_id: The store id.
        :type store_id: :py:class:`str`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        """
        self.store_id = store_id
        return self._mc_client._get(url=self._build_path(store_id), **queryparams)


    def update(self, store_id, data):
        """
        Update a store.

        :param store_id: The store id.
        :type store_id: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:class:`dict`
        """
        self.store_id = store_id
        return self._mc_client._patch(url=self._build_path(store_id), data=data)


    def delete(self, store_id):
        """
        Delete a store. Deleting a store will also delete any associated
        subresources, including Customers, Orders, Products, and Carts.

        :param store_id: The store id.
        :type store_id: :py:class:`str`
        """
        self.store_id = store_id
        return self._mc_client._delete(url=self._build_path(store_id))
