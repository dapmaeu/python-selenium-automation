from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    SIDE_MENU_SIGN_IN = (By.CSS_SELECTOR, "a[data-test='accountNav-signIn']")

    def open_main(self):
        self.open('https://www.target.com/')

    def side_menu_sign_in(self):
        self.click = self.find_element(*self.SIDE_MENU_SIGN_IN).click()

