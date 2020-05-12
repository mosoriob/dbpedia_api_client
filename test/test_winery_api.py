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
from dbpedia.api.winery_api import WineryApi  # noqa: E501
from dbpedia.rest import ApiException


class TestWineryApi(unittest.TestCase):
    """WineryApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.winery_api.WineryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_winerys_get(self):
        """Test case for winerys_get

        List all instances of Winery  # noqa: E501
        """
        pass

    def test_winerys_id_get(self):
        """Test case for winerys_id_get

        Get a single Winery by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()