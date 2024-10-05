from importlib.metadata import pass_none
from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open sign in page')
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()
    sleep(10)


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.sign_in_page.get_current_window()
    print('Original window: ', context.original_window)


@when('Click on Target terms and conditions link')
def click_terms_and_cond_link(context):
    context.app.sign_in_page.click_terms_and_cond_link()
    sleep(5)


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.original_window = context.driver.current_window_handle
    context.app.sign_in_page.switch_to_new_window()
    print('After switching' , context.app.sign_in_page.get_current_window())


@when('input email address')
def input_email(context):
    context.app.sign_in_page.input_email_address()


@when('input incorrect email address')
def input_wrong_email(context):
    context.app.sign_in_page.input_wrong_email()


@when('input password')
def input_password(context):
    context.app.sign_in_page.input_password()


@when('input incorrect password')
def input_wrong_password(context):
    context.app.sign_in_page.input_wrong_password()


@when('click sign in button')
def click_sign_in_button(context):
    context.app.sign_in_page.click_sign_in_button()


# @when('sign in with a passkey later')
# def passkey_maybe_later(context):
#     context.app.sign_in_page.passkey_maybe_later()


@then('Verify user logged in')
def verify_user_logged_in(context):
    context.app.sign_in_page.verify_user_logged_in()


@then('verify sign in form opened')
def verify_sign_in(context):
    context.app.sign_in_page.verify_sign_in_page_open()


@then('Verify Terms and Conditions page is opened')
def verify_terms_and_cond_opened(context):
    context.app.sign_in_page.verify_terms_and_cond_opened()
    sleep(5)


@then('User can close new window and switch back to original')
def close_page_and_switch(context):
    context.app.sign_in_page.close()
    context.app.sign_in_page.switch_to_window_by_id(context.original_window)
    assert context.driver.current_window_handle == context.original_window, "Failed to switch back to the original window."


@then('Verify that Please enter a valid password message is shown')
def enter_a_valid_password(context):
    context.app.sign_in_page.enter_a_valid_password_message()


