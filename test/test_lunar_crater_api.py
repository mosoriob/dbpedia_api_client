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
from dbpedia.api.lunar_crater_api import LunarCraterApi  # noqa: E501
from dbpedia.rest import ApiException


class TestLunarCraterApi(unittest.TestCase):
    """LunarCraterApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.lunar_crater_api.LunarCraterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_lunarcraters_get(self):
        """Test case for lunarcraters_get

        List all instances of LunarCrater  # noqa: E501
        """
        pass

    def test_lunarcraters_id_get(self):
        """Test case for lunarcraters_id_get

        Get a single LunarCrater by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
