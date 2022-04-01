# swagger_client.BasicmessageApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connections_conn_id_send_message_post**](BasicmessageApi.md#connections_conn_id_send_message_post) | **POST** /connections/{conn_id}/send-message | Send a basic message to a connection


# **connections_conn_id_send_message_post**
> BasicMessageModuleResponse connections_conn_id_send_message_post(conn_id, body=body)

Send a basic message to a connection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BasicmessageApi()
conn_id = 'conn_id_example' # str | Connection identifier
body = swagger_client.SendMessage() # SendMessage |  (optional)

try:
    # Send a basic message to a connection
    api_response = api_instance.connections_conn_id_send_message_post(conn_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasicmessageApi->connections_conn_id_send_message_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier | 
 **body** | [**SendMessage**](SendMessage.md)|  | [optional] 

### Return type

[**BasicMessageModuleResponse**](BasicMessageModuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

