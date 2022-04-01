# swagger_client.IntroductionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connections_conn_id_start_introduction_post**](IntroductionApi.md#connections_conn_id_start_introduction_post) | **POST** /connections/{conn_id}/start-introduction | Start an introduction between two connections


# **connections_conn_id_start_introduction_post**
> IntroModuleResponse connections_conn_id_start_introduction_post(conn_id, target_connection_id, message=message)

Start an introduction between two connections

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntroductionApi()
conn_id = 'conn_id_example' # str | Connection identifier
target_connection_id = 'target_connection_id_example' # str | Target connection identifier
message = 'message_example' # str | Message (optional)

try:
    # Start an introduction between two connections
    api_response = api_instance.connections_conn_id_start_introduction_post(conn_id, target_connection_id, message=message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntroductionApi->connections_conn_id_start_introduction_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier | 
 **target_connection_id** | **str**| Target connection identifier | 
 **message** | **str**| Message | [optional] 

### Return type

[**IntroModuleResponse**](IntroModuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

