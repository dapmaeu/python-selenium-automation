from selenium import webdriver
from selenium.webdriver.common.by import By, ByType
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://https://www.amazon.com')


#Homework part 1
#Amazon logo
driver.find_element(By.CSS_SELECTOR, '.a-link-nav-icon')
#Create Account Message
driver.find_element(By.CSS_SELECTOR, "[class='a-spacing-small']")
#Your Name
driver.find_element(By.CSS_SELECTOR, 'ap_customer_name')
#Mobile Number and Email
driver.find_element(By.CSS_SELECTOR, '#ap_email')
#Password
driver.find_element(By.CSS_SELECTOR, '#ap_password')
#Reenter Password
driver.find_element(By.CSS_SELECTOR, 'ap_password_check')
#Create Account button (in my page was called continue)
driver.find_element(By.CSS_SELECTOR, '#continue')
#conditions of use
driver.find_element(By.CSS_SELECTOR, "[href*='ap_register_notification_condition_of_use']")
#privacy notice
driver.find_element(By.CSS_SELECTOR, "[href*='ap_register_notification_privacy_notice']")
#sign in
driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis')




