# swagger_client.SchemaApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schemas_created_get**](SchemaApi.md#schemas_created_get) | **GET** /schemas/created | Search for matching schema that agent originated
[**schemas_post**](SchemaApi.md#schemas_post) | **POST** /schemas | Sends a schema to the ledger
[**schemas_schema_id_get**](SchemaApi.md#schemas_schema_id_get) | **GET** /schemas/{schema_id} | Gets a schema from the ledger


# **schemas_created_get**
> SchemasCreatedResults schemas_created_get(schema_id=schema_id, schema_issuer_did=schema_issuer_did, schema_name=schema_name, schema_version=schema_version)

Search for matching schema that agent originated

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SchemaApi()
schema_id = 'schema_id_example' # str | Schema identifier (optional)
schema_issuer_did = 'schema_issuer_did_example' # str | Schema issuer DID (optional)
schema_name = 'schema_name_example' # str | Schema name (optional)
schema_version = 'schema_version_example' # str | Schema version (optional)

try:
    # Search for matching schema that agent originated
    api_response = api_instance.schemas_created_get(schema_id=schema_id, schema_issuer_did=schema_issuer_did, schema_name=schema_name, schema_version=schema_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaApi->schemas_created_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_id** | **str**| Schema identifier | [optional] 
 **schema_issuer_did** | **str**| Schema issuer DID | [optional] 
 **schema_name** | **str**| Schema name | [optional] 
 **schema_version** | **str**| Schema version | [optional] 

### Return type

[**SchemasCreatedResults**](SchemasCreatedResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schemas_post**
> SchemaSendResults schemas_post(body=body)

Sends a schema to the ledger

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SchemaApi()
body = swagger_client.SchemaSendRequest() # SchemaSendRequest |  (optional)

try:
    # Sends a schema to the ledger
    api_response = api_instance.schemas_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaApi->schemas_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SchemaSendRequest**](SchemaSendRequest.md)|  | [optional] 

### Return type

[**SchemaSendResults**](SchemaSendResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schemas_schema_id_get**
> SchemaGetResults schemas_schema_id_get(schema_id)

Gets a schema from the ledger

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SchemaApi()
schema_id = 'schema_id_example' # str | Schema identifier

try:
    # Gets a schema from the ledger
    api_response = api_instance.schemas_schema_id_get(schema_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaApi->schemas_schema_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_id** | **str**| Schema identifier | 

### Return type

[**SchemaGetResults**](SchemaGetResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

