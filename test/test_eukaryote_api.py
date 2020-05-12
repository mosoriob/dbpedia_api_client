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
from dbpedia.api.eukaryote_api import EukaryoteApi  # noqa: E501
from dbpedia.rest import ApiException


class TestEukaryoteApi(unittest.TestCase):
    """EukaryoteApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.eukaryote_api.EukaryoteApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_eukaryotes_get(self):
        """Test case for eukaryotes_get

        List all instances of Eukaryote  # noqa: E501
        """
        pass

    def test_eukaryotes_id_get(self):
        """Test case for eukaryotes_id_get

        Get a single Eukaryote by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()