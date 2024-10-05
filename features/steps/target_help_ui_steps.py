from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#wait = WebDriverWait(context, 10)


@given('Open target help page')
def open_target_help(context):
    context.driver.get('https://help.target.com/help')


@when('Verify Target Help sign is present')
def target_help_sign_present(context):
    context.driver.find_element(By.XPATH, "//*[contains(text(), 'Target Help')]")


@when('Verify search bar is present')
def target_search_bar(context):
    context.driver.find_element(By.CSS_SELECTOR, ".search-input")


@when('Verify search button is present')
def search_button(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn-sm")


@when('Verify what would you like to do is present')
def user_options(context):
    context.driver.find_element(By.CSS_SELECTOR,"[class='grid_6']")


@when('Verify that contact and product recall are present')
def contact_and_prod_recall(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class='grid_4 boxSmallr txtAC bigbox2']")


@then('Verify Browse all help pages sign is present')
def browse_all_help(context):
    context.driver.find_element(By.CSS_SELECTOR,"[class='home-container'] h2")

