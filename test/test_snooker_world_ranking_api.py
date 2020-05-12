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
from dbpedia.api.snooker_world_ranking_api import SnookerWorldRankingApi  # noqa: E501
from dbpedia.rest import ApiException


class TestSnookerWorldRankingApi(unittest.TestCase):
    """SnookerWorldRankingApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.snooker_world_ranking_api.SnookerWorldRankingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_snookerworldrankings_get(self):
        """Test case for snookerworldrankings_get

        List all instances of SnookerWorldRanking  # noqa: E501
        """
        pass

    def test_snookerworldrankings_id_get(self):
        """Test case for snookerworldrankings_id_get

        Get a single SnookerWorldRanking by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
