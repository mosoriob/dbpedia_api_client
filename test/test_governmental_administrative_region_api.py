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
from dbpedia.api.governmental_administrative_region_api import GovernmentalAdministrativeRegionApi  # noqa: E501
from dbpedia.rest import ApiException


class TestGovernmentalAdministrativeRegionApi(unittest.TestCase):
    """GovernmentalAdministrativeRegionApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.governmental_administrative_region_api.GovernmentalAdministrativeRegionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_governmentaladministrativeregions_get(self):
        """Test case for governmentaladministrativeregions_get

        List all instances of GovernmentalAdministrativeRegion  # noqa: E501
        """
        pass

    def test_governmentaladministrativeregions_id_get(self):
        """Test case for governmentaladministrativeregions_id_get

        Get a single GovernmentalAdministrativeRegion by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
