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
from dbpedia.api.airport_api import AirportApi  # noqa: E501
from dbpedia.rest import ApiException


class TestAirportApi(unittest.TestCase):
    """AirportApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.airport_api.AirportApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_airports_get(self):
        """Test case for airports_get

        List all instances of Airport  # noqa: E501
        """
        pass

    def test_airports_id_get(self):
        """Test case for airports_id_get

        Get a single Airport by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
