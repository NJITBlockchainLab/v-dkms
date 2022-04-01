# swagger_client.LedgerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ledger_did_endpoint_get**](LedgerApi.md#ledger_did_endpoint_get) | **GET** /ledger/did-endpoint | Get the endpoint for a DID from the ledger.
[**ledger_did_verkey_get**](LedgerApi.md#ledger_did_verkey_get) | **GET** /ledger/did-verkey | Get the verkey for a DID from the ledger.
[**ledger_get_nym_role_get**](LedgerApi.md#ledger_get_nym_role_get) | **GET** /ledger/get-nym-role | Get the role from the NYM registration of a public DID.
[**ledger_register_nym_post**](LedgerApi.md#ledger_register_nym_post) | **POST** /ledger/register-nym | Send a NYM registration to the ledger.
[**ledger_rotate_public_did_keypair_patch**](LedgerApi.md#ledger_rotate_public_did_keypair_patch) | **PATCH** /ledger/rotate-public-did-keypair | Rotate key pair for public DID.
[**ledger_taa_accept_post**](LedgerApi.md#ledger_taa_accept_post) | **POST** /ledger/taa/accept | Accept the transaction author agreement
[**ledger_taa_get**](LedgerApi.md#ledger_taa_get) | **GET** /ledger/taa | Fetch the current transaction author agreement, if any


# **ledger_did_endpoint_get**
> LedgerModulesResult ledger_did_endpoint_get(did, endpoint_type=endpoint_type)

Get the endpoint for a DID from the ledger.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LedgerApi()
did = 'did_example' # str | DID of interest
endpoint_type = 'endpoint_type_example' # str | Endpoint type of interest (default 'Endpoint') (optional)

try:
    # Get the endpoint for a DID from the ledger.
    api_response = api_instance.ledger_did_endpoint_get(did, endpoint_type=endpoint_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LedgerApi->ledger_did_endpoint_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| DID of interest | 
 **endpoint_type** | **str**| Endpoint type of interest (default &#39;Endpoint&#39;) | [optional] 

### Return type

[**LedgerModulesResult**](LedgerModulesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ledger_did_verkey_get**
> LedgerModulesResult ledger_did_verkey_get(did)

Get the verkey for a DID from the ledger.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LedgerApi()
did = 'did_example' # str | DID of interest

try:
    # Get the verkey for a DID from the ledger.
    api_response = api_instance.ledger_did_verkey_get(did)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LedgerApi->ledger_did_verkey_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| DID of interest | 

### Return type

[**LedgerModulesResult**](LedgerModulesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ledger_get_nym_role_get**
> LedgerModulesResult ledger_get_nym_role_get(did)

Get the role from the NYM registration of a public DID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LedgerApi()
did = 'did_example' # str | DID of interest

try:
    # Get the role from the NYM registration of a public DID.
    api_response = api_instance.ledger_get_nym_role_get(did)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LedgerApi->ledger_get_nym_role_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| DID of interest | 

### Return type

[**LedgerModulesResult**](LedgerModulesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ledger_register_nym_post**
> LedgerModulesResult ledger_register_nym_post(did, verkey, alias=alias, role=role)

Send a NYM registration to the ledger.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LedgerApi()
did = 'did_example' # str | DID to register
verkey = 'verkey_example' # str | Verification key
alias = 'alias_example' # str | Alias (optional)
role = 'role_example' # str | Role (optional)

try:
    # Send a NYM registration to the ledger.
    api_response = api_instance.ledger_register_nym_post(did, verkey, alias=alias, role=role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LedgerApi->ledger_register_nym_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| DID to register | 
 **verkey** | **str**| Verification key | 
 **alias** | **str**| Alias | [optional] 
 **role** | **str**| Role | [optional] 

### Return type

[**LedgerModulesResult**](LedgerModulesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ledger_rotate_public_did_keypair_patch**
> LedgerModulesResult ledger_rotate_public_did_keypair_patch()

Rotate key pair for public DID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LedgerApi()

try:
    # Rotate key pair for public DID.
    api_response = api_instance.ledger_rotate_public_did_keypair_patch()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LedgerApi->ledger_rotate_public_did_keypair_patch: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LedgerModulesResult**](LedgerModulesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ledger_taa_accept_post**
> LedgerModulesResult ledger_taa_accept_post(body=body)

Accept the transaction author agreement

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LedgerApi()
body = swagger_client.TAAAccept() # TAAAccept |  (optional)

try:
    # Accept the transaction author agreement
    api_response = api_instance.ledger_taa_accept_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LedgerApi->ledger_taa_accept_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TAAAccept**](TAAAccept.md)|  | [optional] 

### Return type

[**LedgerModulesResult**](LedgerModulesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ledger_taa_get**
> TAAResult ledger_taa_get()

Fetch the current transaction author agreement, if any

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LedgerApi()

try:
    # Fetch the current transaction author agreement, if any
    api_response = api_instance.ledger_taa_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LedgerApi->ledger_taa_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TAAResult**](TAAResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

