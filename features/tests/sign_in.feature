Feature: Tests for Target Sign in Functionality


   Scenario: User can navigate to Sign In
    Given Open target main page
    When click Sign in
    When click on side menu sign in
    Then verify sign in form opened

  Scenario: User can enter username and password
    Given Open target main page
    When click Sign in
    When click on side menu sign in
    When input email address
    When input password
    When click sign in button
    #And sign in with a passkey later
    Then Verify user logged in

  #the target login page link is broken.
  # I had to add steps to access the login page from main
  Scenario: User can access Terms and conditions from sign in page
    Given Open target main page
    When click Sign in
    And click on side menu sign in
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window and switch back to original

  Scenario: User cant log in with invalid credentials
    Given Open target main page
    When click Sign in
    And click on side menu sign in
    When input incorrect email address
    When input incorrect password
    When click sign in button
    Then Verify that Please enter a valid password message is shown
#the “We can't find your account.” message never appeared when I was
  #trying to build the test case. so I built it with what i could use.


