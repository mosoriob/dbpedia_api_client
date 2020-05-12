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
from dbpedia.api.prefecture_api import PrefectureApi  # noqa: E501
from dbpedia.rest import ApiException


class TestPrefectureApi(unittest.TestCase):
    """PrefectureApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.prefecture_api.PrefectureApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_prefectures_get(self):
        """Test case for prefectures_get

        List all instances of Prefecture  # noqa: E501
        """
        pass

    def test_prefectures_id_get(self):
        """Test case for prefectures_id_get

        Get a single Prefecture by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
