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
from dbpedia.api.cricket_team_api import CricketTeamApi  # noqa: E501
from dbpedia.rest import ApiException


class TestCricketTeamApi(unittest.TestCase):
    """CricketTeamApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.cricket_team_api.CricketTeamApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cricketteams_get(self):
        """Test case for cricketteams_get

        List all instances of CricketTeam  # noqa: E501
        """
        pass

    def test_cricketteams_id_get(self):
        """Test case for cricketteams_id_get

        Get a single CricketTeam by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
