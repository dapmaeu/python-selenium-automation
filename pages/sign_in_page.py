from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_FORM = (By.CSS_SELECTOR, "h1[class='sc-fe064f5c-0 sc-315b8ab9-2 WObnm gClYfs'] span")
    EMAIL_FIELD = (By.CSS_SELECTOR, "[id='username']")
    EMAIL = ""
    WRONG_EMAIL = "wrongemail@nomail.com"
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    PASSWORD = ""
    WRONG_PASSWORD = "totaly the wrong password"
    SIGN_IN_BTN = (By.CSS_SELECTOR, "#login")
    TERMS_AND_COND_LINK = (By.XPATH, "//a[@aria-label='terms & conditions - opens in a new window']")
    SIGN_IN_GREET = (By.XPATH, "//span[text()= 'Hi, Maria ']")
    ENTER_A_VALID_PASSWORD = (By.CSS_SELECTOR, "#password--ErrorMessage")
    # MAYBE_LATER_BTN = (By.XPATH, "//button[text()='Maybe later']")


#the target login page link is broken. so I had to add steps to access the login page from main
    # def open_sign_in_page(self):
    #     self.open('https://www.target.com/login')


    def click_terms_and_cond_link(self):
        self.wait_to_be_clickable_click(*self.TERMS_AND_COND_LINK)


    def verify_terms_and_cond_opened(self):
        self.verify_partial_url('terms-conditions/')


    def verify_sign_in_page_open(self):
        expected_text = 'Sign into your Target account'
        actual_text = self.find_element(*self.SIGN_IN_FORM).text
        assert expected_text == actual_text, f'Expected {expected_text} did not match actual!= {actual_text}'


    def input_email_address(self):
        self.input_text(self.EMAIL,*self.EMAIL_FIELD)

    def input_wrong_email(self):
        self.input_text(self.WRONG_EMAIL,*self.EMAIL_FIELD)


    def input_password(self):
        self.input_text(self.PASSWORD,*self.PASSWORD_FIELD)


    def input_wrong_password(self):
        self.input_text(self.WRONG_PASSWORD,*self.PASSWORD_FIELD)


    def click_sign_in_button(self):
        self.click(*self.SIGN_IN_BTN)
        sleep(10)

    # def passkey_maybe_later(self):
    #     self.click(*self.MAYBE_LATER_BTN)

    def verify_user_logged_in(self):
        expected_text = 'Hi, Maria'
        actual_text = self.find_element(*self.SIGN_IN_GREET)
        assert expected_text == actual_text, f'Expected {expected_text} did not match actual!= {actual_text}'
        sleep(5)


    def enter_a_valid_password_message(self):
        self.wait_for_element_to_appear(*self.ENTER_A_VALID_PASSWORD)
        sleep(5)