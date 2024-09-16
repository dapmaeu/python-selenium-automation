from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")

@then('Verify that cart is empty')
def verify_cart_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "div[data-test='boxEmptyMsg'] h1").text
    assert expected_text == actual_text, f'Expected {expected_text} did not match actual!= {actual_text}'


@when('open cart page')
def open_cart_page(context):
    context.driver.get('https://www.target.com/cart')
    sleep(10)


@then('verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"
