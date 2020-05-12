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
from dbpedia.api.holiday_api import HolidayApi  # noqa: E501
from dbpedia.rest import ApiException


class TestHolidayApi(unittest.TestCase):
    """HolidayApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.holiday_api.HolidayApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_holidays_get(self):
        """Test case for holidays_get

        List all instances of Holiday  # noqa: E501
        """
        pass

    def test_holidays_id_get(self):
        """Test case for holidays_id_get

        Get a single Holiday by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()