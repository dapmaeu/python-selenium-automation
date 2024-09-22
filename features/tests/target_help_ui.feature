Feature: Target Help present elements

  Scenario: Verify UI elements are present
    Given Open target help page
    When Verify Target Help sign is present
    And Verify search bar is present
    And Verify search button is present
    And Verify what would you like to do is present
    And Verify that contact and product recall are present
    Then Verify Browse all help pages sign is present
