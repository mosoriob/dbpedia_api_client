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
from dbpedia.models.still_image import StillImage  # noqa: E501
from dbpedia.rest import ApiException

class TestStillImage(unittest.TestCase):
    """StillImage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StillImage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.still_image.StillImage()  # noqa: E501
        if include_optional :
            return StillImage(
                previous_work = [
                    None
                    ], 
                date_last_updated = [
                    '0'
                    ], 
                document_number = [
                    '0'
                    ], 
                translator = [
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
                music_composer = [
                    None
                    ], 
                type = [
                    '0'
                    ], 
                main_character = [
                    None
                    ], 
                has_national_archives_identifier = [
                    '0'
                    ], 
                id = '0', 
                based_on = [
                    None
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
                production_company = [
                    None
                    ], 
                label = [
                    '0'
                    ], 
                original_language = [
                    None
                    ], 
                license = [
                    None
                    ], 
                subject_term = [
                    '0'
                    ], 
                registry_number = [
                    '0'
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
            return StillImage(
        )

    def testStillImage(self):
        """Test StillImage"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
