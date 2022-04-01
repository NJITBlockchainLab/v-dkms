# swagger_client.DidExchangeApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**didexchange_conn_id_accept_invitation_post**](DidExchangeApi.md#didexchange_conn_id_accept_invitation_post) | **POST** /didexchange/{conn_id}/accept-invitation | Accept a stored connection invitation
[**didexchange_conn_id_accept_request_post**](DidExchangeApi.md#didexchange_conn_id_accept_request_post) | **POST** /didexchange/{conn_id}/accept-request | Accept a stored connection request
[**didexchange_create_request_post**](DidExchangeApi.md#didexchange_create_request_post) | **POST** /didexchange/create-request | Create request against public DID&#39;s implicit invitation
[**didexchange_receive_request_post**](DidExchangeApi.md#didexchange_receive_request_post) | **POST** /didexchange/receive-request | Receive request against public DID&#39;s implicit invitation


# **didexchange_conn_id_accept_invitation_post**
> ConnRecord didexchange_conn_id_accept_invitation_post(conn_id, my_endpoint=my_endpoint, my_label=my_label)

Accept a stored connection invitation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DidExchangeApi()
conn_id = 'conn_id_example' # str | Connection identifier
my_endpoint = 'my_endpoint_example' # str | My URL endpoint (optional)
my_label = 'my_label_example' # str | Label for connection request (optional)

try:
    # Accept a stored connection invitation
    api_response = api_instance.didexchange_conn_id_accept_invitation_post(conn_id, my_endpoint=my_endpoint, my_label=my_label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DidExchangeApi->didexchange_conn_id_accept_invitation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier | 
 **my_endpoint** | **str**| My URL endpoint | [optional] 
 **my_label** | **str**| Label for connection request | [optional] 

### Return type

[**ConnRecord**](ConnRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **didexchange_conn_id_accept_request_post**
> ConnRecord didexchange_conn_id_accept_request_post(conn_id, mediation_id=mediation_id, my_endpoint=my_endpoint)

Accept a stored connection request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DidExchangeApi()
conn_id = 'conn_id_example' # str | Connection identifier
mediation_id = 'mediation_id_example' # str | Identifier for active mediation record to be used (optional)
my_endpoint = 'my_endpoint_example' # str | My URL endpoint (optional)

try:
    # Accept a stored connection request
    api_response = api_instance.didexchange_conn_id_accept_request_post(conn_id, mediation_id=mediation_id, my_endpoint=my_endpoint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DidExchangeApi->didexchange_conn_id_accept_request_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier | 
 **mediation_id** | **str**| Identifier for active mediation record to be used | [optional] 
 **my_endpoint** | **str**| My URL endpoint | [optional] 

### Return type

[**ConnRecord**](ConnRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **didexchange_create_request_post**
> DIDXRequest didexchange_create_request_post(their_public_did, mediation_id=mediation_id, my_endpoint=my_endpoint, my_label=my_label)

Create request against public DID's implicit invitation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DidExchangeApi()
their_public_did = 'their_public_did_example' # str | Public DID to which to request connection
mediation_id = 'mediation_id_example' # str | Identifier for active mediation record to be used (optional)
my_endpoint = 'my_endpoint_example' # str | My URL endpoint (optional)
my_label = 'my_label_example' # str | Label for connection request (optional)

try:
    # Create request against public DID's implicit invitation
    api_response = api_instance.didexchange_create_request_post(their_public_did, mediation_id=mediation_id, my_endpoint=my_endpoint, my_label=my_label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DidExchangeApi->didexchange_create_request_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **their_public_did** | **str**| Public DID to which to request connection | 
 **mediation_id** | **str**| Identifier for active mediation record to be used | [optional] 
 **my_endpoint** | **str**| My URL endpoint | [optional] 
 **my_label** | **str**| Label for connection request | [optional] 

### Return type

[**DIDXRequest**](DIDXRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **didexchange_receive_request_post**
> ConnRecord didexchange_receive_request_post(body=body, alias=alias, auto_accept=auto_accept, mediation_id=mediation_id, my_endpoint=my_endpoint)

Receive request against public DID's implicit invitation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DidExchangeApi()
body = swagger_client.DIDXRequest() # DIDXRequest |  (optional)
alias = 'alias_example' # str | Alias for connection (optional)
auto_accept = true # bool | Auto-accept connection (defaults to configuration) (optional)
mediation_id = 'mediation_id_example' # str | Identifier for active mediation record to be used (optional)
my_endpoint = 'my_endpoint_example' # str | My URL endpoint (optional)

try:
    # Receive request against public DID's implicit invitation
    api_response = api_instance.didexchange_receive_request_post(body=body, alias=alias, auto_accept=auto_accept, mediation_id=mediation_id, my_endpoint=my_endpoint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DidExchangeApi->didexchange_receive_request_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DIDXRequest**](DIDXRequest.md)|  | [optional] 
 **alias** | **str**| Alias for connection | [optional] 
 **auto_accept** | **bool**| Auto-accept connection (defaults to configuration) | [optional] 
 **mediation_id** | **str**| Identifier for active mediation record to be used | [optional] 
 **my_endpoint** | **str**| My URL endpoint | [optional] 

### Return type

[**ConnRecord**](ConnRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

