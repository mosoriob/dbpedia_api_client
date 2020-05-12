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
from dbpedia.api.soccer_manager_api import SoccerManagerApi  # noqa: E501
from dbpedia.rest import ApiException


class TestSoccerManagerApi(unittest.TestCase):
    """SoccerManagerApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.soccer_manager_api.SoccerManagerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_soccermanagers_get(self):
        """Test case for soccermanagers_get

        List all instances of SoccerManager  # noqa: E501
        """
        pass

    def test_soccermanagers_id_get(self):
        """Test case for soccermanagers_id_get

        Get a single SoccerManager by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
