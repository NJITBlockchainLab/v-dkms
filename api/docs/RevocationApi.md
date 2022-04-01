# swagger_client.RevocationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**revocation_active_registry_cred_def_id_get**](RevocationApi.md#revocation_active_registry_cred_def_id_get) | **GET** /revocation/active-registry/{cred_def_id} | Get current active revocation registry by credential definition id
[**revocation_clear_pending_revocations_post**](RevocationApi.md#revocation_clear_pending_revocations_post) | **POST** /revocation/clear-pending-revocations | Clear pending revocations
[**revocation_create_registry_post**](RevocationApi.md#revocation_create_registry_post) | **POST** /revocation/create-registry | Creates a new revocation registry
[**revocation_credential_record_get**](RevocationApi.md#revocation_credential_record_get) | **GET** /revocation/credential-record | Get credential revocation status
[**revocation_publish_revocations_post**](RevocationApi.md#revocation_publish_revocations_post) | **POST** /revocation/publish-revocations | Publish pending revocations to ledger
[**revocation_registries_created_get**](RevocationApi.md#revocation_registries_created_get) | **GET** /revocation/registries/created | Search for matching revocation registries that current agent created
[**revocation_registry_rev_reg_id_definition_post**](RevocationApi.md#revocation_registry_rev_reg_id_definition_post) | **POST** /revocation/registry/{rev_reg_id}/definition | Send revocation registry definition to ledger
[**revocation_registry_rev_reg_id_entry_post**](RevocationApi.md#revocation_registry_rev_reg_id_entry_post) | **POST** /revocation/registry/{rev_reg_id}/entry | Send revocation registry entry to ledger
[**revocation_registry_rev_reg_id_get**](RevocationApi.md#revocation_registry_rev_reg_id_get) | **GET** /revocation/registry/{rev_reg_id} | Get revocation registry by revocation registry id
[**revocation_registry_rev_reg_id_issued_get**](RevocationApi.md#revocation_registry_rev_reg_id_issued_get) | **GET** /revocation/registry/{rev_reg_id}/issued | Get number of credentials issued against revocation registry
[**revocation_registry_rev_reg_id_patch**](RevocationApi.md#revocation_registry_rev_reg_id_patch) | **PATCH** /revocation/registry/{rev_reg_id} | Update revocation registry with new public URI to its tails file
[**revocation_registry_rev_reg_id_set_state_patch**](RevocationApi.md#revocation_registry_rev_reg_id_set_state_patch) | **PATCH** /revocation/registry/{rev_reg_id}/set-state | Set revocation registry state manually
[**revocation_registry_rev_reg_id_tails_file_get**](RevocationApi.md#revocation_registry_rev_reg_id_tails_file_get) | **GET** /revocation/registry/{rev_reg_id}/tails-file | Download tails file
[**revocation_registry_rev_reg_id_tails_file_put**](RevocationApi.md#revocation_registry_rev_reg_id_tails_file_put) | **PUT** /revocation/registry/{rev_reg_id}/tails-file | Upload local tails file to server
[**revocation_revoke_post**](RevocationApi.md#revocation_revoke_post) | **POST** /revocation/revoke | Revoke an issued credential


# **revocation_active_registry_cred_def_id_get**
> RevRegResult revocation_active_registry_cred_def_id_get(cred_def_id)

Get current active revocation registry by credential definition id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevocationApi()
cred_def_id = 'cred_def_id_example' # str | Credential definition identifier

try:
    # Get current active revocation registry by credential definition id
    api_response = api_instance.revocation_active_registry_cred_def_id_get(cred_def_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevocationApi->revocation_active_registry_cred_def_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_def_id** | **str**| Credential definition identifier | 

### Return type

[**RevRegResult**](RevRegResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revocation_clear_pending_revocations_post**
> PublishRevocations revocation_clear_pending_revocations_post(body=body)

Clear pending revocations

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevocationApi()
body = swagger_client.ClearPendingRevocationsRequest() # ClearPendingRevocationsRequest |  (optional)

try:
    # Clear pending revocations
    api_response = api_instance.revocation_clear_pending_revocations_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevocationApi->revocation_clear_pending_revocations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClearPendingRevocationsRequest**](ClearPendingRevocationsRequest.md)|  | [optional] 

### Return type

[**PublishRevocations**](PublishRevocations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revocation_create_registry_post**
> RevRegResult revocation_create_registry_post(body=body)

Creates a new revocation registry

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevocationApi()
body = swagger_client.RevRegCreateRequest() # RevRegCreateRequest |  (optional)

try:
    # Creates a new revocation registry
    api_response = api_instance.revocation_create_registry_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevocationApi->revocation_create_registry_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RevRegCreateRequest**](RevRegCreateRequest.md)|  | [optional] 

### Return type

[**RevRegResult**](RevRegResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revocation_credential_record_get**
> CredRevRecordResult revocation_credential_record_get(cred_ex_id=cred_ex_id, cred_rev_id=cred_rev_id, rev_reg_id=rev_reg_id)

Get credential revocation status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevocationApi()
cred_ex_id = 'cred_ex_id_example' # str | Credential exchange identifier (optional)
cred_rev_id = 'cred_rev_id_example' # str | Credential revocation identifier (optional)
rev_reg_id = 'rev_reg_id_example' # str | Revocation registry identifier (optional)

try:
    # Get credential revocation status
    api_response = api_instance.revocation_credential_record_get(cred_ex_id=cred_ex_id, cred_rev_id=cred_rev_id, rev_reg_id=rev_reg_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevocationApi->revocation_credential_record_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_ex_id** | **str**| Credential exchange identifier | [optional] 
 **cred_rev_id** | **str**| Credential revocation identifier | [optional] 
 **rev_reg_id** | **str**| Revocation registry identifier | [optional] 

### Return type

[**CredRevRecordResult**](CredRevRecordResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revocation_publish_revocations_post**
> PublishRevocations revocation_publish_revocations_post(body=body)

Publish pending revocations to ledger

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevocationApi()
body = swagger_client.PublishRevocations() # PublishRevocations |  (optional)

try:
    # Publish pending revocations to ledger
    api_response = api_instance.revocation_publish_revocations_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevocationApi->revocation_publish_revocations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PublishRevocations**](PublishRevocations.md)|  | [optional] 

### Return type

[**PublishRevocations**](PublishRevocations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revocation_registries_created_get**
> RevRegsCreated revocation_registries_created_get(cred_def_id=cred_def_id, state=state)

Search for matching revocation registries that current agent created

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevocationApi()
cred_def_id = 'cred_def_id_example' # str | Credential definition identifier (optional)
state = 'state_example' # str | Revocation registry state (optional)

try:
    # Search for matching revocation registries that current agent created
    api_response = api_instance.revocation_registries_created_get(cred_def_id=cred_def_id, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevocationApi->revocation_registries_created_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_def_id** | **str**| Credential definition identifier | [optional] 
 **state** | **str**| Revocation registry state | [optional] 

### Return type

[**RevRegsCreated**](RevRegsCreated.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revocation_registry_rev_reg_id_definition_post**
> RevRegResult revocation_registry_rev_reg_id_definition_post(rev_reg_id)

Send revocation registry definition to ledger

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevocationApi()
rev_reg_id = 'rev_reg_id_example' # str | Revocation Registry identifier

try:
    # Send revocation registry definition to ledger
    api_response = api_instance.revocation_registry_rev_reg_id_definition_post(rev_reg_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevocationApi->revocation_registry_rev_reg_id_definition_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rev_reg_id** | **str**| Revocation Registry identifier | 

### Return type

[**RevRegResult**](RevRegResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revocation_registry_rev_reg_id_entry_post**
> RevRegResult revocation_registry_rev_reg_id_entry_post(rev_reg_id)

Send revocation registry entry to ledger

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevocationApi()
rev_reg_id = 'rev_reg_id_example' # str | Revocation Registry identifier

try:
    # Send revocation registry entry to ledger
    api_response = api_instance.revocation_registry_rev_reg_id_entry_post(rev_reg_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevocationApi->revocation_registry_rev_reg_id_entry_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rev_reg_id** | **str**| Revocation Registry identifier | 

### Return type

[**RevRegResult**](RevRegResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revocation_registry_rev_reg_id_get**
> RevRegResult revocation_registry_rev_reg_id_get(rev_reg_id)

Get revocation registry by revocation registry id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevocationApi()
rev_reg_id = 'rev_reg_id_example' # str | Revocation Registry identifier

try:
    # Get revocation registry by revocation registry id
    api_response = api_instance.revocation_registry_rev_reg_id_get(rev_reg_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevocationApi->revocation_registry_rev_reg_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rev_reg_id** | **str**| Revocation Registry identifier | 

### Return type

[**RevRegResult**](RevRegResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revocation_registry_rev_reg_id_issued_get**
> RevRegIssuedResult revocation_registry_rev_reg_id_issued_get(rev_reg_id)

Get number of credentials issued against revocation registry

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevocationApi()
rev_reg_id = 'rev_reg_id_example' # str | Revocation Registry identifier

try:
    # Get number of credentials issued against revocation registry
    api_response = api_instance.revocation_registry_rev_reg_id_issued_get(rev_reg_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevocationApi->revocation_registry_rev_reg_id_issued_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rev_reg_id** | **str**| Revocation Registry identifier | 

### Return type

[**RevRegIssuedResult**](RevRegIssuedResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revocation_registry_rev_reg_id_patch**
> RevRegResult revocation_registry_rev_reg_id_patch(rev_reg_id, body=body)

Update revocation registry with new public URI to its tails file

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevocationApi()
rev_reg_id = 'rev_reg_id_example' # str | Revocation Registry identifier
body = swagger_client.RevRegUpdateTailsFileUri() # RevRegUpdateTailsFileUri |  (optional)

try:
    # Update revocation registry with new public URI to its tails file
    api_response = api_instance.revocation_registry_rev_reg_id_patch(rev_reg_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevocationApi->revocation_registry_rev_reg_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rev_reg_id** | **str**| Revocation Registry identifier | 
 **body** | [**RevRegUpdateTailsFileUri**](RevRegUpdateTailsFileUri.md)|  | [optional] 

### Return type

[**RevRegResult**](RevRegResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revocation_registry_rev_reg_id_set_state_patch**
> RevRegResult revocation_registry_rev_reg_id_set_state_patch(rev_reg_id, state)

Set revocation registry state manually

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevocationApi()
rev_reg_id = 'rev_reg_id_example' # str | Revocation Registry identifier
state = 'state_example' # str | Revocation registry state to set

try:
    # Set revocation registry state manually
    api_response = api_instance.revocation_registry_rev_reg_id_set_state_patch(rev_reg_id, state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevocationApi->revocation_registry_rev_reg_id_set_state_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rev_reg_id** | **str**| Revocation Registry identifier | 
 **state** | **str**| Revocation registry state to set | 

### Return type

[**RevRegResult**](RevRegResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revocation_registry_rev_reg_id_tails_file_get**
> str revocation_registry_rev_reg_id_tails_file_get(rev_reg_id)

Download tails file

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevocationApi()
rev_reg_id = 'rev_reg_id_example' # str | Revocation Registry identifier

try:
    # Download tails file
    api_response = api_instance.revocation_registry_rev_reg_id_tails_file_get(rev_reg_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevocationApi->revocation_registry_rev_reg_id_tails_file_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rev_reg_id** | **str**| Revocation Registry identifier | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revocation_registry_rev_reg_id_tails_file_put**
> RevocationModuleResponse revocation_registry_rev_reg_id_tails_file_put(rev_reg_id)

Upload local tails file to server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevocationApi()
rev_reg_id = 'rev_reg_id_example' # str | Revocation Registry identifier

try:
    # Upload local tails file to server
    api_response = api_instance.revocation_registry_rev_reg_id_tails_file_put(rev_reg_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevocationApi->revocation_registry_rev_reg_id_tails_file_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rev_reg_id** | **str**| Revocation Registry identifier | 

### Return type

[**RevocationModuleResponse**](RevocationModuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revocation_revoke_post**
> RevocationModuleResponse revocation_revoke_post(body=body)

Revoke an issued credential

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevocationApi()
body = swagger_client.RevokeRequest() # RevokeRequest |  (optional)

try:
    # Revoke an issued credential
    api_response = api_instance.revocation_revoke_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevocationApi->revocation_revoke_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RevokeRequest**](RevokeRequest.md)|  | [optional] 

### Return type

[**RevocationModuleResponse**](RevocationModuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

