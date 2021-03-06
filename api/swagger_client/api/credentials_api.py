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


class CredentialsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def credential_credential_id_delete(self, credential_id, **kwargs):  # noqa: E501
        """Remove a credential from the wallet by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.credential_credential_id_delete(credential_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credential_id: Credential identifier (required)
        :return: HolderModuleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.credential_credential_id_delete_with_http_info(credential_id, **kwargs)  # noqa: E501
        else:
            (data) = self.credential_credential_id_delete_with_http_info(credential_id, **kwargs)  # noqa: E501
            return data

    def credential_credential_id_delete_with_http_info(self, credential_id, **kwargs):  # noqa: E501
        """Remove a credential from the wallet by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.credential_credential_id_delete_with_http_info(credential_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credential_id: Credential identifier (required)
        :return: HolderModuleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credential_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method credential_credential_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'credential_id' is set
        if self.api_client.client_side_validation and ('credential_id' not in params or
                                                       params['credential_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `credential_id` when calling `credential_credential_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'credential_id' in params:
            path_params['credential_id'] = params['credential_id']  # noqa: E501

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
            '/credential/{credential_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HolderModuleResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def credential_credential_id_get(self, credential_id, **kwargs):  # noqa: E501
        """Fetch a credential from wallet by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.credential_credential_id_get(credential_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credential_id: Credential identifier (required)
        :return: CredBrief
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.credential_credential_id_get_with_http_info(credential_id, **kwargs)  # noqa: E501
        else:
            (data) = self.credential_credential_id_get_with_http_info(credential_id, **kwargs)  # noqa: E501
            return data

    def credential_credential_id_get_with_http_info(self, credential_id, **kwargs):  # noqa: E501
        """Fetch a credential from wallet by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.credential_credential_id_get_with_http_info(credential_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credential_id: Credential identifier (required)
        :return: CredBrief
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credential_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method credential_credential_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'credential_id' is set
        if self.api_client.client_side_validation and ('credential_id' not in params or
                                                       params['credential_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `credential_id` when calling `credential_credential_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'credential_id' in params:
            path_params['credential_id'] = params['credential_id']  # noqa: E501

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
            '/credential/{credential_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CredBrief',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def credential_mime_types_credential_id_get(self, credential_id, **kwargs):  # noqa: E501
        """Get attribute MIME types from wallet  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.credential_mime_types_credential_id_get(credential_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credential_id: Credential identifier (required)
        :return: AttributeMimeTypesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.credential_mime_types_credential_id_get_with_http_info(credential_id, **kwargs)  # noqa: E501
        else:
            (data) = self.credential_mime_types_credential_id_get_with_http_info(credential_id, **kwargs)  # noqa: E501
            return data

    def credential_mime_types_credential_id_get_with_http_info(self, credential_id, **kwargs):  # noqa: E501
        """Get attribute MIME types from wallet  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.credential_mime_types_credential_id_get_with_http_info(credential_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credential_id: Credential identifier (required)
        :return: AttributeMimeTypesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credential_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method credential_mime_types_credential_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'credential_id' is set
        if self.api_client.client_side_validation and ('credential_id' not in params or
                                                       params['credential_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `credential_id` when calling `credential_mime_types_credential_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'credential_id' in params:
            path_params['credential_id'] = params['credential_id']  # noqa: E501

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
            '/credential/mime-types/{credential_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AttributeMimeTypesResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def credential_revoked_credential_id_get(self, credential_id, **kwargs):  # noqa: E501
        """Query credential revocation status by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.credential_revoked_credential_id_get(credential_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credential_id: Credential identifier (required)
        :param str _from: Earliest epoch of revocation status interval of interest
        :param str to: Latest epoch of revocation status interval of interest
        :return: CredRevokedResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.credential_revoked_credential_id_get_with_http_info(credential_id, **kwargs)  # noqa: E501
        else:
            (data) = self.credential_revoked_credential_id_get_with_http_info(credential_id, **kwargs)  # noqa: E501
            return data

    def credential_revoked_credential_id_get_with_http_info(self, credential_id, **kwargs):  # noqa: E501
        """Query credential revocation status by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.credential_revoked_credential_id_get_with_http_info(credential_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credential_id: Credential identifier (required)
        :param str _from: Earliest epoch of revocation status interval of interest
        :param str to: Latest epoch of revocation status interval of interest
        :return: CredRevokedResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credential_id', '_from', 'to']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method credential_revoked_credential_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'credential_id' is set
        if self.api_client.client_side_validation and ('credential_id' not in params or
                                                       params['credential_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `credential_id` when calling `credential_revoked_credential_id_get`")  # noqa: E501

        if self.api_client.client_side_validation and ('_from' in params and not re.search(r'^[0-9]*$', params['_from'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `_from` when calling `credential_revoked_credential_id_get`, must conform to the pattern `/^[0-9]*$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('to' in params and not re.search(r'^[0-9]*$', params['to'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `to` when calling `credential_revoked_credential_id_get`, must conform to the pattern `/^[0-9]*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'credential_id' in params:
            path_params['credential_id'] = params['credential_id']  # noqa: E501

        query_params = []
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501

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
            '/credential/revoked/{credential_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CredRevokedResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def credentials_get(self, **kwargs):  # noqa: E501
        """Fetch credentials from wallet  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.credentials_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str count: Maximum number to retrieve
        :param str start: Start index
        :param str wql: (JSON) WQL query
        :return: CredBriefList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.credentials_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.credentials_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def credentials_get_with_http_info(self, **kwargs):  # noqa: E501
        """Fetch credentials from wallet  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.credentials_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str count: Maximum number to retrieve
        :param str start: Start index
        :param str wql: (JSON) WQL query
        :return: CredBriefList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['count', 'start', 'wql']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method credentials_get" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('count' in params and not re.search(r'^[1-9][0-9]*$', params['count'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `count` when calling `credentials_get`, must conform to the pattern `/^[1-9][0-9]*$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('start' in params and not re.search(r'^[0-9]*$', params['start'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `start` when calling `credentials_get`, must conform to the pattern `/^[0-9]*$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('wql' in params and not re.search(r'^{.*}$', params['wql'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `wql` when calling `credentials_get`, must conform to the pattern `/^{.*}$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501
        if 'wql' in params:
            query_params.append(('wql', params['wql']))  # noqa: E501

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
            '/credentials', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CredBriefList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
