# swagger_client.OutOfBandApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**out_of_band_create_invitation_post**](OutOfBandApi.md#out_of_band_create_invitation_post) | **POST** /out-of-band/create-invitation | Create a new connection invitation
[**out_of_band_receive_invitation_post**](OutOfBandApi.md#out_of_band_receive_invitation_post) | **POST** /out-of-band/receive-invitation | Receive a new connection invitation


# **out_of_band_create_invitation_post**
> InvitationRecord out_of_band_create_invitation_post(body=body, auto_accept=auto_accept, multi_use=multi_use)

Create a new connection invitation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutOfBandApi()
body = swagger_client.InvitationCreateRequest() # InvitationCreateRequest |  (optional)
auto_accept = true # bool | Auto-accept connection (defaults to configuration) (optional)
multi_use = true # bool | Create invitation for multiple use (default false) (optional)

try:
    # Create a new connection invitation
    api_response = api_instance.out_of_band_create_invitation_post(body=body, auto_accept=auto_accept, multi_use=multi_use)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutOfBandApi->out_of_band_create_invitation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvitationCreateRequest**](InvitationCreateRequest.md)|  | [optional] 
 **auto_accept** | **bool**| Auto-accept connection (defaults to configuration) | [optional] 
 **multi_use** | **bool**| Create invitation for multiple use (default false) | [optional] 

### Return type

[**InvitationRecord**](InvitationRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **out_of_band_receive_invitation_post**
> ConnRecord out_of_band_receive_invitation_post(body=body, alias=alias, auto_accept=auto_accept, mediation_id=mediation_id, use_existing_connection=use_existing_connection)

Receive a new connection invitation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutOfBandApi()
body = swagger_client.InvitationReceiveRequest() # InvitationReceiveRequest |  (optional)
alias = 'alias_example' # str | Alias for connection (optional)
auto_accept = true # bool | Auto-accept connection (defaults to configuration) (optional)
mediation_id = 'mediation_id_example' # str | Identifier for active mediation record to be used (optional)
use_existing_connection = true # bool | Use an existing connection, if possible (optional)

try:
    # Receive a new connection invitation
    api_response = api_instance.out_of_band_receive_invitation_post(body=body, alias=alias, auto_accept=auto_accept, mediation_id=mediation_id, use_existing_connection=use_existing_connection)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutOfBandApi->out_of_band_receive_invitation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvitationReceiveRequest**](InvitationReceiveRequest.md)|  | [optional] 
 **alias** | **str**| Alias for connection | [optional] 
 **auto_accept** | **bool**| Auto-accept connection (defaults to configuration) | [optional] 
 **mediation_id** | **str**| Identifier for active mediation record to be used | [optional] 
 **use_existing_connection** | **bool**| Use an existing connection, if possible | [optional] 

### Return type

[**ConnRecord**](ConnRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

