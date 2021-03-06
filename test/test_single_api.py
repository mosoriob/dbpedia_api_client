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
from dbpedia.api.single_api import SingleApi  # noqa: E501
from dbpedia.rest import ApiException


class TestSingleApi(unittest.TestCase):
    """SingleApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.single_api.SingleApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_singles_get(self):
        """Test case for singles_get

        List all instances of Single  # noqa: E501
        """
        pass

    def test_singles_id_get(self):
        """Test case for singles_id_get

        Get a single Single by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
