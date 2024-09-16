from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target help page')
def open_target_help(context):
    context.driver.get('https://help.target.com/help')
    sleep(3)


@when('Verify Target Help sign is present')
def target_help_sign_present(context):
    context.driver.find_element(By.XPATH, "//*[contains(text(), 'Target Help')]")
    sleep(3)


@when('Verify search bar is present')
def target_search_bar(context):
    context.driver.find_element(By.CSS_SELECTOR, ".search-input")


@when('Verify search button is present')
def search_button(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn-sm")


@when('Verify what would you like to do is present')
def user_options(context):
    context.driver.find_element