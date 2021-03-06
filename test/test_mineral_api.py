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
from dbpedia.api.mineral_api import MineralApi  # noqa: E501
from dbpedia.rest import ApiException


class TestMineralApi(unittest.TestCase):
    """MineralApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.mineral_api.MineralApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_minerals_get(self):
        """Test case for minerals_get

        List all instances of Mineral  # noqa: E501
        """
        pass

    def test_minerals_id_get(self):
        """Test case for minerals_id_get

        Get a single Mineral by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
