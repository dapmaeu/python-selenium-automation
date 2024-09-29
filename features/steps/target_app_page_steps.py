from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

@given('Open Target App page')
def open_target_app(context):
    context.app.target_app_page.open_target_app()
    # sleep(6)


@given('Store original window')
def store_window(context):
    context.original_window = context.app.target_app_page.get_current_window()
    print('Original window: ', context.original_window)


@when('Click Privacy Policy link')
def click_pp_link(context):
    context.app.target_app_page.click_pp_link()
    # sleep(6)


@when('Switch to new window')
def switch_to_new_window(context):
    context.app.target_app_page.switch_to_new_window()
    print('After switched', context.app.target_app_page.get_current_window())


@then('Verify Privacy Policy page opened')
def verify_pp_opened(context):
    context.app.target_app_page.verify_pp_opened()
    # sleep(5)


@then('close current page')
def close_page(context):
    context.app.target_app_page.close()
    # sleep(3)

@then('Return to original window')
def switch_to_original(context):
    context.app.target_app_page.switch_to_window_by_id(context.original_window)
    # sleep(1)