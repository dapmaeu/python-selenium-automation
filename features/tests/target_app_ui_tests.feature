# Created by marud at 9/27/2024
Feature: Tests for Target App page
  # Enter feature description here

  Scenario: User is able to open Privacy Policy
    Given Open Target App page
    And Store original window
    When Click Privacy Policy link
    And Switch to new window
    Then Verify Privacy Policy page opened
    And close current page
    And Return to original window
