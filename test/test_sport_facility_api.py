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
from dbpedia.api.sport_facility_api import SportFacilityApi  # noqa: E501
from dbpedia.rest import ApiException


class TestSportFacilityApi(unittest.TestCase):
    """SportFacilityApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.sport_facility_api.SportFacilityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sportfacilitys_get(self):
        """Test case for sportfacilitys_get

        List all instances of SportFacility  # noqa: E501
        """
        pass

    def test_sportfacilitys_id_get(self):
        """Test case for sportfacilitys_id_get

        Get a single SportFacility by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
