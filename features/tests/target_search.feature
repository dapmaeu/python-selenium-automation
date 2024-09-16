Feature: Tests for Target Search Functionality


  Scenario: User can search for a product
    Given Open target main page
    When Search for a product
    Then Verify that correct search results shown

  Scenario: User can search for bread
    Given Open target main page
    When search for bread
    Then verify that correct search results shows for bread

  Scenario Outline: User can search for products
    Given Open target main page
    When search for <product>
    Then Verify that correct search results shows for <search_result>
    Examples:
    |product| search_result|
    |bread  |bread         |
    |tea    |tea           |
    |coffee |coffee        |
