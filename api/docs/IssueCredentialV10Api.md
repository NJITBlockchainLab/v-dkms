# swagger_client.IssueCredentialV10Api

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**issue_credential_create_post**](IssueCredentialV10Api.md#issue_credential_create_post) | **POST** /issue-credential/create | Send holder a credential, automating entire flow
[**issue_credential_records_cred_ex_id_delete**](IssueCredentialV10Api.md#issue_credential_records_cred_ex_id_delete) | **DELETE** /issue-credential/records/{cred_ex_id} | Remove an existing credential exchange record
[**issue_credential_records_cred_ex_id_get**](IssueCredentialV10Api.md#issue_credential_records_cred_ex_id_get) | **GET** /issue-credential/records/{cred_ex_id} | Fetch a single credential exchange record
[**issue_credential_records_cred_ex_id_issue_post**](IssueCredentialV10Api.md#issue_credential_records_cred_ex_id_issue_post) | **POST** /issue-credential/records/{cred_ex_id}/issue | Send holder a credential
[**issue_credential_records_cred_ex_id_problem_report_post**](IssueCredentialV10Api.md#issue_credential_records_cred_ex_id_problem_report_post) | **POST** /issue-credential/records/{cred_ex_id}/problem-report | Send a problem report for credential exchange
[**issue_credential_records_cred_ex_id_send_offer_post**](IssueCredentialV10Api.md#issue_credential_records_cred_ex_id_send_offer_post) | **POST** /issue-credential/records/{cred_ex_id}/send-offer | Send holder a credential offer in reference to a proposal with preview
[**issue_credential_records_cred_ex_id_send_request_post**](IssueCredentialV10Api.md#issue_credential_records_cred_ex_id_send_request_post) | **POST** /issue-credential/records/{cred_ex_id}/send-request | Send issuer a credential request
[**issue_credential_records_cred_ex_id_store_post**](IssueCredentialV10Api.md#issue_credential_records_cred_ex_id_store_post) | **POST** /issue-credential/records/{cred_ex_id}/store | Store a received credential
[**issue_credential_records_get**](IssueCredentialV10Api.md#issue_credential_records_get) | **GET** /issue-credential/records | Fetch all credential exchange records
[**issue_credential_send_offer_post**](IssueCredentialV10Api.md#issue_credential_send_offer_post) | **POST** /issue-credential/send-offer | Send holder a credential offer, independent of any proposal
[**issue_credential_send_post**](IssueCredentialV10Api.md#issue_credential_send_post) | **POST** /issue-credential/send | Send holder a credential, automating entire flow
[**issue_credential_send_proposal_post**](IssueCredentialV10Api.md#issue_credential_send_proposal_post) | **POST** /issue-credential/send-proposal | Send issuer a credential proposal


# **issue_credential_create_post**
> V10CredentialExchange issue_credential_create_post(body=body)

Send holder a credential, automating entire flow

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialV10Api()
body = swagger_client.V10CredentialCreate() # V10CredentialCreate |  (optional)

try:
    # Send holder a credential, automating entire flow
    api_response = api_instance.issue_credential_create_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialV10Api->issue_credential_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V10CredentialCreate**](V10CredentialCreate.md)|  | [optional] 

### Return type

[**V10CredentialExchange**](V10CredentialExchange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential_records_cred_ex_id_delete**
> IssueCredentialModuleResponse issue_credential_records_cred_ex_id_delete(cred_ex_id)

Remove an existing credential exchange record

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialV10Api()
cred_ex_id = 'cred_ex_id_example' # str | Credential exchange identifier

try:
    # Remove an existing credential exchange record
    api_response = api_instance.issue_credential_records_cred_ex_id_delete(cred_ex_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialV10Api->issue_credential_records_cred_ex_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_ex_id** | **str**| Credential exchange identifier | 

### Return type

[**IssueCredentialModuleResponse**](IssueCredentialModuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential_records_cred_ex_id_get**
> V10CredentialExchange issue_credential_records_cred_ex_id_get(cred_ex_id)

Fetch a single credential exchange record

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialV10Api()
cred_ex_id = 'cred_ex_id_example' # str | Credential exchange identifier

try:
    # Fetch a single credential exchange record
    api_response = api_instance.issue_credential_records_cred_ex_id_get(cred_ex_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialV10Api->issue_credential_records_cred_ex_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_ex_id** | **str**| Credential exchange identifier | 

### Return type

[**V10CredentialExchange**](V10CredentialExchange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential_records_cred_ex_id_issue_post**
> V10CredentialExchange issue_credential_records_cred_ex_id_issue_post(cred_ex_id, body=body)

Send holder a credential

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialV10Api()
cred_ex_id = 'cred_ex_id_example' # str | Credential exchange identifier
body = swagger_client.V10CredentialIssueRequest() # V10CredentialIssueRequest |  (optional)

try:
    # Send holder a credential
    api_response = api_instance.issue_credential_records_cred_ex_id_issue_post(cred_ex_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialV10Api->issue_credential_records_cred_ex_id_issue_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_ex_id** | **str**| Credential exchange identifier | 
 **body** | [**V10CredentialIssueRequest**](V10CredentialIssueRequest.md)|  | [optional] 

### Return type

[**V10CredentialExchange**](V10CredentialExchange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential_records_cred_ex_id_problem_report_post**
> IssueCredentialModuleResponse issue_credential_records_cred_ex_id_problem_report_post(cred_ex_id, body=body)

Send a problem report for credential exchange

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialV10Api()
cred_ex_id = 'cred_ex_id_example' # str | Credential exchange identifier
body = swagger_client.V10CredentialProblemReportRequest() # V10CredentialProblemReportRequest |  (optional)

try:
    # Send a problem report for credential exchange
    api_response = api_instance.issue_credential_records_cred_ex_id_problem_report_post(cred_ex_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialV10Api->issue_credential_records_cred_ex_id_problem_report_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_ex_id** | **str**| Credential exchange identifier | 
 **body** | [**V10CredentialProblemReportRequest**](V10CredentialProblemReportRequest.md)|  | [optional] 

### Return type

[**IssueCredentialModuleResponse**](IssueCredentialModuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential_records_cred_ex_id_send_offer_post**
> V10CredentialExchange issue_credential_records_cred_ex_id_send_offer_post(cred_ex_id)

Send holder a credential offer in reference to a proposal with preview

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialV10Api()
cred_ex_id = 'cred_ex_id_example' # str | Credential exchange identifier

try:
    # Send holder a credential offer in reference to a proposal with preview
    api_response = api_instance.issue_credential_records_cred_ex_id_send_offer_post(cred_ex_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialV10Api->issue_credential_records_cred_ex_id_send_offer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_ex_id** | **str**| Credential exchange identifier | 

### Return type

[**V10CredentialExchange**](V10CredentialExchange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential_records_cred_ex_id_send_request_post**
> V10CredentialExchange issue_credential_records_cred_ex_id_send_request_post(cred_ex_id)

Send issuer a credential request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialV10Api()
cred_ex_id = 'cred_ex_id_example' # str | Credential exchange identifier

try:
    # Send issuer a credential request
    api_response = api_instance.issue_credential_records_cred_ex_id_send_request_post(cred_ex_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialV10Api->issue_credential_records_cred_ex_id_send_request_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_ex_id** | **str**| Credential exchange identifier | 

### Return type

[**V10CredentialExchange**](V10CredentialExchange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential_records_cred_ex_id_store_post**
> V10CredentialExchange issue_credential_records_cred_ex_id_store_post(cred_ex_id, body=body)

Store a received credential

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialV10Api()
cred_ex_id = 'cred_ex_id_example' # str | Credential exchange identifier
body = swagger_client.V10CredentialStoreRequest() # V10CredentialStoreRequest |  (optional)

try:
    # Store a received credential
    api_response = api_instance.issue_credential_records_cred_ex_id_store_post(cred_ex_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialV10Api->issue_credential_records_cred_ex_id_store_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_ex_id** | **str**| Credential exchange identifier | 
 **body** | [**V10CredentialStoreRequest**](V10CredentialStoreRequest.md)|  | [optional] 

### Return type

[**V10CredentialExchange**](V10CredentialExchange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential_records_get**
> V10CredentialExchangeListResult issue_credential_records_get(connection_id=connection_id, role=role, state=state, thread_id=thread_id)

Fetch all credential exchange records

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialV10Api()
connection_id = 'connection_id_example' # str | Connection identifier (optional)
role = 'role_example' # str | Role assigned in credential exchange (optional)
state = 'state_example' # str | Credential exchange state (optional)
thread_id = 'thread_id_example' # str | Thread identifier (optional)

try:
    # Fetch all credential exchange records
    api_response = api_instance.issue_credential_records_get(connection_id=connection_id, role=role, state=state, thread_id=thread_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialV10Api->issue_credential_records_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | [**str**](.md)| Connection identifier | [optional] 
 **role** | **str**| Role assigned in credential exchange | [optional] 
 **state** | **str**| Credential exchange state | [optional] 
 **thread_id** | [**str**](.md)| Thread identifier | [optional] 

### Return type

[**V10CredentialExchangeListResult**](V10CredentialExchangeListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential_send_offer_post**
> V10CredentialExchange issue_credential_send_offer_post(body=body)

Send holder a credential offer, independent of any proposal

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialV10Api()
body = swagger_client.V10CredentialOfferRequest() # V10CredentialOfferRequest |  (optional)

try:
    # Send holder a credential offer, independent of any proposal
    api_response = api_instance.issue_credential_send_offer_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialV10Api->issue_credential_send_offer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V10CredentialOfferRequest**](V10CredentialOfferRequest.md)|  | [optional] 

### Return type

[**V10CredentialExchange**](V10CredentialExchange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential_send_post**
> V10CredentialExchange issue_credential_send_post(body=body)

Send holder a credential, automating entire flow

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialV10Api()
body = swagger_client.V10CredentialProposalRequestMand() # V10CredentialProposalRequestMand |  (optional)

try:
    # Send holder a credential, automating entire flow
    api_response = api_instance.issue_credential_send_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialV10Api->issue_credential_send_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V10CredentialProposalRequestMand**](V10CredentialProposalRequestMand.md)|  | [optional] 

### Return type

[**V10CredentialExchange**](V10CredentialExchange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential_send_proposal_post**
> V10CredentialExchange issue_credential_send_proposal_post(body=body)

Send issuer a credential proposal

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialV10Api()
body = swagger_client.V10CredentialProposalRequestOpt() # V10CredentialProposalRequestOpt |  (optional)

try:
    # Send issuer a credential proposal
    api_response = api_instance.issue_credential_send_proposal_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialV10Api->issue_credential_send_proposal_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V10CredentialProposalRequestOpt**](V10CredentialProposalRequestOpt.md)|  | [optional] 

### Return type

[**V10CredentialExchange**](V10CredentialExchange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

