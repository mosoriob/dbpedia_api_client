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
from dbpedia.api.nobel_prize_api import NobelPrizeApi  # noqa: E501
from dbpedia.rest import ApiException


class TestNobelPrizeApi(unittest.TestCase):
    """NobelPrizeApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.nobel_prize_api.NobelPrizeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_nobelprizes_get(self):
        """Test case for nobelprizes_get

        List all instances of NobelPrize  # noqa: E501
        """
        pass

    def test_nobelprizes_id_get(self):
        """Test case for nobelprizes_id_get

        Get a single NobelPrize by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
