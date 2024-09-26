from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class CartPage(Page):
    CART_EMPTY_TXT = (By.CSS_SELECTOR, "div[data-test='boxEmptyMsg'] h1")
    CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def verify_cart_empty(self):
        expected_text = 'Your cart is empty'
        actual_text = self.find_element(*self.CART_EMPTY_TXT).text
        assert expected_text == actual_text, f'Expected {expected_text} did not match actual!= {actual_text}'

    def open_cart_main(self):
        self.open('https://www.target.com/cart')
        sleep(10)

    def verify_cart_items(self, amount=None):
        cart_summary = self.find_element(*self.CART_SUMMARY).text
        assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"
        sleep(5)

