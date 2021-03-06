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
from dbpedia.api.judge_api import JudgeApi  # noqa: E501
from dbpedia.rest import ApiException


class TestJudgeApi(unittest.TestCase):
    """JudgeApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.judge_api.JudgeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_judges_get(self):
        """Test case for judges_get

        List all instances of Judge  # noqa: E501
        """
        pass

    def test_judges_id_get(self):
        """Test case for judges_id_get

        Get a single Judge by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
