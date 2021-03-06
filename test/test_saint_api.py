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
from dbpedia.api.saint_api import SaintApi  # noqa: E501
from dbpedia.rest import ApiException


class TestSaintApi(unittest.TestCase):
    """SaintApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.saint_api.SaintApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_saints_get(self):
        """Test case for saints_get

        List all instances of Saint  # noqa: E501
        """
        pass

    def test_saints_id_get(self):
        """Test case for saints_id_get

        Get a single Saint by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
