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
from dbpedia.models.ship import Ship  # noqa: E501
from dbpedia.rest import ApiException

class TestShip(unittest.TestCase):
    """Ship unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Ship
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.ship.Ship()  # noqa: E501
        if include_optional :
            return Ship(
                laying_down = [
                    '0'
                    ], 
                mass = [
                    None
                    ], 
                description = [
                    '0'
                    ], 
                engine_type = [
                    None
                    ], 
                type = [
                    '0'
                    ], 
                introduction_date = [
                    '0'
                    ], 
                ship_launch = [
                    '0'
                    ], 
                diameter = [
                    None
                    ], 
                design_company = [
                    None
                    ], 
                christening_date = [
                    '0'
                    ], 
                discharge = [
                    1.337
                    ], 
                assembly = [
                    None
                    ], 
                id = '0', 
                ship_crew = [
                    None
                    ], 
                rebuilder = [
                    None
                    ], 
                _class = [
                    None
                    ], 
                model_start_date = [
                    '0'
                    ], 
                acquirement_date = [
                    '0'
                    ], 
                height = [
                    None
                    ], 
                model_end_date = [
                    '0'
                    ], 
                number_of_launches = [
                    56
                    ], 
                model_end_year = [
                    '0'
                    ], 
                maiden_voyage = [
                    '0'
                    ], 
                length = [
                    None
                    ], 
                weight = [
                    None
                    ], 
                commissioning_date = [
                    '0'
                    ], 
                label = [
                    '0'
                    ], 
                version = [
                    None
                    ], 
                decommissioning_date = [
                    '0'
                    ], 
                recommissioning_date = [
                    '0'
                    ], 
                ship_beam = [
                    1.337
                    ], 
                number_of_seats = [
                    56
                    ], 
                homeport = [
                    None
                    ], 
                model_start_year = [
                    '0'
                    ], 
                width = [
                    None
                    ], 
                discharge_average = [
                    1.337
                    ], 
                number_of_crew = [
                    56
                    ], 
                capture_date = [
                    '0'
                    ], 
                ship_draft = [
                    1.337
                    ], 
                order_date = [
                    '0'
                    ], 
                related_mean_of_transportation = [
                    None
                    ], 
                ship_displacement = [
                    1.337
                    ], 
                power_type = [
                    None
                    ]
            )
        else :
            return Ship(
        )

    def testShip(self):
        """Test Ship"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
