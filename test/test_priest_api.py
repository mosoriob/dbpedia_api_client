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
from dbpedia.api.priest_api import PriestApi  # noqa: E501
from dbpedia.rest import ApiException


class TestPriestApi(unittest.TestCase):
    """PriestApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.priest_api.PriestApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_priests_get(self):
        """Test case for priests_get

        List all instances of Priest  # noqa: E501
        """
        pass

    def test_priests_id_get(self):
        """Test case for priests_id_get

        Get a single Priest by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
