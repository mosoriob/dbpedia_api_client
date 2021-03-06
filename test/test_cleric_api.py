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
from dbpedia.api.cleric_api import ClericApi  # noqa: E501
from dbpedia.rest import ApiException


class TestClericApi(unittest.TestCase):
    """ClericApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.cleric_api.ClericApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_clerics_get(self):
        """Test case for clerics_get

        List all instances of Cleric  # noqa: E501
        """
        pass

    def test_clerics_id_get(self):
        """Test case for clerics_id_get

        Get a single Cleric by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
