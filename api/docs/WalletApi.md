# swagger_client.WalletApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wallet_did_create_post**](WalletApi.md#wallet_did_create_post) | **POST** /wallet/did/create | Create a local DID
[**wallet_did_get**](WalletApi.md#wallet_did_get) | **GET** /wallet/did | List wallet DIDs
[**wallet_did_local_rotate_keypair_patch**](WalletApi.md#wallet_did_local_rotate_keypair_patch) | **PATCH** /wallet/did/local/rotate-keypair | Rotate keypair for a DID not posted to the ledger
[**wallet_did_public_get**](WalletApi.md#wallet_did_public_get) | **GET** /wallet/did/public | Fetch the current public DID
[**wallet_did_public_post**](WalletApi.md#wallet_did_public_post) | **POST** /wallet/did/public | Assign the current public DID
[**wallet_get_did_endpoint_get**](WalletApi.md#wallet_get_did_endpoint_get) | **GET** /wallet/get-did-endpoint | Query DID endpoint in wallet
[**wallet_set_did_endpoint_post**](WalletApi.md#wallet_set_did_endpoint_post) | **POST** /wallet/set-did-endpoint | Update endpoint in wallet and on ledger if posted to it


# **wallet_did_create_post**
> DIDResult wallet_did_create_post()

Create a local DID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WalletApi()

try:
    # Create a local DID
    api_response = api_instance.wallet_did_create_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->wallet_did_create_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DIDResult**](DIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_did_get**
> DIDList wallet_did_get(did=did, posture=posture, verkey=verkey)

List wallet DIDs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WalletApi()
did = 'did_example' # str | DID of interest (optional)
posture = 'posture_example' # str | Whether DID is current public DID, posted to ledger but current public DID, or local to the wallet (optional)
verkey = 'verkey_example' # str | Verification key of interest (optional)

try:
    # List wallet DIDs
    api_response = api_instance.wallet_did_get(did=did, posture=posture, verkey=verkey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->wallet_did_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| DID of interest | [optional] 
 **posture** | **str**| Whether DID is current public DID, posted to ledger but current public DID, or local to the wallet | [optional] 
 **verkey** | **str**| Verification key of interest | [optional] 

### Return type

[**DIDList**](DIDList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_did_local_rotate_keypair_patch**
> WalletModuleResponse wallet_did_local_rotate_keypair_patch(did)

Rotate keypair for a DID not posted to the ledger

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WalletApi()
did = 'did_example' # str | DID of interest

try:
    # Rotate keypair for a DID not posted to the ledger
    api_response = api_instance.wallet_did_local_rotate_keypair_patch(did)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->wallet_did_local_rotate_keypair_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| DID of interest | 

### Return type

[**WalletModuleResponse**](WalletModuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_did_public_get**
> DIDResult wallet_did_public_get()

Fetch the current public DID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WalletApi()

try:
    # Fetch the current public DID
    api_response = api_instance.wallet_did_public_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->wallet_did_public_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DIDResult**](DIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_did_public_post**
> DIDResult wallet_did_public_post(did)

Assign the current public DID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WalletApi()
did = 'did_example' # str | DID of interest

try:
    # Assign the current public DID
    api_response = api_instance.wallet_did_public_post(did)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->wallet_did_public_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| DID of interest | 

### Return type

[**DIDResult**](DIDResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_get_did_endpoint_get**
> DIDEndpoint wallet_get_did_endpoint_get(did)

Query DID endpoint in wallet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WalletApi()
did = 'did_example' # str | DID of interest

try:
    # Query DID endpoint in wallet
    api_response = api_instance.wallet_get_did_endpoint_get(did)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->wallet_get_did_endpoint_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| DID of interest | 

### Return type

[**DIDEndpoint**](DIDEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_set_did_endpoint_post**
> WalletModuleResponse wallet_set_did_endpoint_post(body=body)

Update endpoint in wallet and on ledger if posted to it

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WalletApi()
body = swagger_client.DIDEndpointWithType() # DIDEndpointWithType |  (optional)

try:
    # Update endpoint in wallet and on ledger if posted to it
    api_response = api_instance.wallet_set_did_endpoint_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->wallet_set_did_endpoint_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DIDEndpointWithType**](DIDEndpointWithType.md)|  | [optional] 

### Return type

[**WalletModuleResponse**](WalletModuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

