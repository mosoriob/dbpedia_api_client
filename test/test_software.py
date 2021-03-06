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
from dbpedia.models.software import Software  # noqa: E501
from dbpedia.rest import ApiException

class TestSoftware(unittest.TestCase):
    """Software unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Software
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.software.Software()  # noqa: E501
        if include_optional :
            return Software(
                previous_work = [
                    None
                    ], 
                computing_media = [
                    None
                    ], 
                computing_platform = [
                    None
                    ], 
                translator = [
                    None
                    ], 
                programming_language = [
                    None
                    ], 
                alternative_title = [
                    '0'
                    ], 
                description = [
                    '0'
                    ], 
                subsequent_work = [
                    None
                    ], 
                chief_editor = [
                    None
                    ], 
                frequently_updated = [
                    '0'
                    ], 
                aspect_ratio = [
                    None
                    ], 
                music_composer = [
                    None
                    ], 
                type = [
                    '0'
                    ], 
                operating_system = [
                    None
                    ], 
                resolution = [
                    None
                    ], 
                main_character = [
                    None
                    ], 
                id = '0', 
                latest_release_version = [
                    '0'
                    ], 
                latest_release_date = [
                    '0'
                    ], 
                based_on = [
                    None
                    ], 
                latest_preview_version = [
                    '0'
                    ], 
                release_date = [
                    '0'
                    ], 
                composer = [
                    None
                    ], 
                author = [
                    None
                    ], 
                runtime = [
                    None
                    ], 
                cpu = [
                    None
                    ], 
                production_company = [
                    None
                    ], 
                label = [
                    '0'
                    ], 
                computing_input = [
                    None
                    ], 
                original_language = [
                    None
                    ], 
                latest_preview_date = [
                    '0'
                    ], 
                license = [
                    None
                    ], 
                subject_term = [
                    '0'
                    ], 
                file_size = [
                    None
                    ], 
                original_title = [
                    '0'
                    ], 
                producer = [
                    None
                    ], 
                starring = [
                    None
                    ], 
                completion_date = [
                    '0'
                    ], 
                writer = [
                    None
                    ]
            )
        else :
            return Software(
        )

    def testSoftware(self):
        """Test Software"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
