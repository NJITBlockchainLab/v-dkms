# swagger_client.ActionMenuApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**action_menu_conn_id_close_post**](ActionMenuApi.md#action_menu_conn_id_close_post) | **POST** /action-menu/{conn_id}/close | Close the active menu associated with a connection
[**action_menu_conn_id_fetch_post**](ActionMenuApi.md#action_menu_conn_id_fetch_post) | **POST** /action-menu/{conn_id}/fetch | Fetch the active menu
[**action_menu_conn_id_perform_post**](ActionMenuApi.md#action_menu_conn_id_perform_post) | **POST** /action-menu/{conn_id}/perform | Perform an action associated with the active menu
[**action_menu_conn_id_request_post**](ActionMenuApi.md#action_menu_conn_id_request_post) | **POST** /action-menu/{conn_id}/request | Request the active menu
[**action_menu_conn_id_send_menu_post**](ActionMenuApi.md#action_menu_conn_id_send_menu_post) | **POST** /action-menu/{conn_id}/send-menu | Send an action menu to a connection


# **action_menu_conn_id_close_post**
> ActionMenuModulesResult action_menu_conn_id_close_post(conn_id)

Close the active menu associated with a connection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActionMenuApi()
conn_id = 'conn_id_example' # str | Connection identifier

try:
    # Close the active menu associated with a connection
    api_response = api_instance.action_menu_conn_id_close_post(conn_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionMenuApi->action_menu_conn_id_close_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier | 

### Return type

[**ActionMenuModulesResult**](ActionMenuModulesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_menu_conn_id_fetch_post**
> ActionMenuModulesResult action_menu_conn_id_fetch_post(conn_id)

Fetch the active menu

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActionMenuApi()
conn_id = 'conn_id_example' # str | Connection identifier

try:
    # Fetch the active menu
    api_response = api_instance.action_menu_conn_id_fetch_post(conn_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionMenuApi->action_menu_conn_id_fetch_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier | 

### Return type

[**ActionMenuModulesResult**](ActionMenuModulesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_menu_conn_id_perform_post**
> ActionMenuModulesResult action_menu_conn_id_perform_post(conn_id, body=body)

Perform an action associated with the active menu

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActionMenuApi()
conn_id = 'conn_id_example' # str | Connection identifier
body = swagger_client.PerformRequest() # PerformRequest |  (optional)

try:
    # Perform an action associated with the active menu
    api_response = api_instance.action_menu_conn_id_perform_post(conn_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionMenuApi->action_menu_conn_id_perform_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier | 
 **body** | [**PerformRequest**](PerformRequest.md)|  | [optional] 

### Return type

[**ActionMenuModulesResult**](ActionMenuModulesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_menu_conn_id_request_post**
> ActionMenuModulesResult action_menu_conn_id_request_post(conn_id)

Request the active menu

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActionMenuApi()
conn_id = 'conn_id_example' # str | Connection identifier

try:
    # Request the active menu
    api_response = api_instance.action_menu_conn_id_request_post(conn_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionMenuApi->action_menu_conn_id_request_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier | 

### Return type

[**ActionMenuModulesResult**](ActionMenuModulesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_menu_conn_id_send_menu_post**
> ActionMenuModulesResult action_menu_conn_id_send_menu_post(conn_id, body=body)

Send an action menu to a connection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActionMenuApi()
conn_id = 'conn_id_example' # str | Connection identifier
body = swagger_client.SendMenu() # SendMenu |  (optional)

try:
    # Send an action menu to a connection
    api_response = api_instance.action_menu_conn_id_send_menu_post(conn_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionMenuApi->action_menu_conn_id_send_menu_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier | 
 **body** | [**SendMenu**](SendMenu.md)|  | [optional] 

### Return type

[**ActionMenuModulesResult**](ActionMenuModulesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

