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
from dbpedia.api.amusement_park_attraction_api import AmusementParkAttractionApi  # noqa: E501
from dbpedia.rest import ApiException


class TestAmusementParkAttractionApi(unittest.TestCase):
    """AmusementParkAttractionApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.amusement_park_attraction_api.AmusementParkAttractionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_amusementparkattractions_get(self):
        """Test case for amusementparkattractions_get

        List all instances of AmusementParkAttraction  # noqa: E501
        """
        pass

    def test_amusementparkattractions_id_get(self):
        """Test case for amusementparkattractions_id_get

        Get a single AmusementParkAttraction by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
