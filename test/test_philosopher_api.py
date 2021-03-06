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
from dbpedia.api.philosopher_api import PhilosopherApi  # noqa: E501
from dbpedia.rest import ApiException


class TestPhilosopherApi(unittest.TestCase):
    """PhilosopherApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.philosopher_api.PhilosopherApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_philosophers_get(self):
        """Test case for philosophers_get

        List all instances of Philosopher  # noqa: E501
        """
        pass

    def test_philosophers_id_get(self):
        """Test case for philosophers_id_get

        Get a single Philosopher by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
