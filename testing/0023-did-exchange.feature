@RFC0023 @AIP20
Feature: RFC 0023 Establishing Connections with DID Exchange
   In order establish a connection with two parties,
   As a responder or a requester,
   I want to use DID Exchange(RFC0023) and Out of Band(RFC0434) protocols to accomplish this.


   @T001-RFC0023 @critical @AcceptanceTest
   Scenario: Establish a connection with DID Exchange between two agents with an explicit invitation
      Given we have "2" agents
         | name | role      |
         | DMV | requester |
         | Bob  | responder |
      When "Bob" sends an explicit invitation to "DMV"
      And "DMV" receives the invitation
      And "DMV" sends the request to "Bob"
      And "Bob" receives the request
      And "Bob" sends a response to "DMV"
      And "DMV" receives the response
      And "DMV" sends complete to "Bob"
      Then "DMV" and "Bob" have a connection

   #@T002-RFC0023 @critical @AcceptanceTest @Deprecated
   #Scenario: Establish a connection with DID Exchange between two agents with an explicit invitation with role reversal

   @T003-RFC0023 @normal @AcceptanceTest
   Scenario: Establish a connection with DID Exchange between two agents with an explicit invitation with a public DID
      Given we have "2" agents
         | name | role      |
         | DMV | requester |
         | Bob  | responder |
      When "Bob" sends an explicit invitation with a public DID to "DMV"
      And "DMV" receives the invitation
      And "DMV" sends the request to "Bob"
      And "Bob" receives the request
      And "Bob" sends a response to "DMV"
      And "DMV" receives the response
      And "DMV" sends complete to "Bob"
      Then "DMV" and "Bob" have a connection

   #@T004-RFC0023 @normal @AcceptanceTest @Deprecated
   #Scenario: Establish a connection with DID Exchange between two agents with an explicit invitation with a public DID with role reversal

   @T005-RFC0023 @critical @AcceptanceTest
   Scenario: Establish a connection with DID Exchange between two agents with an implicit invitation
      Given we have "2" agents
         | name | role      |
         | DMV | requester |
         | Bob  | responder |
      And "Bob" has a resolvable DID
      And "DMV" acquires the resolvable DID
      When "DMV" sends the request to "Bob" with the public DID
      And "Bob" receives the request with their public DID
      When "Bob" sends a response to "DMV"
      And "DMV" receives the response
      And "DMV" sends complete to "Bob"
      Then "DMV" and "Bob" have a connection

   #@T006-RFC0023 @critical @AcceptanceTest @Deprecated
   #Scenario: Establish a connection with DID Exchange between two agents with an implicit invitation with role reversal

   # This test will give an expected failure when running with Aca-py with the --auto-accept-requests & --auto-respond-messages options.
   # Do not run this test with those flags on. It may also fail for other agents that do auto_responding depending on how the backchannel is implmented.
   @T007-RFC0023 @normal @AcceptanceTest @NegativeTest @ExceptionTest
   Scenario: Establish a connection with DID Exchange between two agents with attempt to continue after protocol is completed
      Given we have "2" agents
         | name | role      |
         | DMV | requester |
         | Bob  | responder |
      When "Bob" sends an explicit invitation to "DMV"
      And "DMV" receives the invitation
      And "DMV" sends the request to "Bob"
      And "Bob" receives the request
      And "Bob" sends a response to "DMV"
      And "DMV" receives the response
      And "DMV" sends complete to "Bob"
      And "Bob" sends a response to "DMV" which produces a problem_report
      Then "DMV" and "Bob" still have a completed connection

   @T008-RFC0023 @normal @AcceptanceTest @ExceptionTest @wip
   Scenario: Establish a connection with DID Exchange between two agents with an explicit invitation but invitation is rejected and connection process restarted
      Given we have "2" agents
         | name | role      |
         | DMV | requester |
         | Bob  | responder |
      When "Bob" sends an explicit invitation to "DMV"
      And "DMV" receives the invitation
      And "DMV" rejects the invitation
      And "DMV" restarts the connection process
      Then a successful connection can be established between "DMV" and "Bob"

   @T009-RFC0023 @normal @AcceptanceTest @ExceptionTest @wip
   Scenario: Establish a connection with DID Exchange between two agents with an explicit invitation but invitation is rejected and connection process abandoned
      Given we have "2" agents
         | name | role      |
         | DMV | requester |
         | Bob  | responder |
      When "Bob" sends an explicit invitation to "DMV"
      And "DMV" receives the invitation
      And "DMV" rejects the invitation
      And "DMV" abandons the connection process
      Then a connection can be established between "DMV" and "Bob" given that invitation

   @T010-RFC0023 @normal @AcceptanceTest @ExceptionTest @NegativeTest @wip
   Scenario Outline: Establish a connection with DID Exchange and responder rejects the request
      Given we have "2" agents
         | name | role      |
         | DMV | requester |
         | Bob  | responder |
      When "Bob" sends an explicit invitation to "DMV"
      And "DMV" receives the invitation
      And "DMV" sends the request to "Bob"
      And "Bob" receives the request
      And "Bob" rejects the request because of <reason>
      Then the connection is abandoned
      And "DMV" and "Bob" do not have a connection
      And establishing the connection cannot be continued

      Examples:
         | reason                                  |
         | Unsupported DID method for provided DID |
         | Expired Invitation                      |
         | DID Doc Invalid                         |
         | Unsupported key type                    |
         | Unsupported endpoint protocol           |
         | Missing reference to invitation         |
         | unknown processing error                |

   @T011-RFC0023 @normal @AcceptanceTest @ExceptionTest @NegativeTest @wip
   Scenario Outline: Establish a connection with DID Exchange and requester rejects the response
      Given we have "2" agents
         | name | role      |
         | DMV | requester |
         | Bob  | responder |
      When "Bob" sends an explicit invitation to "DMV"
      And "DMV" receives the invitation
      And "DMV" sends the request to "Bob"
      And "Bob" receives the request
      And "Bob" sends a response to "DMV"
      And "DMV" receives the response
      And "DMV" rejects the response because of <reason>
      Then the connection is abandoned
      And "DMV" and "Bob" do not have a connection
      And establishing the connection cannot be continued

      Examples:
         | reason                                  |
         | Unsupported DID method for provided DID |
         | Expired request                         |
         | DID Doc Invalid                         |
         | Unsupported key type                    |
         | Unsupported endpoint protocol           |
         | Invalid signature                       |
         | unknown processing error                |

   @T012-RFC0023 @normal @DerivedFunctionalTest @wip
   Scenario: Attempt to Establish a connection with DID Exchange between two agents with an explicit invitation with connection reuse
      Given we have "2" agents
         | name | role      |
         | DMV | requester |
         | Bob  | responder |
      And "DMV" and "Bob" have an existing connection with a public DID
      When "Bob" sends an explicit invitation wih a public DID
      And "DMV" receives the invitation while wanting to reuse an existing connection
      And "DMV" sends the request to "Bob"
      And "Bob" receives the request
      And "Bob" sends a response to "DMV"
      And "DMV" receives the response
      And "DMV" sends complete to "Bob"
      Then "DMV" and "Bob" have a connection