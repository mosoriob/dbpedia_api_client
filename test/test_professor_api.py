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
from dbpedia.api.professor_api import ProfessorApi  # noqa: E501
from dbpedia.rest import ApiException


class TestProfessorApi(unittest.TestCase):
    """ProfessorApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.professor_api.ProfessorApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_professors_get(self):
        """Test case for professors_get

        List all instances of Professor  # noqa: E501
        """
        pass

    def test_professors_id_get(self):
        """Test case for professors_id_get

        Get a single Professor by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
