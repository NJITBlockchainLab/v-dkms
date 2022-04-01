# swagger_client.TrustpingApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connections_conn_id_send_ping_post**](TrustpingApi.md#connections_conn_id_send_ping_post) | **POST** /connections/{conn_id}/send-ping | Send a trust ping to a connection


# **connections_conn_id_send_ping_post**
> PingRequestResponse connections_conn_id_send_ping_post(conn_id, body=body)

Send a trust ping to a connection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TrustpingApi()
conn_id = 'conn_id_example' # str | Connection identifier
body = swagger_client.PingRequest() # PingRequest |  (optional)

try:
    # Send a trust ping to a connection
    api_response = api_instance.connections_conn_id_send_ping_post(conn_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrustpingApi->connections_conn_id_send_ping_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier | 
 **body** | [**PingRequest**](PingRequest.md)|  | [optional] 

### Return type

[**PingRequestResponse**](PingRequestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

