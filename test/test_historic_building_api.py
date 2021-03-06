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
from dbpedia.api.historic_building_api import HistoricBuildingApi  # noqa: E501
from dbpedia.rest import ApiException


class TestHistoricBuildingApi(unittest.TestCase):
    """HistoricBuildingApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.historic_building_api.HistoricBuildingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_historicbuildings_get(self):
        """Test case for historicbuildings_get

        List all instances of HistoricBuilding  # noqa: E501
        """
        pass

    def test_historicbuildings_id_get(self):
        """Test case for historicbuildings_id_get

        Get a single HistoricBuilding by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
