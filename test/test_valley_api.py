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
from dbpedia.api.valley_api import ValleyApi  # noqa: E501
from dbpedia.rest import ApiException


class TestValleyApi(unittest.TestCase):
    """ValleyApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.valley_api.ValleyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_valleys_get(self):
        """Test case for valleys_get

        List all instances of Valley  # noqa: E501
        """
        pass

    def test_valleys_id_get(self):
        """Test case for valleys_id_get

        Get a single Valley by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
