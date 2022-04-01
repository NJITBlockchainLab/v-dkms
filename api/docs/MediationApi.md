# swagger_client.MediationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mediation_default_mediator_delete**](MediationApi.md#mediation_default_mediator_delete) | **DELETE** /mediation/default-mediator | Clear default mediator
[**mediation_default_mediator_get**](MediationApi.md#mediation_default_mediator_get) | **GET** /mediation/default-mediator | Get default mediator
[**mediation_keylists_get**](MediationApi.md#mediation_keylists_get) | **GET** /mediation/keylists | Retrieve keylists by connection or role
[**mediation_keylists_mediation_id_send_keylist_query_post**](MediationApi.md#mediation_keylists_mediation_id_send_keylist_query_post) | **POST** /mediation/keylists/{mediation_id}/send-keylist-query | Send keylist query to mediator
[**mediation_keylists_mediation_id_send_keylist_update_post**](MediationApi.md#mediation_keylists_mediation_id_send_keylist_update_post) | **POST** /mediation/keylists/{mediation_id}/send-keylist-update | Send keylist update to mediator
[**mediation_mediation_id_default_mediator_put**](MediationApi.md#mediation_mediation_id_default_mediator_put) | **PUT** /mediation/{mediation_id}/default-mediator | Set default mediator
[**mediation_request_conn_id_post**](MediationApi.md#mediation_request_conn_id_post) | **POST** /mediation/request/{conn_id} | Request mediation from connection
[**mediation_requests_get**](MediationApi.md#mediation_requests_get) | **GET** /mediation/requests | Query mediation requests, returns list of all mediation records
[**mediation_requests_mediation_id_delete**](MediationApi.md#mediation_requests_mediation_id_delete) | **DELETE** /mediation/requests/{mediation_id} | Delete mediation request by ID
[**mediation_requests_mediation_id_deny_post**](MediationApi.md#mediation_requests_mediation_id_deny_post) | **POST** /mediation/requests/{mediation_id}/deny | Deny a stored mediation request
[**mediation_requests_mediation_id_get**](MediationApi.md#mediation_requests_mediation_id_get) | **GET** /mediation/requests/{mediation_id} | Retrieve mediation request record
[**mediation_requests_mediation_id_grant_post**](MediationApi.md#mediation_requests_mediation_id_grant_post) | **POST** /mediation/requests/{mediation_id}/grant | Grant received mediation


# **mediation_default_mediator_delete**
> MediationRecord mediation_default_mediator_delete()

Clear default mediator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediationApi()

try:
    # Clear default mediator
    api_response = api_instance.mediation_default_mediator_delete()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediationApi->mediation_default_mediator_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MediationRecord**](MediationRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mediation_default_mediator_get**
> MediationRecord mediation_default_mediator_get()

Get default mediator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediationApi()

try:
    # Get default mediator
    api_response = api_instance.mediation_default_mediator_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediationApi->mediation_default_mediator_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MediationRecord**](MediationRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mediation_keylists_get**
> Keylist mediation_keylists_get(conn_id=conn_id, role=role)

Retrieve keylists by connection or role

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediationApi()
conn_id = 'conn_id_example' # str | Connection identifier (optional) (optional)
role = 'server' # str | Filer on role, 'client' for keys         mediated by other agents, 'server' for keys         mediated by this agent (optional) (default to server)

try:
    # Retrieve keylists by connection or role
    api_response = api_instance.mediation_keylists_get(conn_id=conn_id, role=role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediationApi->mediation_keylists_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | [**str**](.md)| Connection identifier (optional) | [optional] 
 **role** | **str**| Filer on role, &#39;client&#39; for keys         mediated by other agents, &#39;server&#39; for keys         mediated by this agent | [optional] [default to server]

### Return type

[**Keylist**](Keylist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mediation_keylists_mediation_id_send_keylist_query_post**
> KeylistQuery mediation_keylists_mediation_id_send_keylist_query_post(mediation_id, body=body, paginate_limit=paginate_limit, paginate_offset=paginate_offset)

Send keylist query to mediator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediationApi()
mediation_id = 'mediation_id_example' # str | Mediation record identifier
body = swagger_client.KeylistQueryFilterRequest() # KeylistQueryFilterRequest |  (optional)
paginate_limit = -1 # int | limit number of results (optional) (default to -1)
paginate_offset = 0 # int | offset to use in pagination (optional) (default to 0)

try:
    # Send keylist query to mediator
    api_response = api_instance.mediation_keylists_mediation_id_send_keylist_query_post(mediation_id, body=body, paginate_limit=paginate_limit, paginate_offset=paginate_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediationApi->mediation_keylists_mediation_id_send_keylist_query_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediation_id** | [**str**](.md)| Mediation record identifier | 
 **body** | [**KeylistQueryFilterRequest**](KeylistQueryFilterRequest.md)|  | [optional] 
 **paginate_limit** | **int**| limit number of results | [optional] [default to -1]
 **paginate_offset** | **int**| offset to use in pagination | [optional] [default to 0]

### Return type

[**KeylistQuery**](KeylistQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mediation_keylists_mediation_id_send_keylist_update_post**
> KeylistUpdate mediation_keylists_mediation_id_send_keylist_update_post(mediation_id, body=body)

Send keylist update to mediator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediationApi()
mediation_id = 'mediation_id_example' # str | Mediation record identifier
body = swagger_client.KeylistUpdateRequest() # KeylistUpdateRequest |  (optional)

try:
    # Send keylist update to mediator
    api_response = api_instance.mediation_keylists_mediation_id_send_keylist_update_post(mediation_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediationApi->mediation_keylists_mediation_id_send_keylist_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediation_id** | [**str**](.md)| Mediation record identifier | 
 **body** | [**KeylistUpdateRequest**](KeylistUpdateRequest.md)|  | [optional] 

### Return type

[**KeylistUpdate**](KeylistUpdate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mediation_mediation_id_default_mediator_put**
> MediationRecord mediation_mediation_id_default_mediator_put(mediation_id)

Set default mediator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediationApi()
mediation_id = 'mediation_id_example' # str | Mediation record identifier

try:
    # Set default mediator
    api_response = api_instance.mediation_mediation_id_default_mediator_put(mediation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediationApi->mediation_mediation_id_default_mediator_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediation_id** | [**str**](.md)| Mediation record identifier | 

### Return type

[**MediationRecord**](MediationRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mediation_request_conn_id_post**
> MediationRecord mediation_request_conn_id_post(conn_id, body=body)

Request mediation from connection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediationApi()
conn_id = 'conn_id_example' # str | Connection identifier
body = swagger_client.MediationCreateRequest() # MediationCreateRequest |  (optional)

try:
    # Request mediation from connection
    api_response = api_instance.mediation_request_conn_id_post(conn_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediationApi->mediation_request_conn_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier | 
 **body** | [**MediationCreateRequest**](MediationCreateRequest.md)|  | [optional] 

### Return type

[**MediationRecord**](MediationRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mediation_requests_get**
> MediationList mediation_requests_get(conn_id=conn_id, mediator_terms=mediator_terms, recipient_terms=recipient_terms, state=state)

Query mediation requests, returns list of all mediation records

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediationApi()
conn_id = 'conn_id_example' # str | Connection identifier (optional) (optional)
mediator_terms = ['mediator_terms_example'] # list[str] | List of mediator rules for recipient (optional)
recipient_terms = ['recipient_terms_example'] # list[str] | List of recipient rules for mediation (optional)
state = 'state_example' # str | Mediation state (optional) (optional)

try:
    # Query mediation requests, returns list of all mediation records
    api_response = api_instance.mediation_requests_get(conn_id=conn_id, mediator_terms=mediator_terms, recipient_terms=recipient_terms, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediationApi->mediation_requests_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | [**str**](.md)| Connection identifier (optional) | [optional] 
 **mediator_terms** | [**list[str]**](str.md)| List of mediator rules for recipient | [optional] 
 **recipient_terms** | [**list[str]**](str.md)| List of recipient rules for mediation | [optional] 
 **state** | **str**| Mediation state (optional) | [optional] 

### Return type

[**MediationList**](MediationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mediation_requests_mediation_id_delete**
> MediationRecord mediation_requests_mediation_id_delete(mediation_id)

Delete mediation request by ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediationApi()
mediation_id = 'mediation_id_example' # str | Mediation record identifier

try:
    # Delete mediation request by ID
    api_response = api_instance.mediation_requests_mediation_id_delete(mediation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediationApi->mediation_requests_mediation_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediation_id** | [**str**](.md)| Mediation record identifier | 

### Return type

[**MediationRecord**](MediationRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mediation_requests_mediation_id_deny_post**
> MediationDeny mediation_requests_mediation_id_deny_post(mediation_id, body=body)

Deny a stored mediation request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediationApi()
mediation_id = 'mediation_id_example' # str | Mediation record identifier
body = swagger_client.AdminMediationDeny() # AdminMediationDeny |  (optional)

try:
    # Deny a stored mediation request
    api_response = api_instance.mediation_requests_mediation_id_deny_post(mediation_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediationApi->mediation_requests_mediation_id_deny_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediation_id** | [**str**](.md)| Mediation record identifier | 
 **body** | [**AdminMediationDeny**](AdminMediationDeny.md)|  | [optional] 

### Return type

[**MediationDeny**](MediationDeny.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mediation_requests_mediation_id_get**
> MediationRecord mediation_requests_mediation_id_get(mediation_id)

Retrieve mediation request record

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediationApi()
mediation_id = 'mediation_id_example' # str | Mediation record identifier

try:
    # Retrieve mediation request record
    api_response = api_instance.mediation_requests_mediation_id_get(mediation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediationApi->mediation_requests_mediation_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediation_id** | [**str**](.md)| Mediation record identifier | 

### Return type

[**MediationRecord**](MediationRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mediation_requests_mediation_id_grant_post**
> MediationGrant mediation_requests_mediation_id_grant_post(mediation_id)

Grant received mediation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediationApi()
mediation_id = 'mediation_id_example' # str | Mediation record identifier

try:
    # Grant received mediation
    api_response = api_instance.mediation_requests_mediation_id_grant_post(mediation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediationApi->mediation_requests_mediation_id_grant_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediation_id** | [**str**](.md)| Mediation record identifier | 

### Return type

[**MediationGrant**](MediationGrant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

