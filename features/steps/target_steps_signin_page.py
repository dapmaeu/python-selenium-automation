from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('verify sign in form opened')
def verify_sign_in(context):
    expected_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1[class='sc-fe064f5c-0 sc-315b8ab9-2 WObnm gClYfs'] span").text
    assert expected_text == actual_text, f'Expected {expected_text} did not match actual!= {actual_text}'