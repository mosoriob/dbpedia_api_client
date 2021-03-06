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
from dbpedia.api.athletics_api import AthleticsApi  # noqa: E501
from dbpedia.rest import ApiException


class TestAthleticsApi(unittest.TestCase):
    """AthleticsApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.athletics_api.AthleticsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_athleticss_get(self):
        """Test case for athleticss_get

        List all instances of Athletics  # noqa: E501
        """
        pass

    def test_athleticss_id_get(self):
        """Test case for athleticss_id_get

        Get a single Athletics by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
