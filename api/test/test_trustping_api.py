# coding: utf-8

"""
    sp

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v0.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.trustping_api import TrustpingApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTrustpingApi(unittest.TestCase):
    """TrustpingApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.trustping_api.TrustpingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_connections_conn_id_send_ping_post(self):
        """Test case for connections_conn_id_send_ping_post

        Send a trust ping to a connection  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
