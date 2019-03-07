Feature: Update the customer name
  As a client
  I want to update my customer name because my name has changed

  Scenario: Customer name has changed
    Given customer "Nicole Forsgren" with ID "12345" exists
    When The customer with id "12345" updates their name to "Nicholas Forsgren"
    And I fetch customer "12345"
    Then I should see customer "Nicholas Forsgren"


