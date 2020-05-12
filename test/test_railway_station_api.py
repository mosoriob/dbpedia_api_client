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
from dbpedia.api.railway_station_api import RailwayStationApi  # noqa: E501
from dbpedia.rest import ApiException


class TestRailwayStationApi(unittest.TestCase):
    """RailwayStationApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.railway_station_api.RailwayStationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_railwaystations_get(self):
        """Test case for railwaystations_get

        List all instances of RailwayStation  # noqa: E501
        """
        pass

    def test_railwaystations_id_get(self):
        """Test case for railwaystations_id_get

        Get a single RailwayStation by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
