from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


    def verify_results(self, product):
        actual_result = self.find_element(*self.SEARCH_RESULTS_HEADER).text
        assert product in actual_result, f'Expected {product}, got actual {actual_result}'

    def click_add_to_cart(self):
        self.find_element(*self.ADD_TO_CART_BTN).click()
        sleep(5)

    def store_product_name(self):
        self.product_name = self.find_element(*self.SIDE_NAV_PRODUCT_NAME).text
        print(f'Product name: {self.product_name}')

    def click_add_to_cart_side_nav(self):
        self.click(*self.ADD_TO_CART_BTN_SIDE_NAV)
        sleep(5)

    def verify_cart_product_name(self):
        actual_name = self.find_element(*self.CART_ITEM_TITLE).text
        assert self.product_name in actual_name, f'Expected {self.product_name} but got {actual_name}'




