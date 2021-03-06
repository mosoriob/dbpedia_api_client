# coding: utf-8

"""
    DBpedia

    This is the API of the DBpedia Ontology  # noqa: E501

    The version of the OpenAPI document: v0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import dbpedia
from dbpedia.models.soccer_tournament import SoccerTournament  # noqa: E501
from dbpedia.rest import ApiException

class TestSoccerTournament(unittest.TestCase):
    """SoccerTournament unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SoccerTournament
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.soccer_tournament.SoccerTournament()  # noqa: E501
        if include_optional :
            return SoccerTournament(
                soccer_tournament_top_scorer = [
                    None
                    ], 
                number_of_people_attending = [
                    56
                    ], 
                end_date = [
                    '0'
                    ], 
                soccer_tournament_opening_season = [
                    None
                    ], 
                description = [
                    '0'
                    ], 
                soccer_tournament_this_season = [
                    None
                    ], 
                soccer_tournament_most_succesfull = [
                    None
                    ], 
                type = [
                    '0'
                    ], 
                soccer_tournament_last_champion = [
                    None
                    ], 
                silver_medalist = [
                    None
                    ], 
                participant = [
                    '0'
                    ], 
                duration = [
                    1.337
                    ], 
                medalist = [
                    None
                    ], 
                previous_event = [
                    None
                    ], 
                champion_in_single_female = [
                    None
                    ], 
                champion_in_double_male = [
                    None
                    ], 
                soccer_tournament_most_steady = [
                    None
                    ], 
                id = '0', 
                following_event = [
                    None
                    ], 
                champion_in_single_male = [
                    None
                    ], 
                bronze_medalist = [
                    None
                    ], 
                champion_in_mixed_double = [
                    None
                    ], 
                soccer_tournament_closing_season = [
                    None
                    ], 
                caused_by = [
                    None
                    ], 
                label = [
                    '0'
                    ], 
                gold_medalist = [
                    None
                    ], 
                champion_in_single = [
                    None
                    ], 
                race_track = [
                    None
                    ], 
                next_event = [
                    None
                    ], 
                champion_in_double_female = [
                    None
                    ], 
                champion_in_double = [
                    None
                    ], 
                start_date = [
                    '0'
                    ], 
                champion = [
                    None
                    ]
            )
        else :
            return SoccerTournament(
        )

    def testSoccerTournament(self):
        """Test SoccerTournament"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
