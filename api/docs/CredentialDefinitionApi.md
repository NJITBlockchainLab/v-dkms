# swagger_client.CredentialDefinitionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credential_definitions_created_get**](CredentialDefinitionApi.md#credential_definitions_created_get) | **GET** /credential-definitions/created | Search for matching credential definitions that agent originated
[**credential_definitions_cred_def_id_get**](CredentialDefinitionApi.md#credential_definitions_cred_def_id_get) | **GET** /credential-definitions/{cred_def_id} | Gets a credential definition from the ledger
[**credential_definitions_post**](CredentialDefinitionApi.md#credential_definitions_post) | **POST** /credential-definitions | Sends a credential definition to the ledger


# **credential_definitions_created_get**
> CredentialDefinitionsCreatedResults credential_definitions_created_get(cred_def_id=cred_def_id, issuer_did=issuer_did, schema_id=schema_id, schema_issuer_did=schema_issuer_did, schema_name=schema_name, schema_version=schema_version)

Search for matching credential definitions that agent originated

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CredentialDefinitionApi()
cred_def_id = 'cred_def_id_example' # str | Credential definition id (optional)
issuer_did = 'issuer_did_example' # str | Issuer DID (optional)
schema_id = 'schema_id_example' # str | Schema identifier (optional)
schema_issuer_did = 'schema_issuer_did_example' # str | Schema issuer DID (optional)
schema_name = 'schema_name_example' # str | Schema name (optional)
schema_version = 'schema_version_example' # str | Schema version (optional)

try:
    # Search for matching credential definitions that agent originated
    api_response = api_instance.credential_definitions_created_get(cred_def_id=cred_def_id, issuer_did=issuer_did, schema_id=schema_id, schema_issuer_did=schema_issuer_did, schema_name=schema_name, schema_version=schema_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialDefinitionApi->credential_definitions_created_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_def_id** | **str**| Credential definition id | [optional] 
 **issuer_did** | **str**| Issuer DID | [optional] 
 **schema_id** | **str**| Schema identifier | [optional] 
 **schema_issuer_did** | **str**| Schema issuer DID | [optional] 
 **schema_name** | **str**| Schema name | [optional] 
 **schema_version** | **str**| Schema version | [optional] 

### Return type

[**CredentialDefinitionsCreatedResults**](CredentialDefinitionsCreatedResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credential_definitions_cred_def_id_get**
> CredentialDefinitionGetResults credential_definitions_cred_def_id_get(cred_def_id)

Gets a credential definition from the ledger

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CredentialDefinitionApi()
cred_def_id = 'cred_def_id_example' # str | Credential definition identifier

try:
    # Gets a credential definition from the ledger
    api_response = api_instance.credential_definitions_cred_def_id_get(cred_def_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialDefinitionApi->credential_definitions_cred_def_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_def_id** | **str**| Credential definition identifier | 

### Return type

[**CredentialDefinitionGetResults**](CredentialDefinitionGetResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credential_definitions_post**
> CredentialDefinitionSendResults credential_definitions_post(body=body)

Sends a credential definition to the ledger

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CredentialDefinitionApi()
body = swagger_client.CredentialDefinitionSendRequest() # CredentialDefinitionSendRequest |  (optional)

try:
    # Sends a credential definition to the ledger
    api_response = api_instance.credential_definitions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialDefinitionApi->credential_definitions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CredentialDefinitionSendRequest**](CredentialDefinitionSendRequest.md)|  | [optional] 

### Return type

[**CredentialDefinitionSendResults**](CredentialDefinitionSendResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

