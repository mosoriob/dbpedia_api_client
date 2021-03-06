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
from dbpedia.api.club_moss_api import ClubMossApi  # noqa: E501
from dbpedia.rest import ApiException


class TestClubMossApi(unittest.TestCase):
    """ClubMossApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.club_moss_api.ClubMossApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_clubmosss_get(self):
        """Test case for clubmosss_get

        List all instances of ClubMoss  # noqa: E501
        """
        pass

    def test_clubmosss_id_get(self):
        """Test case for clubmosss_id_get

        Get a single ClubMoss by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
