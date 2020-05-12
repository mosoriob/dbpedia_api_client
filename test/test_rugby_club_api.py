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
from dbpedia.api.rugby_club_api import RugbyClubApi  # noqa: E501
from dbpedia.rest import ApiException


class TestRugbyClubApi(unittest.TestCase):
    """RugbyClubApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.rugby_club_api.RugbyClubApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_rugbyclubs_get(self):
        """Test case for rugbyclubs_get

        List all instances of RugbyClub  # noqa: E501
        """
        pass

    def test_rugbyclubs_id_get(self):
        """Test case for rugbyclubs_id_get

        Get a single RugbyClub by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()