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
from dbpedia.api.singer_api import SingerApi  # noqa: E501
from dbpedia.rest import ApiException


class TestSingerApi(unittest.TestCase):
    """SingerApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.singer_api.SingerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_singers_get(self):
        """Test case for singers_get

        List all instances of Singer  # noqa: E501
        """
        pass

    def test_singers_id_get(self):
        """Test case for singers_id_get

        Get a single Singer by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
