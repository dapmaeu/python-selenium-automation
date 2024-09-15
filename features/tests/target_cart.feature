# Created by marud at 9/14/2024
Feature: Tests for Target cart Functionality

  Scenario: User can verifies that cart is empty
    Given Open target main page
    When click on cart icon
    Then Verify that cart is empty

  Scenario: User can navigate to Sign In
    Given Open target main page
    When click Sign in
    When click on side menu sign in
    Then verify sign in form opened