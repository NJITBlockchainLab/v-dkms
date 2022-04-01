# swagger_client.CredentialsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credential_credential_id_delete**](CredentialsApi.md#credential_credential_id_delete) | **DELETE** /credential/{credential_id} | Remove a credential from the wallet by id
[**credential_credential_id_get**](CredentialsApi.md#credential_credential_id_get) | **GET** /credential/{credential_id} | Fetch a credential from wallet by id
[**credential_mime_types_credential_id_get**](CredentialsApi.md#credential_mime_types_credential_id_get) | **GET** /credential/mime-types/{credential_id} | Get attribute MIME types from wallet
[**credential_revoked_credential_id_get**](CredentialsApi.md#credential_revoked_credential_id_get) | **GET** /credential/revoked/{credential_id} | Query credential revocation status by id
[**credentials_get**](CredentialsApi.md#credentials_get) | **GET** /credentials | Fetch credentials from wallet


# **credential_credential_id_delete**
> HolderModuleResponse credential_credential_id_delete(credential_id)

Remove a credential from the wallet by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CredentialsApi()
credential_id = 'credential_id_example' # str | Credential identifier

try:
    # Remove a credential from the wallet by id
    api_response = api_instance.credential_credential_id_delete(credential_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->credential_credential_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**| Credential identifier | 

### Return type

[**HolderModuleResponse**](HolderModuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credential_credential_id_get**
> CredBrief credential_credential_id_get(credential_id)

Fetch a credential from wallet by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CredentialsApi()
credential_id = 'credential_id_example' # str | Credential identifier

try:
    # Fetch a credential from wallet by id
    api_response = api_instance.credential_credential_id_get(credential_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->credential_credential_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**| Credential identifier | 

### Return type

[**CredBrief**](CredBrief.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credential_mime_types_credential_id_get**
> AttributeMimeTypesResult credential_mime_types_credential_id_get(credential_id)

Get attribute MIME types from wallet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CredentialsApi()
credential_id = 'credential_id_example' # str | Credential identifier

try:
    # Get attribute MIME types from wallet
    api_response = api_instance.credential_mime_types_credential_id_get(credential_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->credential_mime_types_credential_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**| Credential identifier | 

### Return type

[**AttributeMimeTypesResult**](AttributeMimeTypesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credential_revoked_credential_id_get**
> CredRevokedResult credential_revoked_credential_id_get(credential_id, _from=_from, to=to)

Query credential revocation status by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CredentialsApi()
credential_id = 'credential_id_example' # str | Credential identifier
_from = '_from_example' # str | Earliest epoch of revocation status interval of interest (optional)
to = 'to_example' # str | Latest epoch of revocation status interval of interest (optional)

try:
    # Query credential revocation status by id
    api_response = api_instance.credential_revoked_credential_id_get(credential_id, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->credential_revoked_credential_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**| Credential identifier | 
 **_from** | **str**| Earliest epoch of revocation status interval of interest | [optional] 
 **to** | **str**| Latest epoch of revocation status interval of interest | [optional] 

### Return type

[**CredRevokedResult**](CredRevokedResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_get**
> CredBriefList credentials_get(count=count, start=start, wql=wql)

Fetch credentials from wallet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CredentialsApi()
count = 'count_example' # str | Maximum number to retrieve (optional)
start = 'start_example' # str | Start index (optional)
wql = 'wql_example' # str | (JSON) WQL query (optional)

try:
    # Fetch credentials from wallet
    api_response = api_instance.credentials_get(count=count, start=start, wql=wql)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->credentials_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **str**| Maximum number to retrieve | [optional] 
 **start** | **str**| Start index | [optional] 
 **wql** | **str**| (JSON) WQL query | [optional] 

### Return type

[**CredBriefList**](CredBriefList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

