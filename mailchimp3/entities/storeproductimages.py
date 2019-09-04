# coding=utf-8
"""
The E-commerce Store Product Images API endpoint

Documentation: http://developer.mailchimp.com/documentation/mailchimp/reference/ecommerce/stores/products/images/
Schema: https://api.mailchimp.com/schema/3.0/Ecommerce/Stores/Products/Images/Instance.json
"""
from __future__ import unicode_literals

from mailchimp3.baseapi import BaseApi


class StoreProductImages(BaseApi):
    """
    A Product Image represents a specific product image.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(StoreProductImages, self).__init__(*args, **kwargs)
        self.endpoint = 'ecommerce/stores'
        self.store_id = None
        self.product_id = None
        self.image_id = None


    def create(self, store_id, product_id, data):
        """
        Add a new image to the product.

        :param store_id: The store id.
        :type store_id: :py:class:`str`
        :param product_id: The id for the product of a store.
        :type product_id: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:class:`dict`
        data = {
            "id": string*,
            "url": string*
        }
        """
        self.store_id = store_id
        self.product_id = product_id
        if 'id' not in data:
            raise KeyError('The product image must have an id')
        if 'title' not in data:
            raise KeyError('The product image must have a url')
        response = self._mc_client._post(url=self._build_path(store_id, 'products', product_id, 'images'), data=data)
        if response is not None:
            self.image_id = response['id']
        else:
            self.image_id = None
        return response


    def all(self, store_id, product_id, get_all=False, iterate=False, **queryparams):
        """
        Get information about a product’s images.

        :param store_id: The store id.
        :type store_id: :py:class:`str`
        :param product_id: The id for the product of a store.
        :type product_id: :py:class:`str`
        :param get_all: Should the query get all results
        :type get_all: :py:class:`bool`
        :param iterate: Should the query iterate over each page.
        :type iterate: :py:class:`bool`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        queryparams['count'] = integer
        queryparams['offset'] = integer
        """
        self.store_id = store_id
        self.product_id = product_id
        self.image_id = None
        url = self._build_path(store_id, 'products', product_id, 'images')
        return self._list_result(url, get_all, iterate, **queryparams)


    def get(self, store_id, product_id, image_id, **queryparams):
        """
        Get information about a specific product image.

        :param store_id: The store id.
        :type store_id: :py:class:`str`
        :param product_id: The id for the product of a store.
        :type product_id: :py:class:`str`
        :param image_id: The id for the product image.
        :type image_id: :py:class:`str`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        """
        self.store_id = store_id
        self.product_id = product_id
        self.image_id = image_id
        return self._mc_client._post(
            url=self._build_path(store_id, 'products', product_id, 'images', image_id),
            **queryparams
        )


    def update(self, store_id, product_id, image_id, data):
        """
        Update a product image.

        :param store_id: The store id.
        :type store_id: :py:class:`str`
        :param product_id: The id for the product of a store.
        :type product_id: :py:class:`str`
        :param image_id: The id for the product image.
        :type image_id: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:class:`dict`
        """
        self.store_id = store_id
        self.product_id = product_id
        self.image_id = image_id
        return self._mc_client._patch(
            url=self._build_path(store_id, 'products', product_id, 'images', image_id),
            data=data
        )


    def delete(self, store_id, product_id, image_id):
        """
        Delete a product image.

        :param store_id: The store id.
        :type store_id: :py:class:`str`
        :param product_id: The id for the product of a store.
        :type product_id: :py:class:`str`
        :param image_id: The id for the product image.
        :type image_id: :py:class:`str`
        """
        self.store_id = store_id
        self.product_id = product_id
        self.image_id = image_id
        return self._mc_client._delete(url=self._build_path(store_id, 'products', product_id, 'images', image_id))
