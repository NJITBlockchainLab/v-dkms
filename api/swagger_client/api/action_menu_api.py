# coding: utf-8

"""
    sp

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v0.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ActionMenuApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def action_menu_conn_id_close_post(self, conn_id, **kwargs):  # noqa: E501
        """Close the active menu associated with a connection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_menu_conn_id_close_post(conn_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str conn_id: Connection identifier (required)
        :return: ActionMenuModulesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.action_menu_conn_id_close_post_with_http_info(conn_id, **kwargs)  # noqa: E501
        else:
            (data) = self.action_menu_conn_id_close_post_with_http_info(conn_id, **kwargs)  # noqa: E501
            return data

    def action_menu_conn_id_close_post_with_http_info(self, conn_id, **kwargs):  # noqa: E501
        """Close the active menu associated with a connection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_menu_conn_id_close_post_with_http_info(conn_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str conn_id: Connection identifier (required)
        :return: ActionMenuModulesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conn_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method action_menu_conn_id_close_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'conn_id' is set
        if self.api_client.client_side_validation and ('conn_id' not in params or
                                                       params['conn_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `conn_id` when calling `action_menu_conn_id_close_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'conn_id' in params:
            path_params['conn_id'] = params['conn_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/action-menu/{conn_id}/close', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActionMenuModulesResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def action_menu_conn_id_fetch_post(self, conn_id, **kwargs):  # noqa: E501
        """Fetch the active menu  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_menu_conn_id_fetch_post(conn_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str conn_id: Connection identifier (required)
        :return: ActionMenuModulesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.action_menu_conn_id_fetch_post_with_http_info(conn_id, **kwargs)  # noqa: E501
        else:
            (data) = self.action_menu_conn_id_fetch_post_with_http_info(conn_id, **kwargs)  # noqa: E501
            return data

    def action_menu_conn_id_fetch_post_with_http_info(self, conn_id, **kwargs):  # noqa: E501
        """Fetch the active menu  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_menu_conn_id_fetch_post_with_http_info(conn_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str conn_id: Connection identifier (required)
        :return: ActionMenuModulesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conn_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method action_menu_conn_id_fetch_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'conn_id' is set
        if self.api_client.client_side_validation and ('conn_id' not in params or
                                                       params['conn_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `conn_id` when calling `action_menu_conn_id_fetch_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'conn_id' in params:
            path_params['conn_id'] = params['conn_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/action-menu/{conn_id}/fetch', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActionMenuModulesResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def action_menu_conn_id_perform_post(self, conn_id, **kwargs):  # noqa: E501
        """Perform an action associated with the active menu  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_menu_conn_id_perform_post(conn_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str conn_id: Connection identifier (required)
        :param PerformRequest body:
        :return: ActionMenuModulesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.action_menu_conn_id_perform_post_with_http_info(conn_id, **kwargs)  # noqa: E501
        else:
            (data) = self.action_menu_conn_id_perform_post_with_http_info(conn_id, **kwargs)  # noqa: E501
            return data

    def action_menu_conn_id_perform_post_with_http_info(self, conn_id, **kwargs):  # noqa: E501
        """Perform an action associated with the active menu  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_menu_conn_id_perform_post_with_http_info(conn_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str conn_id: Connection identifier (required)
        :param PerformRequest body:
        :return: ActionMenuModulesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conn_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method action_menu_conn_id_perform_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'conn_id' is set
        if self.api_client.client_side_validation and ('conn_id' not in params or
                                                       params['conn_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `conn_id` when calling `action_menu_conn_id_perform_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'conn_id' in params:
            path_params['conn_id'] = params['conn_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/action-menu/{conn_id}/perform', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActionMenuModulesResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def action_menu_conn_id_request_post(self, conn_id, **kwargs):  # noqa: E501
        """Request the active menu  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_menu_conn_id_request_post(conn_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str conn_id: Connection identifier (required)
        :return: ActionMenuModulesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.action_menu_conn_id_request_post_with_http_info(conn_id, **kwargs)  # noqa: E501
        else:
            (data) = self.action_menu_conn_id_request_post_with_http_info(conn_id, **kwargs)  # noqa: E501
            return data

    def action_menu_conn_id_request_post_with_http_info(self, conn_id, **kwargs):  # noqa: E501
        """Request the active menu  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_menu_conn_id_request_post_with_http_info(conn_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str conn_id: Connection identifier (required)
        :return: ActionMenuModulesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conn_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method action_menu_conn_id_request_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'conn_id' is set
        if self.api_client.client_side_validation and ('conn_id' not in params or
                                                       params['conn_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `conn_id` when calling `action_menu_conn_id_request_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'conn_id' in params:
            path_params['conn_id'] = params['conn_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/action-menu/{conn_id}/request', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActionMenuModulesResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def action_menu_conn_id_send_menu_post(self, conn_id, **kwargs):  # noqa: E501
        """Send an action menu to a connection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_menu_conn_id_send_menu_post(conn_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str conn_id: Connection identifier (required)
        :param SendMenu body:
        :return: ActionMenuModulesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.action_menu_conn_id_send_menu_post_with_http_info(conn_id, **kwargs)  # noqa: E501
        else:
            (data) = self.action_menu_conn_id_send_menu_post_with_http_info(conn_id, **kwargs)  # noqa: E501
            return data

    def action_menu_conn_id_send_menu_post_with_http_info(self, conn_id, **kwargs):  # noqa: E501
        """Send an action menu to a connection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_menu_conn_id_send_menu_post_with_http_info(conn_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str conn_id: Connection identifier (required)
        :param SendMenu body:
        :return: ActionMenuModulesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conn_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method action_menu_conn_id_send_menu_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'conn_id' is set
        if self.api_client.client_side_validation and ('conn_id' not in params or
                                                       params['conn_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `conn_id` when calling `action_menu_conn_id_send_menu_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'conn_id' in params:
            path_params['conn_id'] = params['conn_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/action-menu/{conn_id}/send-menu', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActionMenuModulesResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
