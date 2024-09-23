Feature: Tests for Target Search Functionality


  Scenario: User can search for a coffee
    Given Open target main page
    When Search for coffee
    Then Verify that correct search results shows for coffee

  Scenario: User can search for tea
    Given Open target main page
    When search for tea
    Then verify that correct search results shows for tea

  Scenario Outline: User can search for products
    Given Open target main page
    When search for <product>
    Then Verify that correct search results shows for <search_result>
    Examples:
    |product| search_result|
    |bread  |bread         |
    |tea    |tea           |
    |coffee |coffee        |


  Scenario: Target search has product name and product image
    Given Open target main page
    When search for tea
    Then Verify that every product has a name and an image



