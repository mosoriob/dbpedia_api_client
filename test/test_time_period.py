# coding: utf-8

"""
    DBpedia

    This is the API of the DBpedia Ontology  # noqa: E501

    The version of the OpenAPI document: v0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import dbpedia
from dbpedia.models.time_period import TimePeriod  # noqa: E501
from dbpedia.rest import ApiException

class TestTimePeriod(unittest.TestCase):
    """TimePeriod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TimePeriod
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.time_period.TimePeriod()  # noqa: E501
        if include_optional :
            return TimePeriod(
                description = [
                    '0'
                    ], 
                id = '0', 
                label = [
                    '0'
                    ], 
                type = [
                    '0'
                    ]
            )
        else :
            return TimePeriod(
        )

    def testTimePeriod(self):
        """Test TimePeriod"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
