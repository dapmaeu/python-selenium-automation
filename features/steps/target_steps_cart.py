from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
CART_ITEM_TITLE =  (By.CSS_SELECTOR, "[data-test='cartItem-title']")

@then('Verify that cart is empty')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()


@when('open cart page')
def open_cart_main(context):
    context.app.cart_page.open_cart_main()


@then('verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    context.app.cart_page.verify_cart_items(amount)


@then('Verify cart has correct product')
def verify_product_name(context):
    context.app.search_results_page.verify_cart_product_name()
    sleep(10)