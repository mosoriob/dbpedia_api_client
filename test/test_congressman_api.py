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
from dbpedia.api.congressman_api import CongressmanApi  # noqa: E501
from dbpedia.rest import ApiException


class TestCongressmanApi(unittest.TestCase):
    """CongressmanApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.congressman_api.CongressmanApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_congressmans_get(self):
        """Test case for congressmans_get

        List all instances of Congressman  # noqa: E501
        """
        pass

    def test_congressmans_id_get(self):
        """Test case for congressmans_id_get

        Get a single Congressman by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
