from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from sample_script import driver


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')
    sleep(2)


@when('click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/CartLink']").click()


@then('Verify that cart is empty')
def verify_cart_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "div[data-test='boxEmptyMsg'] h1").text
    assert expected_text == actual_text, f'Expected {expected_text} did not match actual!= {actual_text}'


@when('click Sign in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/AccountLink']").click()
    sleep(2)


@when('click on side menu sign in')
def side_menu_click(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']").click()

@then('verify sign in form opened')
def verify_sign_in(context):
    expected_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1[class='sc-fe064f5c-0 sc-315b8ab9-2 WObnm gClYfs'] span").text
    assert expected_text == actual_text, f'Expected {expected_text} did not match actual!= {actual_text}'


