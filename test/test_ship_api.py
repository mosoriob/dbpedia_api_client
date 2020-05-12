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
from dbpedia.api.ship_api import ShipApi  # noqa: E501
from dbpedia.rest import ApiException


class TestShipApi(unittest.TestCase):
    """ShipApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.ship_api.ShipApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ships_get(self):
        """Test case for ships_get

        List all instances of Ship  # noqa: E501
        """
        pass

    def test_ships_id_get(self):
        """Test case for ships_id_get

        Get a single Ship by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
