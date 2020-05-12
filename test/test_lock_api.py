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
from dbpedia.api.lock_api import LockApi  # noqa: E501
from dbpedia.rest import ApiException


class TestLockApi(unittest.TestCase):
    """LockApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.lock_api.LockApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_locks_get(self):
        """Test case for locks_get

        List all instances of Lock  # noqa: E501
        """
        pass

    def test_locks_id_get(self):
        """Test case for locks_id_get

        Get a single Lock by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
