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
from dbpedia.api.contest_api import ContestApi  # noqa: E501
from dbpedia.rest import ApiException


class TestContestApi(unittest.TestCase):
    """ContestApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.contest_api.ContestApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_contests_get(self):
        """Test case for contests_get

        List all instances of Contest  # noqa: E501
        """
        pass

    def test_contests_id_get(self):
        """Test case for contests_id_get

        Get a single Contest by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
