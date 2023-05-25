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
from selenium.webdriver.firefox.service import Service as FirefoxService  # Change here
from webdriver_manager.firefox import GeckoDriverManager  # Change here


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
# from selenium.webdriver.firefox.service import Service  # Change here
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ---------------------------------------------------------------------------------------------------------------- #
## Options for Firefox Browser
options = webdriver.FirefoxOptions()
options.add_argument("--start-maximized")                                     # Maximize the window tap
options.add_argument('--ignore-certificate-errors')

# ---------------------------------------------------------------------------------------------------------------- #
# Create a new instance of Firefox WebDriver
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)        # Change here
driver.get('https://www.linkedin.com/checkpoint/lg/sign-in-another-account')      # Go to LinkedIn website
driver.find_element(By.ID, 'username').send_keys('Noah.wolfe3@gcu.edu')           # Type ID & Password
driver.find_element(By.ID, 'password').send_keys('Canyon1949!')
# ---------------------------------------------------------------------------------------------------------------- #
# Sign in button click
driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()   # Button Click
time.sleep(20)
WDW(driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Sales Nav')))  # Wait to find Sales Nav tab
driver.find_element(By.PARTIAL_LINK_TEXT, 'Sales Nav').send_keys(Keys.RETURN)           # Navigate Sales Nav Tabtime.sleep(100)
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
    time.sleep(2)
    element = driver.find_element_by_class_name('class="artdeco-entity-lockup__subtitle ember-view t-14"')
    #I dont know what element will be equal too till we test
    
    #COMPARE THE COMPANY NAME WITH THE ELEMENT
    #IF TRUE
        #ADD TO ARRAY
        #Move on to next person
    #IF FALSE
        #Move on to next person

    #IF NO PERSON FOUND
        #WRITE TO CSV FILE
    #IF PERSON FOUND BUT NOT FIT TITLE ADD IF LESS THAN 3
        #ADD TO LIST
    #IF PERSON FOUND GRATOR THEN 3 FILTER TITLE
        #ADD TO LIST

# ADD MORE (Look at prevoius CSV to find)
# title_list = ['CEO', 'Co-Founder', 'Business Owner', 'Director Contract Manufacturing', 'Owner', 'COO', 'Principal Engineer', 'Founder', 'Sales Supervisor', 'Sales Closer', 'Sales Representative', 'Director of Operations', 'Principal', 'President of Operations', 'Chief Executive Officer', 'CTO', 'Business Development Lead', 'Marketing Executive', 'CEO', 'Chief Executive Officer', 'C.E.O.', 'Founder', 'Co-founder', 'Cofounder', 'Director of Development', 'Business Development', 'Retail', 'ecommerce', 'Digital Marketing', 'CMO', 'Chief Marketing Officer', 'CTO', 'Chief Technology Officer', 'Director of Marketing', 'Software', 'Fundraising', 'Partner', 'Donor', 'President', 'Owner', 'Partnership', 'Marketing manager']