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
from dbpedia.api.gaelic_games_player_api import GaelicGamesPlayerApi  # noqa: E501
from dbpedia.rest import ApiException


class TestGaelicGamesPlayerApi(unittest.TestCase):
    """GaelicGamesPlayerApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.gaelic_games_player_api.GaelicGamesPlayerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_gaelicgamesplayers_get(self):
        """Test case for gaelicgamesplayers_get

        List all instances of GaelicGamesPlayer  # noqa: E501
        """
        pass

    def test_gaelicgamesplayers_id_get(self):
        """Test case for gaelicgamesplayers_id_get

        Get a single GaelicGamesPlayer by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()