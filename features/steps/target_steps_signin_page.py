from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('verify sign in form opened')
def verify_sign_in(context):
    context.app.sign_in_page.verify_sign_in_page_open()


@when('input email address')
def input_email(context):
    context.app.sign_in_page.input_email_address()

@when('input password')
def input_password(context):
    context.app.sign_in_page.input_password()

@when('click sign in button')
def click_sign_in_button(context):
    context.app.sign_in_page.click_sign_in_button()


