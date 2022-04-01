# Agent API

## Version Number
- API version: v0.1.0
- Package version: 0.1.0

## Requirements.

Python 2.7 and 3.4+


## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ActionMenuApi* | [**action_menu_conn_id_close_post**](docs/ActionMenuApi.md#action_menu_conn_id_close_post) | **POST** /action-menu/{conn_id}/close | Close the active menu associated with a connection
*ActionMenuApi* | [**action_menu_conn_id_fetch_post**](docs/ActionMenuApi.md#action_menu_conn_id_fetch_post) | **POST** /action-menu/{conn_id}/fetch | Fetch the active menu
*ActionMenuApi* | [**action_menu_conn_id_perform_post**](docs/ActionMenuApi.md#action_menu_conn_id_perform_post) | **POST** /action-menu/{conn_id}/perform | Perform an action associated with the active menu
*ActionMenuApi* | [**action_menu_conn_id_request_post**](docs/ActionMenuApi.md#action_menu_conn_id_request_post) | **POST** /action-menu/{conn_id}/request | Request the active menu
*ActionMenuApi* | [**action_menu_conn_id_send_menu_post**](docs/ActionMenuApi.md#action_menu_conn_id_send_menu_post) | **POST** /action-menu/{conn_id}/send-menu | Send an action menu to a connection
*BasicmessageApi* | [**connections_conn_id_send_message_post**](docs/BasicmessageApi.md#connections_conn_id_send_message_post) | **POST** /connections/{conn_id}/send-message | Send a basic message to a connection
*ConnectionApi* | [**connections_conn_id_accept_invitation_post**](docs/ConnectionApi.md#connections_conn_id_accept_invitation_post) | **POST** /connections/{conn_id}/accept-invitation | Accept a stored connection invitation
*ConnectionApi* | [**connections_conn_id_accept_request_post**](docs/ConnectionApi.md#connections_conn_id_accept_request_post) | **POST** /connections/{conn_id}/accept-request | Accept a stored connection request
*ConnectionApi* | [**connections_conn_id_delete**](docs/ConnectionApi.md#connections_conn_id_delete) | **DELETE** /connections/{conn_id} | Remove an existing connection record
*ConnectionApi* | [**connections_conn_id_endpoints_get**](docs/ConnectionApi.md#connections_conn_id_endpoints_get) | **GET** /connections/{conn_id}/endpoints | Fetch connection remote endpoint
*ConnectionApi* | [**connections_conn_id_establish_inbound_ref_id_post**](docs/ConnectionApi.md#connections_conn_id_establish_inbound_ref_id_post) | **POST** /connections/{conn_id}/establish-inbound/{ref_id} | Assign another connection as the inbound connection
*ConnectionApi* | [**connections_conn_id_get**](docs/ConnectionApi.md#connections_conn_id_get) | **GET** /connections/{conn_id} | Fetch a single connection record
*ConnectionApi* | [**connections_conn_id_metadata_get**](docs/ConnectionApi.md#connections_conn_id_metadata_get) | **GET** /connections/{conn_id}/metadata | Fetch connection metadata
*ConnectionApi* | [**connections_conn_id_metadata_post**](docs/ConnectionApi.md#connections_conn_id_metadata_post) | **POST** /connections/{conn_id}/metadata | Set connection metadata
*ConnectionApi* | [**connections_create_invitation_post**](docs/ConnectionApi.md#connections_create_invitation_post) | **POST** /connections/create-invitation | Create a new connection invitation
*ConnectionApi* | [**connections_create_static_post**](docs/ConnectionApi.md#connections_create_static_post) | **POST** /connections/create-static | Create a new static connection
*ConnectionApi* | [**connections_get**](docs/ConnectionApi.md#connections_get) | **GET** /connections | Query agent-to-agent connections
*ConnectionApi* | [**connections_receive_invitation_post**](docs/ConnectionApi.md#connections_receive_invitation_post) | **POST** /connections/receive-invitation | Receive a new connection invitation
*CredentialDefinitionApi* | [**credential_definitions_created_get**](docs/CredentialDefinitionApi.md#credential_definitions_created_get) | **GET** /credential-definitions/created | Search for matching credential definitions that agent originated
*CredentialDefinitionApi* | [**credential_definitions_cred_def_id_get**](docs/CredentialDefinitionApi.md#credential_definitions_cred_def_id_get) | **GET** /credential-definitions/{cred_def_id} | Gets a credential definition from the ledger
*CredentialDefinitionApi* | [**credential_definitions_post**](docs/CredentialDefinitionApi.md#credential_definitions_post) | **POST** /credential-definitions | Sends a credential definition to the ledger
*CredentialsApi* | [**credential_credential_id_delete**](docs/CredentialsApi.md#credential_credential_id_delete) | **DELETE** /credential/{credential_id} | Remove a credential from the wallet by id
*CredentialsApi* | [**credential_credential_id_get**](docs/CredentialsApi.md#credential_credential_id_get) | **GET** /credential/{credential_id} | Fetch a credential from wallet by id
*CredentialsApi* | [**credential_mime_types_credential_id_get**](docs/CredentialsApi.md#credential_mime_types_credential_id_get) | **GET** /credential/mime-types/{credential_id} | Get attribute MIME types from wallet
*CredentialsApi* | [**credential_revoked_credential_id_get**](docs/CredentialsApi.md#credential_revoked_credential_id_get) | **GET** /credential/revoked/{credential_id} | Query credential revocation status by id
*CredentialsApi* | [**credentials_get**](docs/CredentialsApi.md#credentials_get) | **GET** /credentials | Fetch credentials from wallet
*DidExchangeApi* | [**didexchange_conn_id_accept_invitation_post**](docs/DidExchangeApi.md#didexchange_conn_id_accept_invitation_post) | **POST** /didexchange/{conn_id}/accept-invitation | Accept a stored connection invitation
*DidExchangeApi* | [**didexchange_conn_id_accept_request_post**](docs/DidExchangeApi.md#didexchange_conn_id_accept_request_post) | **POST** /didexchange/{conn_id}/accept-request | Accept a stored connection request
*DidExchangeApi* | [**didexchange_create_request_post**](docs/DidExchangeApi.md#didexchange_create_request_post) | **POST** /didexchange/create-request | Create request against public DID&#39;s implicit invitation
*DidExchangeApi* | [**didexchange_receive_request_post**](docs/DidExchangeApi.md#didexchange_receive_request_post) | **POST** /didexchange/receive-request | Receive request against public DID&#39;s implicit invitation
*IntroductionApi* | [**connections_conn_id_start_introduction_post**](docs/IntroductionApi.md#connections_conn_id_start_introduction_post) | **POST** /connections/{conn_id}/start-introduction | Start an introduction between two connections
*IssueCredentialV10Api* | [**issue_credential_create_post**](docs/IssueCredentialV10Api.md#issue_credential_create_post) | **POST** /issue-credential/create | Send holder a credential, automating entire flow
*IssueCredentialV10Api* | [**issue_credential_records_cred_ex_id_delete**](docs/IssueCredentialV10Api.md#issue_credential_records_cred_ex_id_delete) | **DELETE** /issue-credential/records/{cred_ex_id} | Remove an existing credential exchange record
*IssueCredentialV10Api* | [**issue_credential_records_cred_ex_id_get**](docs/IssueCredentialV10Api.md#issue_credential_records_cred_ex_id_get) | **GET** /issue-credential/records/{cred_ex_id} | Fetch a single credential exchange record
*IssueCredentialV10Api* | [**issue_credential_records_cred_ex_id_issue_post**](docs/IssueCredentialV10Api.md#issue_credential_records_cred_ex_id_issue_post) | **POST** /issue-credential/records/{cred_ex_id}/issue | Send holder a credential
*IssueCredentialV10Api* | [**issue_credential_records_cred_ex_id_problem_report_post**](docs/IssueCredentialV10Api.md#issue_credential_records_cred_ex_id_problem_report_post) | **POST** /issue-credential/records/{cred_ex_id}/problem-report | Send a problem report for credential exchange
*IssueCredentialV10Api* | [**issue_credential_records_cred_ex_id_send_offer_post**](docs/IssueCredentialV10Api.md#issue_credential_records_cred_ex_id_send_offer_post) | **POST** /issue-credential/records/{cred_ex_id}/send-offer | Send holder a credential offer in reference to a proposal with preview
*IssueCredentialV10Api* | [**issue_credential_records_cred_ex_id_send_request_post**](docs/IssueCredentialV10Api.md#issue_credential_records_cred_ex_id_send_request_post) | **POST** /issue-credential/records/{cred_ex_id}/send-request | Send issuer a credential request
*IssueCredentialV10Api* | [**issue_credential_records_cred_ex_id_store_post**](docs/IssueCredentialV10Api.md#issue_credential_records_cred_ex_id_store_post) | **POST** /issue-credential/records/{cred_ex_id}/store | Store a received credential
*IssueCredentialV10Api* | [**issue_credential_records_get**](docs/IssueCredentialV10Api.md#issue_credential_records_get) | **GET** /issue-credential/records | Fetch all credential exchange records
*IssueCredentialV10Api* | [**issue_credential_send_offer_post**](docs/IssueCredentialV10Api.md#issue_credential_send_offer_post) | **POST** /issue-credential/send-offer | Send holder a credential offer, independent of any proposal
*IssueCredentialV10Api* | [**issue_credential_send_post**](docs/IssueCredentialV10Api.md#issue_credential_send_post) | **POST** /issue-credential/send | Send holder a credential, automating entire flow
*IssueCredentialV10Api* | [**issue_credential_send_proposal_post**](docs/IssueCredentialV10Api.md#issue_credential_send_proposal_post) | **POST** /issue-credential/send-proposal | Send issuer a credential proposal
*IssueCredentialV20Api* | [**issue_credential20_create_post**](docs/IssueCredentialV20Api.md#issue_credential20_create_post) | **POST** /issue-credential-2.0/create | Send holder a credential, automating entire flow
*IssueCredentialV20Api* | [**issue_credential20_records_cred_ex_id_delete**](docs/IssueCredentialV20Api.md#issue_credential20_records_cred_ex_id_delete) | **DELETE** /issue-credential-2.0/records/{cred_ex_id} | Remove an existing credential exchange record
*IssueCredentialV20Api* | [**issue_credential20_records_cred_ex_id_get**](docs/IssueCredentialV20Api.md#issue_credential20_records_cred_ex_id_get) | **GET** /issue-credential-2.0/records/{cred_ex_id} | Fetch a single credential exchange record
*IssueCredentialV20Api* | [**issue_credential20_records_cred_ex_id_issue_post**](docs/IssueCredentialV20Api.md#issue_credential20_records_cred_ex_id_issue_post) | **POST** /issue-credential-2.0/records/{cred_ex_id}/issue | Send holder a credential
*IssueCredentialV20Api* | [**issue_credential20_records_cred_ex_id_problem_report_post**](docs/IssueCredentialV20Api.md#issue_credential20_records_cred_ex_id_problem_report_post) | **POST** /issue-credential-2.0/records/{cred_ex_id}/problem-report | Send a problem report for credential exchange
*IssueCredentialV20Api* | [**issue_credential20_records_cred_ex_id_send_offer_post**](docs/IssueCredentialV20Api.md#issue_credential20_records_cred_ex_id_send_offer_post) | **POST** /issue-credential-2.0/records/{cred_ex_id}/send-offer | Send holder a credential offer in reference to a proposal with preview
*IssueCredentialV20Api* | [**issue_credential20_records_cred_ex_id_send_request_post**](docs/IssueCredentialV20Api.md#issue_credential20_records_cred_ex_id_send_request_post) | **POST** /issue-credential-2.0/records/{cred_ex_id}/send-request | Send issuer a credential request
*IssueCredentialV20Api* | [**issue_credential20_records_cred_ex_id_store_post**](docs/IssueCredentialV20Api.md#issue_credential20_records_cred_ex_id_store_post) | **POST** /issue-credential-2.0/records/{cred_ex_id}/store | Store a received credential
*IssueCredentialV20Api* | [**issue_credential20_records_get**](docs/IssueCredentialV20Api.md#issue_credential20_records_get) | **GET** /issue-credential-2.0/records | Fetch all credential exchange records
*IssueCredentialV20Api* | [**issue_credential20_send_offer_post**](docs/IssueCredentialV20Api.md#issue_credential20_send_offer_post) | **POST** /issue-credential-2.0/send-offer | Send holder a credential offer, independent of any proposal
*IssueCredentialV20Api* | [**issue_credential20_send_post**](docs/IssueCredentialV20Api.md#issue_credential20_send_post) | **POST** /issue-credential-2.0/send | Send holder a credential, automating entire flow
*IssueCredentialV20Api* | [**issue_credential20_send_proposal_post**](docs/IssueCredentialV20Api.md#issue_credential20_send_proposal_post) | **POST** /issue-credential-2.0/send-proposal | Send issuer a credential proposal
*LedgerApi* | [**ledger_did_endpoint_get**](docs/LedgerApi.md#ledger_did_endpoint_get) | **GET** /ledger/did-endpoint | Get the endpoint for a DID from the ledger.
*LedgerApi* | [**ledger_did_verkey_get**](docs/LedgerApi.md#ledger_did_verkey_get) | **GET** /ledger/did-verkey | Get the verkey for a DID from the ledger.
*LedgerApi* | [**ledger_get_nym_role_get**](docs/LedgerApi.md#ledger_get_nym_role_get) | **GET** /ledger/get-nym-role | Get the role from the NYM registration of a public DID.
*LedgerApi* | [**ledger_register_nym_post**](docs/LedgerApi.md#ledger_register_nym_post) | **POST** /ledger/register-nym | Send a NYM registration to the ledger.
*LedgerApi* | [**ledger_rotate_public_did_keypair_patch**](docs/LedgerApi.md#ledger_rotate_public_did_keypair_patch) | **PATCH** /ledger/rotate-public-did-keypair | Rotate key pair for public DID.
*LedgerApi* | [**ledger_taa_accept_post**](docs/LedgerApi.md#ledger_taa_accept_post) | **POST** /ledger/taa/accept | Accept the transaction author agreement
*LedgerApi* | [**ledger_taa_get**](docs/LedgerApi.md#ledger_taa_get) | **GET** /ledger/taa | Fetch the current transaction author agreement, if any
*MediationApi* | [**mediation_default_mediator_delete**](docs/MediationApi.md#mediation_default_mediator_delete) | **DELETE** /mediation/default-mediator | Clear default mediator
*MediationApi* | [**mediation_default_mediator_get**](docs/MediationApi.md#mediation_default_mediator_get) | **GET** /mediation/default-mediator | Get default mediator
*MediationApi* | [**mediation_keylists_get**](docs/MediationApi.md#mediation_keylists_get) | **GET** /mediation/keylists | Retrieve keylists by connection or role
*MediationApi* | [**mediation_keylists_mediation_id_send_keylist_query_post**](docs/MediationApi.md#mediation_keylists_mediation_id_send_keylist_query_post) | **POST** /mediation/keylists/{mediation_id}/send-keylist-query | Send keylist query to mediator
*MediationApi* | [**mediation_keylists_mediation_id_send_keylist_update_post**](docs/MediationApi.md#mediation_keylists_mediation_id_send_keylist_update_post) | **POST** /mediation/keylists/{mediation_id}/send-keylist-update | Send keylist update to mediator
*MediationApi* | [**mediation_mediation_id_default_mediator_put**](docs/MediationApi.md#mediation_mediation_id_default_mediator_put) | **PUT** /mediation/{mediation_id}/default-mediator | Set default mediator
*MediationApi* | [**mediation_request_conn_id_post**](docs/MediationApi.md#mediation_request_conn_id_post) | **POST** /mediation/request/{conn_id} | Request mediation from connection
*MediationApi* | [**mediation_requests_get**](docs/MediationApi.md#mediation_requests_get) | **GET** /mediation/requests | Query mediation requests, returns list of all mediation records
*MediationApi* | [**mediation_requests_mediation_id_delete**](docs/MediationApi.md#mediation_requests_mediation_id_delete) | **DELETE** /mediation/requests/{mediation_id} | Delete mediation request by ID
*MediationApi* | [**mediation_requests_mediation_id_deny_post**](docs/MediationApi.md#mediation_requests_mediation_id_deny_post) | **POST** /mediation/requests/{mediation_id}/deny | Deny a stored mediation request
*MediationApi* | [**mediation_requests_mediation_id_get**](docs/MediationApi.md#mediation_requests_mediation_id_get) | **GET** /mediation/requests/{mediation_id} | Retrieve mediation request record
*MediationApi* | [**mediation_requests_mediation_id_grant_post**](docs/MediationApi.md#mediation_requests_mediation_id_grant_post) | **POST** /mediation/requests/{mediation_id}/grant | Grant received mediation
*OutOfBandApi* | [**out_of_band_create_invitation_post**](docs/OutOfBandApi.md#out_of_band_create_invitation_post) | **POST** /out-of-band/create-invitation | Create a new connection invitation
*OutOfBandApi* | [**out_of_band_receive_invitation_post**](docs/OutOfBandApi.md#out_of_band_receive_invitation_post) | **POST** /out-of-band/receive-invitation | Receive a new connection invitation
*PresentProofApi* | [**present_proof_create_request_post**](docs/PresentProofApi.md#present_proof_create_request_post) | **POST** /present-proof/create-request |      Creates a presentation request not bound to any proposal or existing connection     
*PresentProofApi* | [**present_proof_records_get**](docs/PresentProofApi.md#present_proof_records_get) | **GET** /present-proof/records | Fetch all present-proof exchange records
*PresentProofApi* | [**present_proof_records_pres_ex_id_credentials_get**](docs/PresentProofApi.md#present_proof_records_pres_ex_id_credentials_get) | **GET** /present-proof/records/{pres_ex_id}/credentials | Fetch credentials for a presentation request from wallet
*PresentProofApi* | [**present_proof_records_pres_ex_id_delete**](docs/PresentProofApi.md#present_proof_records_pres_ex_id_delete) | **DELETE** /present-proof/records/{pres_ex_id} | Remove an existing presentation exchange record
*PresentProofApi* | [**present_proof_records_pres_ex_id_get**](docs/PresentProofApi.md#present_proof_records_pres_ex_id_get) | **GET** /present-proof/records/{pres_ex_id} | Fetch a single presentation exchange record
*PresentProofApi* | [**present_proof_records_pres_ex_id_problem_report_post**](docs/PresentProofApi.md#present_proof_records_pres_ex_id_problem_report_post) | **POST** /present-proof/records/{pres_ex_id}/problem-report | Send a problem report for presentation exchange
*PresentProofApi* | [**present_proof_records_pres_ex_id_send_presentation_post**](docs/PresentProofApi.md#present_proof_records_pres_ex_id_send_presentation_post) | **POST** /present-proof/records/{pres_ex_id}/send-presentation | Sends a proof presentation
*PresentProofApi* | [**present_proof_records_pres_ex_id_send_request_post**](docs/PresentProofApi.md#present_proof_records_pres_ex_id_send_request_post) | **POST** /present-proof/records/{pres_ex_id}/send-request | Sends a presentation request in reference to a proposal
*PresentProofApi* | [**present_proof_records_pres_ex_id_verify_presentation_post**](docs/PresentProofApi.md#present_proof_records_pres_ex_id_verify_presentation_post) | **POST** /present-proof/records/{pres_ex_id}/verify-presentation | Verify a received presentation
*PresentProofApi* | [**present_proof_send_proposal_post**](docs/PresentProofApi.md#present_proof_send_proposal_post) | **POST** /present-proof/send-proposal | Sends a presentation proposal
*PresentProofApi* | [**present_proof_send_request_post**](docs/PresentProofApi.md#present_proof_send_request_post) | **POST** /present-proof/send-request | Sends a free presentation request not bound to any proposal
*RevocationApi* | [**revocation_active_registry_cred_def_id_get**](docs/RevocationApi.md#revocation_active_registry_cred_def_id_get) | **GET** /revocation/active-registry/{cred_def_id} | Get current active revocation registry by credential definition id
*RevocationApi* | [**revocation_clear_pending_revocations_post**](docs/RevocationApi.md#revocation_clear_pending_revocations_post) | **POST** /revocation/clear-pending-revocations | Clear pending revocations
*RevocationApi* | [**revocation_create_registry_post**](docs/RevocationApi.md#revocation_create_registry_post) | **POST** /revocation/create-registry | Creates a new revocation registry
*RevocationApi* | [**revocation_credential_record_get**](docs/RevocationApi.md#revocation_credential_record_get) | **GET** /revocation/credential-record | Get credential revocation status
*RevocationApi* | [**revocation_publish_revocations_post**](docs/RevocationApi.md#revocation_publish_revocations_post) | **POST** /revocation/publish-revocations | Publish pending revocations to ledger
*RevocationApi* | [**revocation_registries_created_get**](docs/RevocationApi.md#revocation_registries_created_get) | **GET** /revocation/registries/created | Search for matching revocation registries that current agent created
*RevocationApi* | [**revocation_registry_rev_reg_id_definition_post**](docs/RevocationApi.md#revocation_registry_rev_reg_id_definition_post) | **POST** /revocation/registry/{rev_reg_id}/definition | Send revocation registry definition to ledger
*RevocationApi* | [**revocation_registry_rev_reg_id_entry_post**](docs/RevocationApi.md#revocation_registry_rev_reg_id_entry_post) | **POST** /revocation/registry/{rev_reg_id}/entry | Send revocation registry entry to ledger
*RevocationApi* | [**revocation_registry_rev_reg_id_get**](docs/RevocationApi.md#revocation_registry_rev_reg_id_get) | **GET** /revocation/registry/{rev_reg_id} | Get revocation registry by revocation registry id
*RevocationApi* | [**revocation_registry_rev_reg_id_issued_get**](docs/RevocationApi.md#revocation_registry_rev_reg_id_issued_get) | **GET** /revocation/registry/{rev_reg_id}/issued | Get number of credentials issued against revocation registry
*RevocationApi* | [**revocation_registry_rev_reg_id_patch**](docs/RevocationApi.md#revocation_registry_rev_reg_id_patch) | **PATCH** /revocation/registry/{rev_reg_id} | Update revocation registry with new public URI to its tails file
*RevocationApi* | [**revocation_registry_rev_reg_id_set_state_patch**](docs/RevocationApi.md#revocation_registry_rev_reg_id_set_state_patch) | **PATCH** /revocation/registry/{rev_reg_id}/set-state | Set revocation registry state manually
*RevocationApi* | [**revocation_registry_rev_reg_id_tails_file_get**](docs/RevocationApi.md#revocation_registry_rev_reg_id_tails_file_get) | **GET** /revocation/registry/{rev_reg_id}/tails-file | Download tails file
*RevocationApi* | [**revocation_registry_rev_reg_id_tails_file_put**](docs/RevocationApi.md#revocation_registry_rev_reg_id_tails_file_put) | **PUT** /revocation/registry/{rev_reg_id}/tails-file | Upload local tails file to server
*RevocationApi* | [**revocation_revoke_post**](docs/RevocationApi.md#revocation_revoke_post) | **POST** /revocation/revoke | Revoke an issued credential
*SchemaApi* | [**schemas_created_get**](docs/SchemaApi.md#schemas_created_get) | **GET** /schemas/created | Search for matching schema that agent originated
*SchemaApi* | [**schemas_post**](docs/SchemaApi.md#schemas_post) | **POST** /schemas | Sends a schema to the ledger
*SchemaApi* | [**schemas_schema_id_get**](docs/SchemaApi.md#schemas_schema_id_get) | **GET** /schemas/{schema_id} | Gets a schema from the ledger
*ServerApi* | [**features_get**](docs/ServerApi.md#features_get) | **GET** /features | Query supported features
*ServerApi* | [**plugins_get**](docs/ServerApi.md#plugins_get) | **GET** /plugins | Fetch the list of loaded plugins
*ServerApi* | [**shutdown_get**](docs/ServerApi.md#shutdown_get) | **GET** /shutdown | Shut down server
*ServerApi* | [**status_get**](docs/ServerApi.md#status_get) | **GET** /status | Fetch the server status
*ServerApi* | [**status_live_get**](docs/ServerApi.md#status_live_get) | **GET** /status/live | Liveliness check
*ServerApi* | [**status_ready_get**](docs/ServerApi.md#status_ready_get) | **GET** /status/ready | Readiness check
*ServerApi* | [**status_reset_post**](docs/ServerApi.md#status_reset_post) | **POST** /status/reset | Reset statistics
*TrustpingApi* | [**connections_conn_id_send_ping_post**](docs/TrustpingApi.md#connections_conn_id_send_ping_post) | **POST** /connections/{conn_id}/send-ping | Send a trust ping to a connection
*WalletApi* | [**wallet_did_create_post**](docs/WalletApi.md#wallet_did_create_post) | **POST** /wallet/did/create | Create a local DID
*WalletApi* | [**wallet_did_get**](docs/WalletApi.md#wallet_did_get) | **GET** /wallet/did | List wallet DIDs
*WalletApi* | [**wallet_did_local_rotate_keypair_patch**](docs/WalletApi.md#wallet_did_local_rotate_keypair_patch) | **PATCH** /wallet/did/local/rotate-keypair | Rotate keypair for a DID not posted to the ledger
*WalletApi* | [**wallet_did_public_get**](docs/WalletApi.md#wallet_did_public_get) | **GET** /wallet/did/public | Fetch the current public DID
*WalletApi* | [**wallet_did_public_post**](docs/WalletApi.md#wallet_did_public_post) | **POST** /wallet/did/public | Assign the current public DID
*WalletApi* | [**wallet_get_did_endpoint_get**](docs/WalletApi.md#wallet_get_did_endpoint_get) | **GET** /wallet/get-did-endpoint | Query DID endpoint in wallet
*WalletApi* | [**wallet_set_did_endpoint_post**](docs/WalletApi.md#wallet_set_did_endpoint_post) | **POST** /wallet/set-did-endpoint | Update endpoint in wallet and on ledger if posted to it


## Documentation For Models

 - [AMLRecord](docs/AMLRecord.md)
 - [ActionMenuModulesResult](docs/ActionMenuModulesResult.md)
 - [AdminAPIMessageTracing](docs/AdminAPIMessageTracing.md)
 - [AdminMediationDeny](docs/AdminMediationDeny.md)
 - [AdminModules](docs/AdminModules.md)
 - [AdminShutdown](docs/AdminShutdown.md)
 - [AdminStatus](docs/AdminStatus.md)
 - [AdminStatusLiveliness](docs/AdminStatusLiveliness.md)
 - [AdminStatusReadiness](docs/AdminStatusReadiness.md)
 - [AttachDecorator](docs/AttachDecorator.md)
 - [AttachDecoratorData](docs/AttachDecoratorData.md)
 - [AttachDecoratorData1JWS](docs/AttachDecoratorData1JWS.md)
 - [AttachDecoratorDataJWS](docs/AttachDecoratorDataJWS.md)
 - [AttachDecoratorDataJWSHeader](docs/AttachDecoratorDataJWSHeader.md)
 - [AttachmentDef](docs/AttachmentDef.md)
 - [AttributeMimeTypesResult](docs/AttributeMimeTypesResult.md)
 - [BasicMessageModuleResponse](docs/BasicMessageModuleResponse.md)
 - [ClearPendingRevocationsRequest](docs/ClearPendingRevocationsRequest.md)
 - [ConnRecord](docs/ConnRecord.md)
 - [ConnectionInvitation](docs/ConnectionInvitation.md)
 - [ConnectionList](docs/ConnectionList.md)
 - [ConnectionMetadata](docs/ConnectionMetadata.md)
 - [ConnectionMetadataSetRequest](docs/ConnectionMetadataSetRequest.md)
 - [ConnectionModuleResponse](docs/ConnectionModuleResponse.md)
 - [ConnectionStaticRequest](docs/ConnectionStaticRequest.md)
 - [ConnectionStaticResult](docs/ConnectionStaticResult.md)
 - [CreateInvitationRequest](docs/CreateInvitationRequest.md)
 - [CredAttrSpec](docs/CredAttrSpec.md)
 - [CredBrief](docs/CredBrief.md)
 - [CredBriefList](docs/CredBriefList.md)
 - [CredRevRecordResult](docs/CredRevRecordResult.md)
 - [CredRevokedResult](docs/CredRevokedResult.md)
 - [CredentialDefinition](docs/CredentialDefinition.md)
 - [CredentialDefinitionGetResults](docs/CredentialDefinitionGetResults.md)
 - [CredentialDefinitionSendRequest](docs/CredentialDefinitionSendRequest.md)
 - [CredentialDefinitionSendResults](docs/CredentialDefinitionSendResults.md)
 - [CredentialDefinitionsCreatedResults](docs/CredentialDefinitionsCreatedResults.md)
 - [CredentialPreview](docs/CredentialPreview.md)
 - [DID](docs/DID.md)
 - [DIDEndpoint](docs/DIDEndpoint.md)
 - [DIDEndpointWithType](docs/DIDEndpointWithType.md)
 - [DIDList](docs/DIDList.md)
 - [DIDResult](docs/DIDResult.md)
 - [DIDXRequest](docs/DIDXRequest.md)
 - [EndpointsResult](docs/EndpointsResult.md)
 - [HolderModuleResponse](docs/HolderModuleResponse.md)
 - [IndyCredInfo](docs/IndyCredInfo.md)
 - [IndyCredPrecis](docs/IndyCredPrecis.md)
 - [IndyProofReqAttrSpec](docs/IndyProofReqAttrSpec.md)
 - [IndyProofReqNonRevoked](docs/IndyProofReqNonRevoked.md)
 - [IndyProofReqPredSpec](docs/IndyProofReqPredSpec.md)
 - [IndyProofReqPredSpecRestrictions](docs/IndyProofReqPredSpecRestrictions.md)
 - [IndyProofRequest](docs/IndyProofRequest.md)
 - [IndyRequestedCredsRequestedAttr](docs/IndyRequestedCredsRequestedAttr.md)
 - [IndyRequestedCredsRequestedPred](docs/IndyRequestedCredsRequestedPred.md)
 - [IntroModuleResponse](docs/IntroModuleResponse.md)
 - [InvitationCreateRequest](docs/InvitationCreateRequest.md)
 - [InvitationReceiveRequest](docs/InvitationReceiveRequest.md)
 - [InvitationRecord](docs/InvitationRecord.md)
 - [InvitationResult](docs/InvitationResult.md)
 - [IssueCredentialModuleResponse](docs/IssueCredentialModuleResponse.md)
 - [Keylist](docs/Keylist.md)
 - [KeylistQuery](docs/KeylistQuery.md)
 - [KeylistQueryFilterRequest](docs/KeylistQueryFilterRequest.md)
 - [KeylistQueryPaginate](docs/KeylistQueryPaginate.md)
 - [KeylistUpdate](docs/KeylistUpdate.md)
 - [KeylistUpdateRequest](docs/KeylistUpdateRequest.md)
 - [KeylistUpdateRule](docs/KeylistUpdateRule.md)
 - [LedgerModulesResult](docs/LedgerModulesResult.md)
 - [MediationCreateRequest](docs/MediationCreateRequest.md)
 - [MediationDeny](docs/MediationDeny.md)
 - [MediationGrant](docs/MediationGrant.md)
 - [MediationList](docs/MediationList.md)
 - [MediationRecord](docs/MediationRecord.md)
 - [MenuForm](docs/MenuForm.md)
 - [MenuFormParam](docs/MenuFormParam.md)
 - [MenuJson](docs/MenuJson.md)
 - [MenuOption](docs/MenuOption.md)
 - [PerformRequest](docs/PerformRequest.md)
 - [PingRequest](docs/PingRequest.md)
 - [PingRequestResponse](docs/PingRequestResponse.md)
 - [PresAttrSpec](docs/PresAttrSpec.md)
 - [PresPredSpec](docs/PresPredSpec.md)
 - [PresentProofModuleResponse](docs/PresentProofModuleResponse.md)
 - [PresentationPreview](docs/PresentationPreview.md)
 - [PublishRevocations](docs/PublishRevocations.md)
 - [QueryResult](docs/QueryResult.md)
 - [ReceiveInvitationRequest](docs/ReceiveInvitationRequest.md)
 - [RevRegCreateRequest](docs/RevRegCreateRequest.md)
 - [RevRegIssuedResult](docs/RevRegIssuedResult.md)
 - [RevRegResult](docs/RevRegResult.md)
 - [RevRegUpdateTailsFileUri](docs/RevRegUpdateTailsFileUri.md)
 - [RevRegsCreated](docs/RevRegsCreated.md)
 - [RevocationModuleResponse](docs/RevocationModuleResponse.md)
 - [RevokeRequest](docs/RevokeRequest.md)
 - [RouteRecord](docs/RouteRecord.md)
 - [Schema](docs/Schema.md)
 - [SchemaGetResults](docs/SchemaGetResults.md)
 - [SchemaSendRequest](docs/SchemaSendRequest.md)
 - [SchemaSendResults](docs/SchemaSendResults.md)
 - [SchemasCreatedResults](docs/SchemasCreatedResults.md)
 - [SendMenu](docs/SendMenu.md)
 - [SendMessage](docs/SendMessage.md)
 - [Service](docs/Service.md)
 - [TAAAccept](docs/TAAAccept.md)
 - [TAAAcceptance](docs/TAAAcceptance.md)
 - [TAAInfo](docs/TAAInfo.md)
 - [TAARecord](docs/TAARecord.md)
 - [TAAResult](docs/TAAResult.md)
 - [V10CredentialCreate](docs/V10CredentialCreate.md)
 - [V10CredentialExchange](docs/V10CredentialExchange.md)
 - [V10CredentialExchangeListResult](docs/V10CredentialExchangeListResult.md)
 - [V10CredentialIssueRequest](docs/V10CredentialIssueRequest.md)
 - [V10CredentialOfferRequest](docs/V10CredentialOfferRequest.md)
 - [V10CredentialProblemReportRequest](docs/V10CredentialProblemReportRequest.md)
 - [V10CredentialProposalRequestMand](docs/V10CredentialProposalRequestMand.md)
 - [V10CredentialProposalRequestOpt](docs/V10CredentialProposalRequestOpt.md)
 - [V10CredentialStoreRequest](docs/V10CredentialStoreRequest.md)
 - [V10PresentationCreateRequestRequest](docs/V10PresentationCreateRequestRequest.md)
 - [V10PresentationExchange](docs/V10PresentationExchange.md)
 - [V10PresentationExchangeList](docs/V10PresentationExchangeList.md)
 - [V10PresentationProblemReportRequest](docs/V10PresentationProblemReportRequest.md)
 - [V10PresentationProposalRequest](docs/V10PresentationProposalRequest.md)
 - [V10PresentationRequest](docs/V10PresentationRequest.md)
 - [V10PresentationSendRequestRequest](docs/V10PresentationSendRequestRequest.md)
 - [V20CredAttrSpec](docs/V20CredAttrSpec.md)
 - [V20CredCreate](docs/V20CredCreate.md)
 - [V20CredExRecord](docs/V20CredExRecord.md)
 - [V20CredExRecordDIF](docs/V20CredExRecordDIF.md)
 - [V20CredExRecordDetail](docs/V20CredExRecordDetail.md)
 - [V20CredExRecordIndy](docs/V20CredExRecordIndy.md)
 - [V20CredExRecordListResult](docs/V20CredExRecordListResult.md)
 - [V20CredFilter](docs/V20CredFilter.md)
 - [V20CredFilterDIF](docs/V20CredFilterDIF.md)
 - [V20CredFilterIndy](docs/V20CredFilterIndy.md)
 - [V20CredIssueProblemReportRequest](docs/V20CredIssueProblemReportRequest.md)
 - [V20CredIssueRequest](docs/V20CredIssueRequest.md)
 - [V20CredOfferRequest](docs/V20CredOfferRequest.md)
 - [V20CredPreview](docs/V20CredPreview.md)
 - [V20CredProposalRequestPreviewMand](docs/V20CredProposalRequestPreviewMand.md)
 - [V20CredProposalRequestPreviewOpt](docs/V20CredProposalRequestPreviewOpt.md)
 - [V20CredStoreRequest](docs/V20CredStoreRequest.md)
 - [V20IssueCredentialModuleResponse](docs/V20IssueCredentialModuleResponse.md)
 - [WalletModuleResponse](docs/WalletModuleResponse.md)


## Documentation For Authorization

 All endpoints do not require authorization.





