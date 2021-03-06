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
from dbpedia.models.disease import Disease  # noqa: E501
from dbpedia.rest import ApiException

class TestDisease(unittest.TestCase):
    """Disease unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Disease
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.disease.Disease()  # noqa: E501
        if include_optional :
            return Disease(
                genereviewsname = [
                    '0'
                    ], 
                medlineplus = [
                    '0'
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
                mesh_id = [
                    '0'
                    ], 
                genereviewsid = [
                    '0'
                    ], 
                emedicine_topic = [
                    '0'
                    ], 
                icdo = [
                    '0'
                    ], 
                emedicine_subject = [
                    '0'
                    ], 
                id = '0', 
                diseasesdb = [
                    '0'
                    ], 
                icd9 = [
                    '0'
                    ], 
                icd10 = [
                    '0'
                    ]
            )
        else :
            return Disease(
        )

    def testDisease(self):
        """Test Disease"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
