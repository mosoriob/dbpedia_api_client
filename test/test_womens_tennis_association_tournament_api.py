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
from dbpedia.api.womens_tennis_association_tournament_api import WomensTennisAssociationTournamentApi  # noqa: E501
from dbpedia.rest import ApiException


class TestWomensTennisAssociationTournamentApi(unittest.TestCase):
    """WomensTennisAssociationTournamentApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.womens_tennis_association_tournament_api.WomensTennisAssociationTournamentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_womenstennisassociationtournaments_get(self):
        """Test case for womenstennisassociationtournaments_get

        List all instances of WomensTennisAssociationTournament  # noqa: E501
        """
        pass

    def test_womenstennisassociationtournaments_id_get(self):
        """Test case for womenstennisassociationtournaments_id_get

        Get a single WomensTennisAssociationTournament by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()