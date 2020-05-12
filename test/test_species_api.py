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
from dbpedia.api.species_api import SpeciesApi  # noqa: E501
from dbpedia.rest import ApiException


class TestSpeciesApi(unittest.TestCase):
    """SpeciesApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.species_api.SpeciesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_speciess_get(self):
        """Test case for speciess_get

        List all instances of Species  # noqa: E501
        """
        pass

    def test_speciess_id_get(self):
        """Test case for speciess_id_get

        Get a single Species by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
