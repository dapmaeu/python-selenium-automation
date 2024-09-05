
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

#Amazon logo
#locate by XPATH
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

#Email Field
#locate by ID
driver.find_element(By.ID, "//input[@id='ap_email']")

#Continue button
#locate by XPATH
driver.find_element(By.XPATH, "//input[@class='a-button-input']")

#Conditions of use link
#locate by XPATH
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

# Privacy Notice link
#locate by XPATH
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

# Need help link
#locate by XPATH
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Forgot your password link
#locate by ID
driver.find_element(By.ID, "//a[@id='auth-fpp-link-bottom']")

# Other issues with Sign-In link
#locate by ID
driver.find_element(By.ID, "//a[@id='ap-other-signin-issues-link']")

# Create your Amazon account button
#locate by ID
driver.find_element(By.ID, "//a[@id='createAccountSubmit']")

# 2. Create a test case for the SignIn page using python & selenium script.
# (Make sure to use Incognito browser mode when searching for locators)
#
# Test Case: Users can navigate to SignIn page
# 1. Open https://www.target.com/
# 2. Click SignIn button
# 3. Click SignIn from side navigation
# 4. Verify SignIn page opened:
# “Sign into your Target account” text is shown,
# SignIn button is shown (you can just use driver.find_element() to check for element’s presence, no need to assert here)
#
# [Optional] Build a test case yourself from scratch to search for a product on Target (same as shown in the class), make sure it works and you remember selenium commands.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()


# open the url
driver.get('https://www.target.com/')

driver.find_element(By.XPATH,"//span[@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()
sleep(3)
driver.find_element(By.XPATH,"//a[@data-test='accountNav-signIn' and @class='sc-676073c3-0 sc-859e7637-1 cALZIb kVBpoo']").click()
sleep(3)
actual_result = driver.find_element(By.XPATH,"//span[text()='Sign into your Target account']").text
expected_result = 'Sign into your Target account'

assert expected_result in actual_result
print('Test passed')

driver.quit()

# [Optional] Build a test case yourself from scratch to search for a product on Target (same as shown in the class), make sure it works and you remember selenium commands.

driver.get('https://www.target.com/')
sleep(5)

driver.find_element(By.ID, "search").send_keys('shirt')
sleep(5)

driver.find_element(By.XPATH,"//button[@class='sc-1c2974c-3 bsiIIZ']").click()
sleep(3)
actual_result = driver.find_element(By.XPATH,"//div[@data-test='resultsHeading']").text
expected_result = 'shirt'

assert expected_result in actual_result
print('Test passed')

driver.quit()
