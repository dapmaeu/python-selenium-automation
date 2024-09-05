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
