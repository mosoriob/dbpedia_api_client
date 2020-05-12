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
from dbpedia.api.formula_one_racer_api import FormulaOneRacerApi  # noqa: E501
from dbpedia.rest import ApiException


class TestFormulaOneRacerApi(unittest.TestCase):
    """FormulaOneRacerApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.formula_one_racer_api.FormulaOneRacerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_formulaoneracers_get(self):
        """Test case for formulaoneracers_get

        List all instances of FormulaOneRacer  # noqa: E501
        """
        pass

    def test_formulaoneracers_id_get(self):
        """Test case for formulaoneracers_id_get

        Get a single FormulaOneRacer by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
