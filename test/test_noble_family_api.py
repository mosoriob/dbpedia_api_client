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
from dbpedia.api.noble_family_api import NobleFamilyApi  # noqa: E501
from dbpedia.rest import ApiException


class TestNobleFamilyApi(unittest.TestCase):
    """NobleFamilyApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.noble_family_api.NobleFamilyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_noblefamilys_get(self):
        """Test case for noblefamilys_get

        List all instances of NobleFamily  # noqa: E501
        """
        pass

    def test_noblefamilys_id_get(self):
        """Test case for noblefamilys_id_get

        Get a single NobleFamily by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
