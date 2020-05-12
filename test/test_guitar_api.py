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
from dbpedia.api.guitar_api import GuitarApi  # noqa: E501
from dbpedia.rest import ApiException


class TestGuitarApi(unittest.TestCase):
    """GuitarApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.guitar_api.GuitarApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_guitars_get(self):
        """Test case for guitars_get

        List all instances of Guitar  # noqa: E501
        """
        pass

    def test_guitars_id_get(self):
        """Test case for guitars_id_get

        Get a single Guitar by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
