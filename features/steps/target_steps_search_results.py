from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, "img")


@when('click Add to Cart button')
def click_add_to_cart(context):
    context.app.search_results_page.click_add_to_cart()


@when('Store product name')
def store_product_name(context):
    context.app.search_results_page.store_product_name()


@when('confirm Add to Cart button from side navigation screen')
def side_nav_click_add_to_cart(context):
    context.app.search_results_page.click_add_to_cart_side_nav()


@then('Verify that correct search results shows for {product}')
def verify_results(context, product):
    context.app.search_results_page.verify_results(product)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
    PRODUCT_IMG = (By.CSS_SELECTOR, 'img')
    sleep(5)
    context.driver.execute_script("window.scrollBy(0,1000)", "")
    sleep(5)
    context.driver.execute_script("window.scrollBy(0,1000)", "")
    sleep(5)
    context.driver.execute_script("window.scrollBy(0,1000)", "")
    sleep(5)
    context.driver.execute_script("window.scrollBy(0,1000)", "")
    sleep(5)
    context.driver.execute_script("window.scrollBy(0,1000)", "")
    sleep(5)
    context.driver.execute_script("window.scrollBy(0,1000)", "")
    sleep(5)
    context.driver.execute_script("window.scrollBy(0,1000)", "")
    sleep(5)
    context.driver.execute_script("window.scrollBy(0,1000)", "")
    sleep(5)

    all_products = context.driver.find_elements(*LISTINGS)

    for product in all_products:
        context.driver.wait.until(EC.visibility_of_element_located(PRODUCT_TITLE))
        title = product.find_element(*PRODUCT_TITLE)
        assert title, 'Product title not found'

