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
from dbpedia.api.martial_artist_api import MartialArtistApi  # noqa: E501
from dbpedia.rest import ApiException


class TestMartialArtistApi(unittest.TestCase):
    """MartialArtistApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.martial_artist_api.MartialArtistApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_martialartists_get(self):
        """Test case for martialartists_get

        List all instances of MartialArtist  # noqa: E501
        """
        pass

    def test_martialartists_id_get(self):
        """Test case for martialartists_id_get

        Get a single MartialArtist by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
