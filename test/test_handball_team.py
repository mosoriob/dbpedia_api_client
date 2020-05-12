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
from dbpedia.models.handball_team import HandballTeam  # noqa: E501
from dbpedia.rest import ApiException

class TestHandballTeam(unittest.TestCase):
    """HandballTeam unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test HandballTeam
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.handball_team.HandballTeam()  # noqa: E501
        if include_optional :
            return HandballTeam(
                viaf_id = [
                    '0'
                    ], 
                leader_function = [
                    None
                    ], 
                general_manager = [
                    None
                    ], 
                art_patron = [
                    None
                    ], 
                manager_season = [
                    None
                    ], 
                secretary_general = [
                    None
                    ], 
                number_of_locations = [
                    56
                    ], 
                discipline = [
                    None
                    ], 
                type = [
                    '0'
                    ], 
                revenue = [
                    1.337
                    ], 
                affiliation = [
                    None
                    ], 
                season = [
                    None
                    ], 
                id = '0', 
                nla_id = [
                    '0'
                    ], 
                chairperson = [
                    None
                    ], 
                region_served = [
                    None
                    ], 
                superintendent = [
                    None
                    ], 
                current_team_member = [
                    None
                    ], 
                formation_date = [
                    '0'
                    ], 
                number_of_employees = [
                    56
                    ], 
                extinction_date = [
                    '0'
                    ], 
                player_season = [
                    None
                    ], 
                endowment = [
                    1.337
                    ], 
                slogan = [
                    '0'
                    ], 
                regional_council = [
                    None
                    ], 
                location_city = [
                    None
                    ], 
                number_of_volunteers = [
                    56
                    ], 
                ideology = [
                    None
                    ], 
                description = [
                    '0'
                    ], 
                membership = [
                    '0'
                    ], 
                ceo = [
                    None
                    ], 
                formation_year = [
                    '0'
                    ], 
                junior_season = [
                    None
                    ], 
                current_member = [
                    None
                    ], 
                headquarter = [
                    None
                    ], 
                extinction_year = [
                    '0'
                    ], 
                child_organisation = [
                    None
                    ], 
                honours = [
                    None
                    ], 
                parent_organisation = [
                    None
                    ], 
                organisation_member = [
                    None
                    ], 
                number_of_staff = [
                    56
                    ], 
                product = [
                    None
                    ], 
                hometown = [
                    None
                    ], 
                foundation_place = [
                    None
                    ], 
                national_selection = [
                    None
                    ], 
                manager = [
                    None
                    ], 
                player_in_team = [
                    None
                    ], 
                label = [
                    '0'
                    ], 
                legal_form = [
                    None
                    ], 
                general_council = [
                    None
                    ], 
                trustee = [
                    None
                    ], 
                age = [
                    56
                    ], 
                main_organ = [
                    None
                    ]
            )
        else :
            return HandballTeam(
        )

    def testHandballTeam(self):
        """Test HandballTeam"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
