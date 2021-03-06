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
from dbpedia.api.record_office_api import RecordOfficeApi  # noqa: E501
from dbpedia.rest import ApiException


class TestRecordOfficeApi(unittest.TestCase):
    """RecordOfficeApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.record_office_api.RecordOfficeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_recordoffices_get(self):
        """Test case for recordoffices_get

        List all instances of RecordOffice  # noqa: E501
        """
        pass

    def test_recordoffices_id_get(self):
        """Test case for recordoffices_id_get

        Get a single RecordOffice by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
