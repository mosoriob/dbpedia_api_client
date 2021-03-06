# coding: utf-8

"""
    DBpedia

    This is the API of the DBpedia Ontology  # noqa: E501

    The version of the OpenAPI document: v0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import dbpedia
from dbpedia.api.shopping_mall_api import ShoppingMallApi  # noqa: E501
from dbpedia.rest import ApiException


class TestShoppingMallApi(unittest.TestCase):
    """ShoppingMallApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.shopping_mall_api.ShoppingMallApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_shoppingmalls_get(self):
        """Test case for shoppingmalls_get

        List all instances of ShoppingMall  # noqa: E501
        """
        pass

    def test_shoppingmalls_id_get(self):
        """Test case for shoppingmalls_id_get

        Get a single ShoppingMall by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
