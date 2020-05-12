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
from dbpedia.models.celestial_body import CelestialBody  # noqa: E501
from dbpedia.rest import ApiException

class TestCelestialBody(unittest.TestCase):
    """CelestialBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CelestialBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.celestial_body.CelestialBody()  # noqa: E501
        if include_optional :
            return CelestialBody(
                periapsis = [
                    1.337
                    ], 
                absolute_magnitude = [
                    1.337
                    ], 
                orbital_eccentricity = [
                    1.337
                    ], 
                description = [
                    '0'
                    ], 
                label = [
                    '0'
                    ], 
                type = [
                    '0'
                    ], 
                max_absolute_magnitude = [
                    1.337
                    ], 
                apoapsis = [
                    1.337
                    ], 
                von_klitzing_constant = [
                    1.337
                    ], 
                messier_name = [
                    '0'
                    ], 
                max_apparent_magnitude = [
                    1.337
                    ], 
                id = '0', 
                ngc_name = [
                    '0'
                    ]
            )
        else :
            return CelestialBody(
        )

    def testCelestialBody(self):
        """Test CelestialBody"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
