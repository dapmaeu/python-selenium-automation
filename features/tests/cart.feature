Feature: Tests for Target Cart Functionality


   Scenario: User can verifies that cart is empty
    Given Open target main page
    When click on cart icon
    Then Verify that cart is empty


  Scenario: User can add product to cart
    Given Open target main page
    When search for pants
    And click Add to Cart button
    And confirm Add to Cart button from side navigation screen
    And open cart page
    Then verify cart has 1 item(s)
