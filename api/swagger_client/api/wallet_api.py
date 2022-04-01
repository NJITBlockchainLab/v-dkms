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


class WalletApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def wallet_did_create_post(self, **kwargs):  # noqa: E501
        """Create a local DID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wallet_did_create_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DIDResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.wallet_did_create_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.wallet_did_create_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def wallet_did_create_post_with_http_info(self, **kwargs):  # noqa: E501
        """Create a local DID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wallet_did_create_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DIDResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method wallet_did_create_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/wallet/did/create', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DIDResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def wallet_did_get(self, **kwargs):  # noqa: E501
        """List wallet DIDs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wallet_did_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str did: DID of interest
        :param str posture: Whether DID is current public DID, posted to ledger but current public DID, or local to the wallet
        :param str verkey: Verification key of interest
        :return: DIDList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.wallet_did_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.wallet_did_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def wallet_did_get_with_http_info(self, **kwargs):  # noqa: E501
        """List wallet DIDs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wallet_did_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str did: DID of interest
        :param str posture: Whether DID is current public DID, posted to ledger but current public DID, or local to the wallet
        :param str verkey: Verification key of interest
        :return: DIDList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['did', 'posture', 'verkey']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method wallet_did_get" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('did' in params and not re.search(r'^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$', params['did'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `did` when calling `wallet_did_get`, must conform to the pattern `/^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('verkey' in params and not re.search(r'^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$', params['verkey'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `verkey` when calling `wallet_did_get`, must conform to the pattern `/^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'did' in params:
            query_params.append(('did', params['did']))  # noqa: E501
        if 'posture' in params:
            query_params.append(('posture', params['posture']))  # noqa: E501
        if 'verkey' in params:
            query_params.append(('verkey', params['verkey']))  # noqa: E501

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
            '/wallet/did', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DIDList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def wallet_did_local_rotate_keypair_patch(self, did, **kwargs):  # noqa: E501
        """Rotate keypair for a DID not posted to the ledger  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wallet_did_local_rotate_keypair_patch(did, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str did: DID of interest (required)
        :return: WalletModuleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.wallet_did_local_rotate_keypair_patch_with_http_info(did, **kwargs)  # noqa: E501
        else:
            (data) = self.wallet_did_local_rotate_keypair_patch_with_http_info(did, **kwargs)  # noqa: E501
            return data

    def wallet_did_local_rotate_keypair_patch_with_http_info(self, did, **kwargs):  # noqa: E501
        """Rotate keypair for a DID not posted to the ledger  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wallet_did_local_rotate_keypair_patch_with_http_info(did, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str did: DID of interest (required)
        :return: WalletModuleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['did']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method wallet_did_local_rotate_keypair_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'did' is set
        if self.api_client.client_side_validation and ('did' not in params or
                                                       params['did'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `did` when calling `wallet_did_local_rotate_keypair_patch`")  # noqa: E501

        if self.api_client.client_side_validation and ('did' in params and not re.search(r'^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$', params['did'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `did` when calling `wallet_did_local_rotate_keypair_patch`, must conform to the pattern `/^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'did' in params:
            query_params.append(('did', params['did']))  # noqa: E501

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
            '/wallet/did/local/rotate-keypair', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WalletModuleResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def wallet_did_public_get(self, **kwargs):  # noqa: E501
        """Fetch the current public DID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wallet_did_public_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DIDResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.wallet_did_public_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.wallet_did_public_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def wallet_did_public_get_with_http_info(self, **kwargs):  # noqa: E501
        """Fetch the current public DID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wallet_did_public_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DIDResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method wallet_did_public_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/wallet/did/public', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DIDResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def wallet_did_public_post(self, did, **kwargs):  # noqa: E501
        """Assign the current public DID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wallet_did_public_post(did, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str did: DID of interest (required)
        :return: DIDResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.wallet_did_public_post_with_http_info(did, **kwargs)  # noqa: E501
        else:
            (data) = self.wallet_did_public_post_with_http_info(did, **kwargs)  # noqa: E501
            return data

    def wallet_did_public_post_with_http_info(self, did, **kwargs):  # noqa: E501
        """Assign the current public DID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wallet_did_public_post_with_http_info(did, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str did: DID of interest (required)
        :return: DIDResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['did']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method wallet_did_public_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'did' is set
        if self.api_client.client_side_validation and ('did' not in params or
                                                       params['did'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `did` when calling `wallet_did_public_post`")  # noqa: E501

        if self.api_client.client_side_validation and ('did' in params and not re.search(r'^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$', params['did'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `did` when calling `wallet_did_public_post`, must conform to the pattern `/^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'did' in params:
            query_params.append(('did', params['did']))  # noqa: E501

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
            '/wallet/did/public', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DIDResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def wallet_get_did_endpoint_get(self, did, **kwargs):  # noqa: E501
        """Query DID endpoint in wallet  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wallet_get_did_endpoint_get(did, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str did: DID of interest (required)
        :return: DIDEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.wallet_get_did_endpoint_get_with_http_info(did, **kwargs)  # noqa: E501
        else:
            (data) = self.wallet_get_did_endpoint_get_with_http_info(did, **kwargs)  # noqa: E501
            return data

    def wallet_get_did_endpoint_get_with_http_info(self, did, **kwargs):  # noqa: E501
        """Query DID endpoint in wallet  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wallet_get_did_endpoint_get_with_http_info(did, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str did: DID of interest (required)
        :return: DIDEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['did']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method wallet_get_did_endpoint_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'did' is set
        if self.api_client.client_side_validation and ('did' not in params or
                                                       params['did'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `did` when calling `wallet_get_did_endpoint_get`")  # noqa: E501

        if self.api_client.client_side_validation and ('did' in params and not re.search(r'^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$', params['did'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `did` when calling `wallet_get_did_endpoint_get`, must conform to the pattern `/^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'did' in params:
            query_params.append(('did', params['did']))  # noqa: E501

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
            '/wallet/get-did-endpoint', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DIDEndpoint',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def wallet_set_did_endpoint_post(self, **kwargs):  # noqa: E501
        """Update endpoint in wallet and on ledger if posted to it  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wallet_set_did_endpoint_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DIDEndpointWithType body:
        :return: WalletModuleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.wallet_set_did_endpoint_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.wallet_set_did_endpoint_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def wallet_set_did_endpoint_post_with_http_info(self, **kwargs):  # noqa: E501
        """Update endpoint in wallet and on ledger if posted to it  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wallet_set_did_endpoint_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DIDEndpointWithType body:
        :return: WalletModuleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method wallet_set_did_endpoint_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/wallet/set-did-endpoint', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WalletModuleResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)