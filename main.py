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
from selenium.webdriver.chrome.service import Service as ChromeService        # Download chrome automatically
from webdriver_manager.chrome import ChromeDriverManager


# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait as WDW
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# ---------------------------------------------------------------------------------------------------------------- #
## Options for Chrome Browser
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")                                     # Maximize the window tap
options.add_argument('--ignore-certificate-errors')

# ---------------------------------------------------------------------------------------------------------------- #
# Create a new instance of Chrome WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)        # Download automatically Chromedriver.
driver.get('https://www.linkedin.com/checkpoint/lg/sign-in-another-account')      # Go to LinkedIn website
driver.find_element(By.ID, 'username').send_keys('Noah.wolfe3@gcu.edu')           # Type ID & Password
driver.find_element(By.ID, 'password').send_keys('Canyon1949!')

# ---------------------------------------------------------------------------------------------------------------- #
# Sign in button click
driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()    # Button Click
driver.find_element(By.LINK_TEXT, 'Sales Nav').send_keys(Keys.RETURN)             # Navigate Sales Nav Tap
time.sleep(6)
# Close the browser window
# driver.quit()

# ---------------------------------------------------------------------------------------------------------------- #
# Type the company name
#Read CSV file (Make sure it is right csv)
fulldf = pd.read_csv('/home/lettuce/WorkCode/SalesNavigator/linkedin_from_excel/company_result/company_100_500.csv')
dfcompany = fulldf["Company"]

#First Itteration on Homepage
temp_compamny = dfcompany[0]
driver.find_element(By.ID, 'global-typeahead-search-input').send_keys(temp_compamny)   # Search bar click and type 
driver.find_element(By.XPATH, "//button[normalize-space()='Submit search']").click()  #Click Search button

#Click the search bar and type company name
#Get each company name For loop
for x in range(len(dfcompany)-1):
    print(dfcompany[x+1])
    temp_compamny = dfcompany[x+1]
    driver.find_element(By.ID, 'global-typeahead-search-input').send_keys(temp_compamny)   # Search bar click and type 
    driver.find_element(By.ID, 'global-typeahead-search-input').send_keys(Keys.ENTER) #Hit Enter instead of clicking search button
    


# ADD MORE (Look at prevoius CSV to find)
# title_list = ['CEO', 'Co-Founder', 'Business Owner', 'Director Contract Manufacturing', 'Owner', 'COO', 'Principal Engineer', 'Founder', 'Sales Supervisor', 'Sales Closer', 'Sales Representative', 'Director of Operations', 'Principal', 'President of Operations', 'Chief Executive Officer', 'CTO', 'Business Development Lead', 'Marketing Executive', 'CEO', 'Chief Executive Officer', 'C.E.O.', 'Founder', 'Co-founder', 'Cofounder', 'Director of Development', 'Business Development', 'Retail', 'ecommerce', 'Digital Marketing', 'CMO', 'Chief Marketing Officer', 'CTO', 'Chief Technology Officer', 'Director of Marketing', 'Software', 'Fundraising', 'Partner', 'Donor', 'President', 'Owner', 'Partnership', 'Marketing manager']