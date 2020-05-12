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
from dbpedia.api.boxing_api import BoxingApi  # noqa: E501
from dbpedia.rest import ApiException


class TestBoxingApi(unittest.TestCase):
    """BoxingApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.boxing_api.BoxingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_boxings_get(self):
        """Test case for boxings_get

        List all instances of Boxing  # noqa: E501
        """
        pass

    def test_boxings_id_get(self):
        """Test case for boxings_id_get

        Get a single Boxing by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
