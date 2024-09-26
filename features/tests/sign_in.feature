Feature: Tests for Target Sign in Functionality


   Scenario: User can navigate to Sign In
    Given Open target main page
    When click Sign in
    When click on side menu sign in
    Then verify sign in form opened

  Scenario:
    Given Open target main page
    When click Sign in
    When click on side menu sign in
    When input email address
    When input password
    When click sign in button
    #Then Verify user is logged in