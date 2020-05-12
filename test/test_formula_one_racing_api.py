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
from dbpedia.api.formula_one_racing_api import FormulaOneRacingApi  # noqa: E501
from dbpedia.rest import ApiException


class TestFormulaOneRacingApi(unittest.TestCase):
    """FormulaOneRacingApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.formula_one_racing_api.FormulaOneRacingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_formulaoneracings_get(self):
        """Test case for formulaoneracings_get

        List all instances of FormulaOneRacing  # noqa: E501
        """
        pass

    def test_formulaoneracings_id_get(self):
        """Test case for formulaoneracings_id_get

        Get a single FormulaOneRacing by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
