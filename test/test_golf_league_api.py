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
from dbpedia.api.golf_league_api import GolfLeagueApi  # noqa: E501
from dbpedia.rest import ApiException


class TestGolfLeagueApi(unittest.TestCase):
    """GolfLeagueApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.golf_league_api.GolfLeagueApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_golfleagues_get(self):
        """Test case for golfleagues_get

        List all instances of GolfLeague  # noqa: E501
        """
        pass

    def test_golfleagues_id_get(self):
        """Test case for golfleagues_id_get

        Get a single GolfLeague by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
