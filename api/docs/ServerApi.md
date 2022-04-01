# swagger_client.ServerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**features_get**](ServerApi.md#features_get) | **GET** /features | Query supported features
[**plugins_get**](ServerApi.md#plugins_get) | **GET** /plugins | Fetch the list of loaded plugins
[**shutdown_get**](ServerApi.md#shutdown_get) | **GET** /shutdown | Shut down server
[**status_get**](ServerApi.md#status_get) | **GET** /status | Fetch the server status
[**status_live_get**](ServerApi.md#status_live_get) | **GET** /status/live | Liveliness check
[**status_ready_get**](ServerApi.md#status_ready_get) | **GET** /status/ready | Readiness check
[**status_reset_post**](ServerApi.md#status_reset_post) | **POST** /status/reset | Reset statistics


# **features_get**
> QueryResult features_get(query=query)

Query supported features

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()
query = 'query_example' # str | Query (optional)

try:
    # Query supported features
    api_response = api_instance.features_get(query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->features_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query | [optional] 

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plugins_get**
> AdminModules plugins_get()

Fetch the list of loaded plugins

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()

try:
    # Fetch the list of loaded plugins
    api_response = api_instance.plugins_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->plugins_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminModules**](AdminModules.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shutdown_get**
> AdminShutdown shutdown_get()

Shut down server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()

try:
    # Shut down server
    api_response = api_instance.shutdown_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->shutdown_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminShutdown**](AdminShutdown.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_get**
> AdminStatus status_get()

Fetch the server status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()

try:
    # Fetch the server status
    api_response = api_instance.status_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->status_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminStatus**](AdminStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_live_get**
> AdminStatusLiveliness status_live_get()

Liveliness check

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()

try:
    # Liveliness check
    api_response = api_instance.status_live_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->status_live_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminStatusLiveliness**](AdminStatusLiveliness.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_ready_get**
> AdminStatusReadiness status_ready_get()

Readiness check

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()

try:
    # Readiness check
    api_response = api_instance.status_ready_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->status_ready_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminStatusReadiness**](AdminStatusReadiness.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_reset_post**
> AdminStatus status_reset_post()

Reset statistics

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()

try:
    # Reset statistics
    api_response = api_instance.status_reset_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->status_reset_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminStatus**](AdminStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

