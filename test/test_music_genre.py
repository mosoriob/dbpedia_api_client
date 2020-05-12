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
from dbpedia.models.music_genre import MusicGenre  # noqa: E501
from dbpedia.rest import ApiException

class TestMusicGenre(unittest.TestCase):
    """MusicGenre unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MusicGenre
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.music_genre.MusicGenre()  # noqa: E501
        if include_optional :
            return MusicGenre(
                music_fusion_genre = [
                    None
                    ], 
                music_subgenre = [
                    None
                    ], 
                description = [
                    '0'
                    ], 
                derivative = [
                    None
                    ], 
                id = '0', 
                label = [
                    '0'
                    ], 
                type = [
                    '0'
                    ], 
                stylistic_origin = [
                    None
                    ]
            )
        else :
            return MusicGenre(
        )

    def testMusicGenre(self):
        """Test MusicGenre"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
