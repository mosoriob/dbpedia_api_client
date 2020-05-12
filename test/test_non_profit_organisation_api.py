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
from dbpedia.api.non_profit_organisation_api import NonProfitOrganisationApi  # noqa: E501
from dbpedia.rest import ApiException


class TestNonProfitOrganisationApi(unittest.TestCase):
    """NonProfitOrganisationApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.non_profit_organisation_api.NonProfitOrganisationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_non_profitorganisations_get(self):
        """Test case for non_profitorganisations_get

        List all instances of Non-ProfitOrganisation  # noqa: E501
        """
        pass

    def test_non_profitorganisations_id_get(self):
        """Test case for non_profitorganisations_id_get

        Get a single Non-ProfitOrganisation by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
