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
from dbpedia.api.water_ride_api import WaterRideApi  # noqa: E501
from dbpedia.rest import ApiException


class TestWaterRideApi(unittest.TestCase):
    """WaterRideApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.water_ride_api.WaterRideApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_waterrides_get(self):
        """Test case for waterrides_get

        List all instances of WaterRide  # noqa: E501
        """
        pass

    def test_waterrides_id_get(self):
        """Test case for waterrides_id_get

        Get a single WaterRide by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
