from lib2to3.fixes.fix_input import context
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('verify that target circle has {amount} links in the target circle page')
def verify_circle_benefits_links(context,amount):
    expected_amount = int(amount)
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='@web/slingshot-components/CellsComponent/Link']")
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'

