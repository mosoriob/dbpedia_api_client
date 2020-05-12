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
from dbpedia.api.architect_api import ArchitectApi  # noqa: E501
from dbpedia.rest import ApiException


class TestArchitectApi(unittest.TestCase):
    """ArchitectApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.architect_api.ArchitectApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_architects_get(self):
        """Test case for architects_get

        List all instances of Architect  # noqa: E501
        """
        pass

    def test_architects_id_get(self):
        """Test case for architects_id_get

        Get a single Architect by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
