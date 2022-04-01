# IndyProofReqAttrSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Attribute name | [optional] 
**names** | **list[str]** | Attribute name group | [optional] 
**non_revoked** | [**IndyProofReqNonRevoked**](IndyProofReqNonRevoked.md) |  | [optional] 
**restrictions** | **list[dict(str, str)]** | If present, credential must satisfy one of given restrictions: specify schema_id, schema_issuer_did, schema_name, schema_version, issuer_did, cred_def_id, and/or attr::&lt;attribute-name&gt;::value where &lt;attribute-name&gt; represents a credential attribute name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


