# ---------------------------------------------------------------------------------------------------------------- #
## Python default import packages.
# Colorama module: pip install colorama
# from colorama import init, Fore, Style  # Do not work on MacOS and Linux   ### Uncomment if you are using

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
driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()   # Button Click
time.sleep(20)
driver.get('https://www.linkedin.com/sales/search/people')
time.sleep(5) #Wait for page to load

# ---------------------------------------------------------------------------------------------------------------- #
# Type the company name
#Read CSV file (Make sure it is right csv)
fulldf = pd.read_csv('/home/lettuce/WorkCode/SalesNavigator/linkedin_from_excel/company_result/company_100_500.csv')
dfcompany = fulldf["Company"]

#First Itteration on Homepage
#temp_compamny = dfcompany[0]
#print(temp_compamny)
#temp_compamny = "Liquid Foundation"
#driver.find_element(By.XPATH, "//input[@id='global-typeahead-search-input']").send_keys(temp_compamny)   # Search bar click and type 
#driver.find_element(By.XPATH, "//span[contains(text(),'Search')]").click()  #Click Search button

#Click the search bar and type company name
#Get each company name For loop


for x in range(len(dfcompany)):
    print(dfcompany[x])
    temp_compamny = dfcompany[x]
    driver.find_element(By.XPATH, "//input[@placeholder='Search keywords']").send_keys(temp_compamny)   # Search bar click and type 
    time.sleep(4)
    driver.find_element(By.XPATH, "//input[@placeholder='Search keywords']").send_keys(Keys.ENTER)   # Search bar click and type 
    time.sleep(4)
    
    text = driver.find_element(By.XPATH, "//body/main[@role='main']/div[@class='flex']/div[@class='full-width']/div[@class='p4 _vertical-scroll-results_1igybl']/div[@class='relative']/ol[@class='artdeco-list background-color-white _border-search-results_1igybl']/li[2]").text
    print(text)
    time.sleep(4)
    #Remove Text From Search
    driver.find_element(By.XPATH, "//button[@id='   ']//li-icon[@type='cancel-icon']//*[name()='svg']").click()  #Click People button
    time.sleep(4)


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