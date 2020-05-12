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
from dbpedia.api.period_of_artistic_style_api import PeriodOfArtisticStyleApi  # noqa: E501
from dbpedia.rest import ApiException


class TestPeriodOfArtisticStyleApi(unittest.TestCase):
    """PeriodOfArtisticStyleApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.period_of_artistic_style_api.PeriodOfArtisticStyleApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_periodofartisticstyles_get(self):
        """Test case for periodofartisticstyles_get

        List all instances of PeriodOfArtisticStyle  # noqa: E501
        """
        pass

    def test_periodofartisticstyles_id_get(self):
        """Test case for periodofartisticstyles_id_get

        Get a single PeriodOfArtisticStyle by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()