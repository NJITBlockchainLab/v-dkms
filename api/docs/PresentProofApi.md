# swagger_client.PresentProofApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**present_proof_create_request_post**](PresentProofApi.md#present_proof_create_request_post) | **POST** /present-proof/create-request |      Creates a presentation request not bound to any proposal or existing connection     
[**present_proof_records_get**](PresentProofApi.md#present_proof_records_get) | **GET** /present-proof/records | Fetch all present-proof exchange records
[**present_proof_records_pres_ex_id_credentials_get**](PresentProofApi.md#present_proof_records_pres_ex_id_credentials_get) | **GET** /present-proof/records/{pres_ex_id}/credentials | Fetch credentials for a presentation request from wallet
[**present_proof_records_pres_ex_id_delete**](PresentProofApi.md#present_proof_records_pres_ex_id_delete) | **DELETE** /present-proof/records/{pres_ex_id} | Remove an existing presentation exchange record
[**present_proof_records_pres_ex_id_get**](PresentProofApi.md#present_proof_records_pres_ex_id_get) | **GET** /present-proof/records/{pres_ex_id} | Fetch a single presentation exchange record
[**present_proof_records_pres_ex_id_problem_report_post**](PresentProofApi.md#present_proof_records_pres_ex_id_problem_report_post) | **POST** /present-proof/records/{pres_ex_id}/problem-report | Send a problem report for presentation exchange
[**present_proof_records_pres_ex_id_send_presentation_post**](PresentProofApi.md#present_proof_records_pres_ex_id_send_presentation_post) | **POST** /present-proof/records/{pres_ex_id}/send-presentation | Sends a proof presentation
[**present_proof_records_pres_ex_id_send_request_post**](PresentProofApi.md#present_proof_records_pres_ex_id_send_request_post) | **POST** /present-proof/records/{pres_ex_id}/send-request | Sends a presentation request in reference to a proposal
[**present_proof_records_pres_ex_id_verify_presentation_post**](PresentProofApi.md#present_proof_records_pres_ex_id_verify_presentation_post) | **POST** /present-proof/records/{pres_ex_id}/verify-presentation | Verify a received presentation
[**present_proof_send_proposal_post**](PresentProofApi.md#present_proof_send_proposal_post) | **POST** /present-proof/send-proposal | Sends a presentation proposal
[**present_proof_send_request_post**](PresentProofApi.md#present_proof_send_request_post) | **POST** /present-proof/send-request | Sends a free presentation request not bound to any proposal


# **present_proof_create_request_post**
> V10PresentationExchange present_proof_create_request_post(body=body)

     Creates a presentation request not bound to any proposal or existing connection     

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresentProofApi()
body = swagger_client.V10PresentationCreateRequestRequest() # V10PresentationCreateRequestRequest |  (optional)

try:
    #      Creates a presentation request not bound to any proposal or existing connection     
    api_response = api_instance.present_proof_create_request_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->present_proof_create_request_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V10PresentationCreateRequestRequest**](V10PresentationCreateRequestRequest.md)|  | [optional] 

### Return type

[**V10PresentationExchange**](V10PresentationExchange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **present_proof_records_get**
> V10PresentationExchangeList present_proof_records_get(connection_id=connection_id, role=role, state=state, thread_id=thread_id)

Fetch all present-proof exchange records

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresentProofApi()
connection_id = 'connection_id_example' # str | Connection identifier (optional)
role = 'role_example' # str | Role assigned in presentation exchange (optional)
state = 'state_example' # str | Presentation exchange state (optional)
thread_id = 'thread_id_example' # str | Thread identifier (optional)

try:
    # Fetch all present-proof exchange records
    api_response = api_instance.present_proof_records_get(connection_id=connection_id, role=role, state=state, thread_id=thread_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->present_proof_records_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | [**str**](.md)| Connection identifier | [optional] 
 **role** | **str**| Role assigned in presentation exchange | [optional] 
 **state** | **str**| Presentation exchange state | [optional] 
 **thread_id** | [**str**](.md)| Thread identifier | [optional] 

### Return type

[**V10PresentationExchangeList**](V10PresentationExchangeList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **present_proof_records_pres_ex_id_credentials_get**
> list[IndyCredPrecis] present_proof_records_pres_ex_id_credentials_get(pres_ex_id, count=count, extra_query=extra_query, referent=referent, start=start)

Fetch credentials for a presentation request from wallet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresentProofApi()
pres_ex_id = 'pres_ex_id_example' # str | Presentation exchange identifier
count = 'count_example' # str | Maximum number to retrieve (optional)
extra_query = 'extra_query_example' # str | (JSON) object mapping referents to extra WQL queries (optional)
referent = 'referent_example' # str | Proof request referents of interest, comma-separated (optional)
start = 'start_example' # str | Start index (optional)

try:
    # Fetch credentials for a presentation request from wallet
    api_response = api_instance.present_proof_records_pres_ex_id_credentials_get(pres_ex_id, count=count, extra_query=extra_query, referent=referent, start=start)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->present_proof_records_pres_ex_id_credentials_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pres_ex_id** | **str**| Presentation exchange identifier | 
 **count** | **str**| Maximum number to retrieve | [optional] 
 **extra_query** | **str**| (JSON) object mapping referents to extra WQL queries | [optional] 
 **referent** | **str**| Proof request referents of interest, comma-separated | [optional] 
 **start** | **str**| Start index | [optional] 

### Return type

[**list[IndyCredPrecis]**](IndyCredPrecis.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **present_proof_records_pres_ex_id_delete**
> PresentProofModuleResponse present_proof_records_pres_ex_id_delete(pres_ex_id)

Remove an existing presentation exchange record

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresentProofApi()
pres_ex_id = 'pres_ex_id_example' # str | Presentation exchange identifier

try:
    # Remove an existing presentation exchange record
    api_response = api_instance.present_proof_records_pres_ex_id_delete(pres_ex_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->present_proof_records_pres_ex_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pres_ex_id** | **str**| Presentation exchange identifier | 

### Return type

[**PresentProofModuleResponse**](PresentProofModuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **present_proof_records_pres_ex_id_get**
> V10PresentationExchange present_proof_records_pres_ex_id_get(pres_ex_id)

Fetch a single presentation exchange record

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresentProofApi()
pres_ex_id = 'pres_ex_id_example' # str | Presentation exchange identifier

try:
    # Fetch a single presentation exchange record
    api_response = api_instance.present_proof_records_pres_ex_id_get(pres_ex_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->present_proof_records_pres_ex_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pres_ex_id** | **str**| Presentation exchange identifier | 

### Return type

[**V10PresentationExchange**](V10PresentationExchange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **present_proof_records_pres_ex_id_problem_report_post**
> PresentProofModuleResponse present_proof_records_pres_ex_id_problem_report_post(pres_ex_id, body=body)

Send a problem report for presentation exchange

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresentProofApi()
pres_ex_id = 'pres_ex_id_example' # str | Presentation exchange identifier
body = swagger_client.V10PresentationProblemReportRequest() # V10PresentationProblemReportRequest |  (optional)

try:
    # Send a problem report for presentation exchange
    api_response = api_instance.present_proof_records_pres_ex_id_problem_report_post(pres_ex_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->present_proof_records_pres_ex_id_problem_report_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pres_ex_id** | **str**| Presentation exchange identifier | 
 **body** | [**V10PresentationProblemReportRequest**](V10PresentationProblemReportRequest.md)|  | [optional] 

### Return type

[**PresentProofModuleResponse**](PresentProofModuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **present_proof_records_pres_ex_id_send_presentation_post**
> V10PresentationExchange present_proof_records_pres_ex_id_send_presentation_post(pres_ex_id, body=body)

Sends a proof presentation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresentProofApi()
pres_ex_id = 'pres_ex_id_example' # str | Presentation exchange identifier
body = swagger_client.V10PresentationRequest() # V10PresentationRequest |  (optional)

try:
    # Sends a proof presentation
    api_response = api_instance.present_proof_records_pres_ex_id_send_presentation_post(pres_ex_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->present_proof_records_pres_ex_id_send_presentation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pres_ex_id** | **str**| Presentation exchange identifier | 
 **body** | [**V10PresentationRequest**](V10PresentationRequest.md)|  | [optional] 

### Return type

[**V10PresentationExchange**](V10PresentationExchange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **present_proof_records_pres_ex_id_send_request_post**
> V10PresentationExchange present_proof_records_pres_ex_id_send_request_post(pres_ex_id, body=body)

Sends a presentation request in reference to a proposal

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresentProofApi()
pres_ex_id = 'pres_ex_id_example' # str | Presentation exchange identifier
body = swagger_client.AdminAPIMessageTracing() # AdminAPIMessageTracing |  (optional)

try:
    # Sends a presentation request in reference to a proposal
    api_response = api_instance.present_proof_records_pres_ex_id_send_request_post(pres_ex_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->present_proof_records_pres_ex_id_send_request_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pres_ex_id** | **str**| Presentation exchange identifier | 
 **body** | [**AdminAPIMessageTracing**](AdminAPIMessageTracing.md)|  | [optional] 

### Return type

[**V10PresentationExchange**](V10PresentationExchange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **present_proof_records_pres_ex_id_verify_presentation_post**
> V10PresentationExchange present_proof_records_pres_ex_id_verify_presentation_post(pres_ex_id)

Verify a received presentation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresentProofApi()
pres_ex_id = 'pres_ex_id_example' # str | Presentation exchange identifier

try:
    # Verify a received presentation
    api_response = api_instance.present_proof_records_pres_ex_id_verify_presentation_post(pres_ex_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->present_proof_records_pres_ex_id_verify_presentation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pres_ex_id** | **str**| Presentation exchange identifier | 

### Return type

[**V10PresentationExchange**](V10PresentationExchange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **present_proof_send_proposal_post**
> V10PresentationExchange present_proof_send_proposal_post(body=body)

Sends a presentation proposal

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresentProofApi()
body = swagger_client.V10PresentationProposalRequest() # V10PresentationProposalRequest |  (optional)

try:
    # Sends a presentation proposal
    api_response = api_instance.present_proof_send_proposal_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->present_proof_send_proposal_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V10PresentationProposalRequest**](V10PresentationProposalRequest.md)|  | [optional] 

### Return type

[**V10PresentationExchange**](V10PresentationExchange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **present_proof_send_request_post**
> V10PresentationExchange present_proof_send_request_post(body=body)

Sends a free presentation request not bound to any proposal

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresentProofApi()
body = swagger_client.V10PresentationSendRequestRequest() # V10PresentationSendRequestRequest |  (optional)

try:
    # Sends a free presentation request not bound to any proposal
    api_response = api_instance.present_proof_send_request_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->present_proof_send_request_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V10PresentationSendRequestRequest**](V10PresentationSendRequestRequest.md)|  | [optional] 

### Return type

[**V10PresentationExchange**](V10PresentationExchange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

