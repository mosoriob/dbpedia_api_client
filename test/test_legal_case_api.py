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
from dbpedia.api.legal_case_api import LegalCaseApi  # noqa: E501
from dbpedia.rest import ApiException


class TestLegalCaseApi(unittest.TestCase):
    """LegalCaseApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.legal_case_api.LegalCaseApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_legalcases_get(self):
        """Test case for legalcases_get

        List all instances of LegalCase  # noqa: E501
        """
        pass

    def test_legalcases_id_get(self):
        """Test case for legalcases_id_get

        Get a single LegalCase by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
