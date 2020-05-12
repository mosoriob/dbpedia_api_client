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
from dbpedia.api.soccer_club_season_api import SoccerClubSeasonApi  # noqa: E501
from dbpedia.rest import ApiException


class TestSoccerClubSeasonApi(unittest.TestCase):
    """SoccerClubSeasonApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.soccer_club_season_api.SoccerClubSeasonApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_soccerclubseasons_get(self):
        """Test case for soccerclubseasons_get

        List all instances of SoccerClubSeason  # noqa: E501
        """
        pass

    def test_soccerclubseasons_id_get(self):
        """Test case for soccerclubseasons_id_get

        Get a single SoccerClubSeason by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
