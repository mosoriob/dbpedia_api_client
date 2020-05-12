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
from dbpedia.models.manga import Manga  # noqa: E501
from dbpedia.rest import ApiException

class TestManga(unittest.TestCase):
    """Manga unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Manga
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.manga.Manga()  # noqa: E501
        if include_optional :
            return Manga(
                previous_work = [
                    None
                    ], 
                coden = [
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
                last_publication_date = [
                    '0'
                    ], 
                type = [
                    '0'
                    ], 
                lcc = [
                    '0'
                    ], 
                lccn = [
                    '0'
                    ], 
                main_character = [
                    None
                    ], 
                id = '0', 
                literary_genre = [
                    None
                    ], 
                based_on = [
                    None
                    ], 
                first_publisher = [
                    None
                    ], 
                first_publication_date = [
                    '0'
                    ], 
                film_version = [
                    None
                    ], 
                release_date = [
                    '0'
                    ], 
                number_of_volumes = [
                    56
                    ], 
                composer = [
                    None
                    ], 
                author = [
                    None
                    ], 
                preface_by = [
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
                original_title = [
                    '0'
                    ], 
                circulation = [
                    56
                    ], 
                oclc = [
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
                    ], 
                magazine = [
                    None
                    ]
            )
        else :
            return Manga(
        )

    def testManga(self):
        """Test Manga"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
