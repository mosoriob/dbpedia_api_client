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
from dbpedia.api.album_api import AlbumApi  # noqa: E501
from dbpedia.rest import ApiException


class TestAlbumApi(unittest.TestCase):
    """AlbumApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.album_api.AlbumApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_albums_get(self):
        """Test case for albums_get

        List all instances of Album  # noqa: E501
        """
        pass

    def test_albums_id_get(self):
        """Test case for albums_id_get

        Get a single Album by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
