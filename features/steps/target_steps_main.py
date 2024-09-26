from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#wait = WebDriverWait(context, 10)


@given('Open target main page')
def open_main(context):
    context.app.main_page.open_main()


@when('click on cart icon')
def click_cart(context):
    context.app.header.click_cart()


@when('search for {item}')
def search_product(context, item):
    context.app.header.search_product(item)
    sleep(5)


@when('click Sign in')
def click_sign_in(context):
    context.app.header.click_sign_in()


@when('click on side menu sign in')
def side_menu_click(context):
    context.app.main_page.side_menu_sign_in()
    sleep(5)


@when('click on target circle button')
def click_target_circle(context):
    context.driver.find_element(By.CSS_SELECTOR, '#utilityNav-circle').click()
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#utilityNav-circle')))
    #sleep(2)


