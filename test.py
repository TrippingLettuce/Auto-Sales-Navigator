# ---------------------------------------------------------------------------------------------------------------- #
## Python default import packages.
# Colorama module: pip install colorama
# from colorama import init, Fore, Style  # Do not work on MacOS and Linux   ### Uncomment if you are using it.

# Python default import.
from datetime import datetime as dt
from glob import glob
import sys
import os
import time
import pandas as pd
import numpy as np
# ---------------------------------------------------------------------------------------------------------------- #
## Applicable packages for automation
# Selenium module imports: pip install selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService           # Change here
from webdriver_manager.firefox import GeckoDriverManager       
from selenium.webdriver.common.action_chains import ActionChains
# Change here

# Packages for web control
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException
# ---------------------------------------------------------------------------------------------------------------- #
## Options for Firefox Browser
options = webdriver.FirefoxOptions()
options.accept_insecure_certs = True

# ---------------------------------------------------------------------------------------------------------------- #
## Create a new instance of Firefox WebDriver
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)     
driver.maximize_window()
wait = WDW(driver, 10)                                                              # Define Wait

driver.get('https://www.linkedin.com/checkpoint/lg/sign-in-another-account')        # Go to LinkedIn website
driver.find_element(By.ID, 'username').send_keys('Noah.wolfe3@gcu.edu')             # Type ID & Password
driver.find_element(By.ID, 'password').send_keys('Canyon1949!')
# ---------------------------------------------------------------------------------------------------------------- #
## Sign in button click
driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()      # Button Click
time.sleep(15)
driver.get('https://www.linkedin.com/sales/search/people')
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search keywords']"))) # Wait until page load

# ---------------------------------------------------------------------------------------------------------------- #
## Type the company name
# Read CSV file (Make sure it is right csv)
current_dir = os.getcwd()                                                           # Get the current directory
file_path = current_dir + "/company_result/company_100_500.csv"                     # File name
# file_path = "/home/lettuce/WorkCode/SalesNavigator/linkedin_from_excel/company_result/company_100_500.csv"
fulldf = pd.read_csv(file_path)
dfcompany = fulldf["Company"]

temp_company = dfcompany[0]

wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search keywords']"))).send_keys(temp_company, Keys.ENTER)
wait.until(EC.element_to_be_clickable((By.XPATH, f"/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/ol[1]/li[{1}]/div[1]/div[1]/div[1]/label[1]"))).click() 

save_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Save all selected leads to a custom list.']")))
save_button.click()

# Find the parent element that contains the list of <li> elements
parent_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div[1]/div[2]/div[1]/div[2]/div/div[3]/div/div/ul')))
parent_element.find_element(By.XPATH, '/html/body/main/div[1]/div[2]/div[1]/div[2]/div/div[3]/div/div/ul')


# element = driver.find_element("xpath", f'/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/ol[1]/li[{m}]/div[1]/div[1]/div[1]/label[1]')
# driver.execute_script("arguments[0].scrollIntoView();", element)
# driver.execute_script("arguments[0].click();", element)
# print(f"Clicked {m}")


# Scroll down the page to ensure all elements are loaded
# You can adjust the number of scroll iterations and sleep time as needed
# for _ in range(10):
#     parent_element.send_keys(Keys.PAGE_DOWN)
#     time.sleep(0.5)

child_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div[1]/div[2]/div[1]/div[2]/div/div[3]/div/div/ul/li[2]/ul')))
child_element.find_element(By.XPATH, '/html/body/main/div[1]/div[2]/div[1]/div[2]/div/div[3]/div/div/ul/li[2]/ul')

child_li = child_element.find_elements(By.TAG_NAME, 'li')

li_count = len(child_li)

print(li_count)
for i in range(1, li_count + 1):
    text = child_element.find_element(By.XPATH, f'/html/body/main/div[1]/div[2]/div[1]/div[2]/div/div[3]/div/div/ul/li[2]/ul/li[{i}]/div/div/div[1]').text
    if text == 'Test leads 2.0':
        driver.find_element(By.XPATH, f'/html/body/main/div[1]/div[2]/div[1]/div[2]/div/div[3]/div/div/ul/li[2]/ul/li[{i}]').click()
        break

