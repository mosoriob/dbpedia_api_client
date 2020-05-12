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
from dbpedia.models.galaxy import Galaxy  # noqa: E501
from dbpedia.rest import ApiException

class TestGalaxy(unittest.TestCase):
    """Galaxy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Galaxy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.galaxy.Galaxy()  # noqa: E501
        if include_optional :
            return Galaxy(
                mean_radius = [
                    None
                    ], 
                cluster = [
                    None
                    ], 
                orbital_period = [
                    None
                    ], 
                surface_area = [
                    None
                    ], 
                orbital_eccentricity = [
                    1.337
                    ], 
                mass = [
                    None
                    ], 
                description = [
                    '0'
                    ], 
                type = [
                    '0'
                    ], 
                max_absolute_magnitude = [
                    1.337
                    ], 
                mean_temperature = [
                    None
                    ], 
                constellation = [
                    None
                    ], 
                von_klitzing_constant = [
                    1.337
                    ], 
                maximum_temperature = [
                    None
                    ], 
                temperature = [
                    None
                    ], 
                definition = [
                    '0'
                    ], 
                id = '0', 
                periapsis = [
                    None
                    ], 
                absolute_magnitude = [
                    1.337
                    ], 
                density = [
                    None
                    ], 
                notable_features = [
                    '0'
                    ], 
                average_speed = [
                    None
                    ], 
                label = [
                    '0'
                    ], 
                apoapsis = [
                    None
                    ], 
                volume = [
                    None
                    ], 
                messier_name = [
                    '0'
                    ], 
                max_apparent_magnitude = [
                    1.337
                    ], 
                explorer = [
                    None
                    ], 
                minimum_temperature = [
                    None
                    ], 
                ngc_name = [
                    '0'
                    ]
            )
        else :
            return Galaxy(
        )

    def testGalaxy(self):
        """Test Galaxy"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
