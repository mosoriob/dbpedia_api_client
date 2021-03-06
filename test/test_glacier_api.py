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
from dbpedia.api.glacier_api import GlacierApi  # noqa: E501
from dbpedia.rest import ApiException


class TestGlacierApi(unittest.TestCase):
    """GlacierApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.glacier_api.GlacierApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_glaciers_get(self):
        """Test case for glaciers_get

        List all instances of Glacier  # noqa: E501
        """
        pass

    def test_glaciers_id_get(self):
        """Test case for glaciers_id_get

        Get a single Glacier by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
