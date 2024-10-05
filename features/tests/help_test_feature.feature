Feature: Tests for Help pages

  Scenario: User can select Help topic promotions and coupons
    Given Open help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify help Current promotions page opened


  Scenario: User can select Help About Target Circle
    Given Open help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Target Circle™
    Then Verify help About Target Circle page opened


  Scenario: User can select Help Target Account
    Given Open help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Target Account
    Then Verify help Create account page opened