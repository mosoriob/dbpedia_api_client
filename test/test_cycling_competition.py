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
from dbpedia.models.cycling_competition import CyclingCompetition  # noqa: E501
from dbpedia.rest import ApiException

class TestCyclingCompetition(unittest.TestCase):
    """CyclingCompetition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CyclingCompetition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.cycling_competition.CyclingCompetition()  # noqa: E501
        if include_optional :
            return CyclingCompetition(
                number_of_people_attending = [
                    56
                    ], 
                end_date = [
                    '0'
                    ], 
                description = [
                    '0'
                    ], 
                type = [
                    '0'
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
            return CyclingCompetition(
        )

    def testCyclingCompetition(self):
        """Test CyclingCompetition"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
