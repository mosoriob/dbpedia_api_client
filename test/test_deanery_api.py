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
from dbpedia.api.deanery_api import DeaneryApi  # noqa: E501
from dbpedia.rest import ApiException


class TestDeaneryApi(unittest.TestCase):
    """DeaneryApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.deanery_api.DeaneryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_deanerys_get(self):
        """Test case for deanerys_get

        List all instances of Deanery  # noqa: E501
        """
        pass

    def test_deanerys_id_get(self):
        """Test case for deanerys_id_get

        Get a single Deanery by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
