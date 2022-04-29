@RFC0453 @AIP20
Feature: RFC 0453 Aries Agent Issue Credential v2

  @T001-RFC0453 @RFC0592 @critical @AcceptanceTest @DIDExchangeConnection @CredFormat_Indy @Schema_DriversLicense_v2
  Scenario Outline: Issue a Indy credential with the Holder beginning with a proposal
    Given "2" agents
      | name | role   |
      | DMV | issuer |
      | Bob  | holder |
    Given "DMV" has a public did
    And "DMV" is ready to issue a credential
    And "DMV" and "Bob" have an existing connection
    When "Bob" proposes a "indy" credential to "DMV" with <credential_data>
    And "DMV" offers the "indy" credential
    And "Bob" requests the "indy" credential
    And "DMV" issues the "indy" credential
    And "Bob" acknowledges the "indy" credential issue
    Then "Bob" has the "indy" credential issued

    Examples:
      | credential_data   |
      | Data_DL_MaxValues |

  @T001.1-RFC0453 @RFC0593 @critical @AcceptanceTest @DIDExchangeConnection @CredFormat_JSON-LD @Schema_DriversLicense_v2
  Scenario Outline: Issue a JSON-LD credential with the Holder beginning with a proposal
    Given "2" agents
      | name | role   |
      | DMV | issuer |
      | Bob  | holder |
    And "DMV" is ready to issue a "json-ld" credential
    And "DMV" and "Bob" have an existing connection
    When "Bob" proposes a "json-ld" credential to "DMV" with <credential_data>
    And "DMV" offers the "json-ld" credential
    And "Bob" requests the "json-ld" credential
    And "DMV" issues the "json-ld" credential
    And "Bob" acknowledges the "json-ld" credential issue
    Then "Bob" has the "json-ld" credential issued

    @ProofType_Ed25519Signature2018 @DidMethod_sov
    Examples:
      | credential_data   |
      | Data_DL_MaxValues |

    @ProofType_Ed25519Signature2018 @DidMethod_key
    Examples:
      | credential_data   |
      | Data_DL_MaxValues |

    @ProofType_BbsBlsSignature2020 @DidMethod_key
    Examples:
      | credential_data   |
      | Data_DL_MaxValues |

    @ProofType_Ed25519Signature2018 @DidMethod_orb
    Examples:
      | credential_data   |
      | Data_DL_MaxValues |

    @ProofType_BbsBlsSignature2020 @DidMethod_orb
    Examples:
      | credential_data   |
      | Data_DL_MaxValues |

`
