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
from dbpedia.api.time_period_api import TimePeriodApi  # noqa: E501
from dbpedia.rest import ApiException


class TestTimePeriodApi(unittest.TestCase):
    """TimePeriodApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.time_period_api.TimePeriodApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_timeperiods_get(self):
        """Test case for timeperiods_get

        List all instances of TimePeriod  # noqa: E501
        """
        pass

    def test_timeperiods_id_get(self):
        """Test case for timeperiods_id_get

        Get a single TimePeriod by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
