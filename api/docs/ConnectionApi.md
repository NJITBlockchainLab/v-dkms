# swagger_client.ConnectionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connections_conn_id_accept_invitation_post**](ConnectionApi.md#connections_conn_id_accept_invitation_post) | **POST** /connections/{conn_id}/accept-invitation | Accept a stored connection invitation
[**connections_conn_id_accept_request_post**](ConnectionApi.md#connections_conn_id_accept_request_post) | **POST** /connections/{conn_id}/accept-request | Accept a stored connection request
[**connections_conn_id_delete**](ConnectionApi.md#connections_conn_id_delete) | **DELETE** /connections/{conn_id} | Remove an existing connection record
[**connections_conn_id_endpoints_get**](ConnectionApi.md#connections_conn_id_endpoints_get) | **GET** /connections/{conn_id}/endpoints | Fetch connection remote endpoint
[**connections_conn_id_establish_inbound_ref_id_post**](ConnectionApi.md#connections_conn_id_establish_inbound_ref_id_post) | **POST** /connections/{conn_id}/establish-inbound/{ref_id} | Assign another connection as the inbound connection
[**connections_conn_id_get**](ConnectionApi.md#connections_conn_id_get) | **GET** /connections/{conn_id} | Fetch a single connection record
[**connections_conn_id_metadata_get**](ConnectionApi.md#connections_conn_id_metadata_get) | **GET** /connections/{conn_id}/metadata | Fetch connection metadata
[**connections_conn_id_metadata_post**](ConnectionApi.md#connections_conn_id_metadata_post) | **POST** /connections/{conn_id}/metadata | Set connection metadata
[**connections_create_invitation_post**](ConnectionApi.md#connections_create_invitation_post) | **POST** /connections/create-invitation | Create a new connection invitation
[**connections_create_static_post**](ConnectionApi.md#connections_create_static_post) | **POST** /connections/create-static | Create a new static connection
[**connections_get**](ConnectionApi.md#connections_get) | **GET** /connections | Query agent-to-agent connections
[**connections_receive_invitation_post**](ConnectionApi.md#connections_receive_invitation_post) | **POST** /connections/receive-invitation | Receive a new connection invitation


# **connections_conn_id_accept_invitation_post**
> ConnRecord connections_conn_id_accept_invitation_post(conn_id, mediation_id=mediation_id, my_endpoint=my_endpoint, my_label=my_label)

Accept a stored connection invitation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
conn_id = 'conn_id_example' # str | Connection identifier
mediation_id = 'mediation_id_example' # str | Identifier for active mediation record to be used (optional)
my_endpoint = 'my_endpoint_example' # str | My URL endpoint (optional)
my_label = 'my_label_example' # str | Label for connection (optional)

try:
    # Accept a stored connection invitation
    api_response = api_instance.connections_conn_id_accept_invitation_post(conn_id, mediation_id=mediation_id, my_endpoint=my_endpoint, my_label=my_label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->connections_conn_id_accept_invitation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier | 
 **mediation_id** | **str**| Identifier for active mediation record to be used | [optional] 
 **my_endpoint** | **str**| My URL endpoint | [optional] 
 **my_label** | **str**| Label for connection | [optional] 

### Return type

[**ConnRecord**](ConnRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connections_conn_id_accept_request_post**
> ConnRecord connections_conn_id_accept_request_post(conn_id, my_endpoint=my_endpoint)

Accept a stored connection request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
conn_id = 'conn_id_example' # str | Connection identifier
my_endpoint = 'my_endpoint_example' # str | My URL endpoint (optional)

try:
    # Accept a stored connection request
    api_response = api_instance.connections_conn_id_accept_request_post(conn_id, my_endpoint=my_endpoint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->connections_conn_id_accept_request_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier | 
 **my_endpoint** | **str**| My URL endpoint | [optional] 

### Return type

[**ConnRecord**](ConnRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connections_conn_id_delete**
> ConnectionModuleResponse connections_conn_id_delete(conn_id)

Remove an existing connection record

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
conn_id = 'conn_id_example' # str | Connection identifier

try:
    # Remove an existing connection record
    api_response = api_instance.connections_conn_id_delete(conn_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->connections_conn_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier | 

### Return type

[**ConnectionModuleResponse**](ConnectionModuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connections_conn_id_endpoints_get**
> EndpointsResult connections_conn_id_endpoints_get(conn_id)

Fetch connection remote endpoint

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
conn_id = 'conn_id_example' # str | Connection identifier

try:
    # Fetch connection remote endpoint
    api_response = api_instance.connections_conn_id_endpoints_get(conn_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->connections_conn_id_endpoints_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier | 

### Return type

[**EndpointsResult**](EndpointsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connections_conn_id_establish_inbound_ref_id_post**
> ConnectionModuleResponse connections_conn_id_establish_inbound_ref_id_post(conn_id, ref_id)

Assign another connection as the inbound connection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
conn_id = 'conn_id_example' # str | Connection identifier
ref_id = 'ref_id_example' # str | Inbound connection identifier

try:
    # Assign another connection as the inbound connection
    api_response = api_instance.connections_conn_id_establish_inbound_ref_id_post(conn_id, ref_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->connections_conn_id_establish_inbound_ref_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier | 
 **ref_id** | **str**| Inbound connection identifier | 

### Return type

[**ConnectionModuleResponse**](ConnectionModuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connections_conn_id_get**
> ConnRecord connections_conn_id_get(conn_id)

Fetch a single connection record

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
conn_id = 'conn_id_example' # str | Connection identifier

try:
    # Fetch a single connection record
    api_response = api_instance.connections_conn_id_get(conn_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->connections_conn_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier | 

### Return type

[**ConnRecord**](ConnRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connections_conn_id_metadata_get**
> ConnectionMetadata connections_conn_id_metadata_get(conn_id, key=key)

Fetch connection metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
conn_id = 'conn_id_example' # str | Connection identifier
key = 'key_example' # str | Key to retrieve. (optional)

try:
    # Fetch connection metadata
    api_response = api_instance.connections_conn_id_metadata_get(conn_id, key=key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->connections_conn_id_metadata_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier | 
 **key** | **str**| Key to retrieve. | [optional] 

### Return type

[**ConnectionMetadata**](ConnectionMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connections_conn_id_metadata_post**
> ConnectionMetadata connections_conn_id_metadata_post(conn_id, body=body)

Set connection metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
conn_id = 'conn_id_example' # str | Connection identifier
body = swagger_client.ConnectionMetadataSetRequest() # ConnectionMetadataSetRequest |  (optional)

try:
    # Set connection metadata
    api_response = api_instance.connections_conn_id_metadata_post(conn_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->connections_conn_id_metadata_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier | 
 **body** | [**ConnectionMetadataSetRequest**](ConnectionMetadataSetRequest.md)|  | [optional] 

### Return type

[**ConnectionMetadata**](ConnectionMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connections_create_invitation_post**
> InvitationResult connections_create_invitation_post(body=body, alias=alias, auto_accept=auto_accept, multi_use=multi_use, public=public)

Create a new connection invitation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
body = swagger_client.CreateInvitationRequest() # CreateInvitationRequest |  (optional)
alias = 'alias_example' # str | Alias (optional)
auto_accept = true # bool | Auto-accept connection (defaults to configuration) (optional)
multi_use = true # bool | Create invitation for multiple use (default false) (optional)
public = true # bool | Create invitation from public DID (default false) (optional)

try:
    # Create a new connection invitation
    api_response = api_instance.connections_create_invitation_post(body=body, alias=alias, auto_accept=auto_accept, multi_use=multi_use, public=public)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->connections_create_invitation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateInvitationRequest**](CreateInvitationRequest.md)|  | [optional] 
 **alias** | **str**| Alias | [optional] 
 **auto_accept** | **bool**| Auto-accept connection (defaults to configuration) | [optional] 
 **multi_use** | **bool**| Create invitation for multiple use (default false) | [optional] 
 **public** | **bool**| Create invitation from public DID (default false) | [optional] 

### Return type

[**InvitationResult**](InvitationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connections_create_static_post**
> ConnectionStaticResult connections_create_static_post(body=body)

Create a new static connection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
body = swagger_client.ConnectionStaticRequest() # ConnectionStaticRequest |  (optional)

try:
    # Create a new static connection
    api_response = api_instance.connections_create_static_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->connections_create_static_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectionStaticRequest**](ConnectionStaticRequest.md)|  | [optional] 

### Return type

[**ConnectionStaticResult**](ConnectionStaticResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connections_get**
> ConnectionList connections_get(alias=alias, invitation_key=invitation_key, my_did=my_did, state=state, their_did=their_did, their_role=their_role)

Query agent-to-agent connections

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
alias = 'alias_example' # str | Alias (optional)
invitation_key = 'invitation_key_example' # str | invitation key (optional)
my_did = 'my_did_example' # str | My DID (optional)
state = 'state_example' # str | Connection state (optional)
their_did = 'their_did_example' # str | Their DID (optional)
their_role = 'their_role_example' # str | Their role in the connection protocol (optional)

try:
    # Query agent-to-agent connections
    api_response = api_instance.connections_get(alias=alias, invitation_key=invitation_key, my_did=my_did, state=state, their_did=their_did, their_role=their_role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->connections_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias | [optional] 
 **invitation_key** | **str**| invitation key | [optional] 
 **my_did** | **str**| My DID | [optional] 
 **state** | **str**| Connection state | [optional] 
 **their_did** | **str**| Their DID | [optional] 
 **their_role** | **str**| Their role in the connection protocol | [optional] 

### Return type

[**ConnectionList**](ConnectionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connections_receive_invitation_post**
> ConnRecord connections_receive_invitation_post(body=body, alias=alias, auto_accept=auto_accept, mediation_id=mediation_id)

Receive a new connection invitation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
body = swagger_client.ReceiveInvitationRequest() # ReceiveInvitationRequest |  (optional)
alias = 'alias_example' # str | Alias (optional)
auto_accept = true # bool | Auto-accept connection (defaults to configuration) (optional)
mediation_id = 'mediation_id_example' # str | Identifier for active mediation record to be used (optional)

try:
    # Receive a new connection invitation
    api_response = api_instance.connections_receive_invitation_post(body=body, alias=alias, auto_accept=auto_accept, mediation_id=mediation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->connections_receive_invitation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReceiveInvitationRequest**](ReceiveInvitationRequest.md)|  | [optional] 
 **alias** | **str**| Alias | [optional] 
 **auto_accept** | **bool**| Auto-accept connection (defaults to configuration) | [optional] 
 **mediation_id** | **str**| Identifier for active mediation record to be used | [optional] 

### Return type

[**ConnRecord**](ConnRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

