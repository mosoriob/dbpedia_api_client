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
from dbpedia.models.artery import Artery  # noqa: E501
from dbpedia.rest import ApiException

class TestArtery(unittest.TestCase):
    """Artery unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Artery
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.artery.Artery()  # noqa: E501
        if include_optional :
            return Artery(
                branch_to = [
                    None
                    ], 
                vein = [
                    None
                    ], 
                gray_page = [
                    56
                    ], 
                mesh_number = [
                    '0'
                    ], 
                organ_system = [
                    None
                    ], 
                mesh_name = [
                    '0'
                    ], 
                description = [
                    '0'
                    ], 
                label = [
                    '0'
                    ], 
                drains_to = [
                    None
                    ], 
                artery = [
                    None
                    ], 
                type = [
                    '0'
                    ], 
                branch_from = [
                    None
                    ], 
                drains_from = [
                    None
                    ], 
                lymph = [
                    None
                    ], 
                dorlands_prefix = [
                    '0'
                    ], 
                supplies = [
                    None
                    ], 
                nerve = [
                    None
                    ], 
                dorlands_suffix = [
                    '0'
                    ], 
                precursor = [
                    None
                    ], 
                id = '0', 
                gray_subject = [
                    56
                    ]
            )
        else :
            return Artery(
        )

    def testArtery(self):
        """Test Artery"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
