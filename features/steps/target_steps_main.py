from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/CartLink']").click()


@when('search for {item}')
def search_product(context, item):
    print(item)
    context.driver.find_element(By.CSS_SELECTOR, '#search').send_keys(item)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(10)


# @when('Search for a product')
# def search_product(context):
#     context.driver.find_element(By.ID, 'search').send_keys('tea')
#     context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
#     sleep(5)


@when('click Sign in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/AccountLink']").click()
    sleep(2)


@when('click on side menu sign in')
def side_menu_click(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']").click()


@when('click on target circle button')
def click_target_circle(context):
    context.driver.find_element(By.CSS_SELECTOR, '#utilityNav-circle')
    sleep(2)


