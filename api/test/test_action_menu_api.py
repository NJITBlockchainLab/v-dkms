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
from swagger_client.api.action_menu_api import ActionMenuApi  # noqa: E501
from swagger_client.rest import ApiException


class TestActionMenuApi(unittest.TestCase):
    """ActionMenuApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.action_menu_api.ActionMenuApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_action_menu_conn_id_close_post(self):
        """Test case for action_menu_conn_id_close_post

        Close the active menu associated with a connection  # noqa: E501
        """
        pass

    def test_action_menu_conn_id_fetch_post(self):
        """Test case for action_menu_conn_id_fetch_post

        Fetch the active menu  # noqa: E501
        """
        pass

    def test_action_menu_conn_id_perform_post(self):
        """Test case for action_menu_conn_id_perform_post

        Perform an action associated with the active menu  # noqa: E501
        """
        pass

    def test_action_menu_conn_id_request_post(self):
        """Test case for action_menu_conn_id_request_post

        Request the active menu  # noqa: E501
        """
        pass

    def test_action_menu_conn_id_send_menu_post(self):
        """Test case for action_menu_conn_id_send_menu_post

        Send an action menu to a connection  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()