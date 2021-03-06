# coding: utf-8

"""
    DBpedia

    This is the API of the DBpedia Ontology  # noqa: E501

    The version of the OpenAPI document: v0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import dbpedia
from dbpedia.api.song_writer_api import SongWriterApi  # noqa: E501
from dbpedia.rest import ApiException


class TestSongWriterApi(unittest.TestCase):
    """SongWriterApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.song_writer_api.SongWriterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_songwriters_get(self):
        """Test case for songwriters_get

        List all instances of SongWriter  # noqa: E501
        """
        pass

    def test_songwriters_id_get(self):
        """Test case for songwriters_id_get

        Get a single SongWriter by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
