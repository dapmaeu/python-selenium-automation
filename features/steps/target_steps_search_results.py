from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from sample_script import driver


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")

@then('Verify that correct search results shown')
def verify_results(context):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    expected_result = 'tea'
    assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'


@then('Verify that correct search results shows for {product}')
def verify_results(context, product):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product in actual_result, f'Expected {product}, got actual {actual_result}'


@when('click Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()

@when('confirm Add to Cart button from side navigation screen')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN_SIDE_NAV).click()
    sleep(5)

