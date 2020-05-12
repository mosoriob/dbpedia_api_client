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
from dbpedia.api.gross_domestic_product_api import GrossDomesticProductApi  # noqa: E501
from dbpedia.rest import ApiException


class TestGrossDomesticProductApi(unittest.TestCase):
    """GrossDomesticProductApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.gross_domestic_product_api.GrossDomesticProductApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_grossdomesticproducts_get(self):
        """Test case for grossdomesticproducts_get

        List all instances of GrossDomesticProduct  # noqa: E501
        """
        pass

    def test_grossdomesticproducts_id_get(self):
        """Test case for grossdomesticproducts_id_get

        Get a single GrossDomesticProduct by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
