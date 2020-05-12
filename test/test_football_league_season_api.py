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
from dbpedia.api.football_league_season_api import FootballLeagueSeasonApi  # noqa: E501
from dbpedia.rest import ApiException


class TestFootballLeagueSeasonApi(unittest.TestCase):
    """FootballLeagueSeasonApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.football_league_season_api.FootballLeagueSeasonApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_footballleagueseasons_get(self):
        """Test case for footballleagueseasons_get

        List all instances of FootballLeagueSeason  # noqa: E501
        """
        pass

    def test_footballleagueseasons_id_get(self):
        """Test case for footballleagueseasons_id_get

        Get a single FootballLeagueSeason by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
