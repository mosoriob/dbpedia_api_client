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
from dbpedia.api.city_api import CityApi  # noqa: E501
from dbpedia.rest import ApiException


class TestCityApi(unittest.TestCase):
    """CityApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.city_api.CityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_citys_get(self):
        """Test case for citys_get

        List all instances of City  # noqa: E501
        """
        pass

    def test_citys_id_get(self):
        """Test case for citys_id_get

        Get a single City by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()