from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page

class Header(Page):
    CART_BTN = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.CSS_SELECTOR, '#search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "a[data-test='@web/AccountLink']")

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def click_cart(self):
        self.click(*self.CART_BTN)

    def click_sign_in(self):
        self.click_sign_in = self.find_element(*self.SIGN_IN_BTN).click()
        # self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-test='@web/AccountLink']")))