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
from webdriver_manager.firefox import GeckoDriverManager                           # Change here

# Packages for web control
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ---------------------------------------------------------------------------------------------------------------- #
## Options for Firefox Browser
options = webdriver.FirefoxOptions()
options.accept_insecure_certs = True
# options.add_argument('--started-maximized')
# options.add_argument('--ignore-certificate-errors')

# ---------------------------------------------------------------------------------------------------------------- #
## Create a new instance of Firefox WebDriver
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)     
driver.maximize_window()

driver.get('https://www.linkedin.com/checkpoint/lg/sign-in-another-account')        # Go to LinkedIn website
driver.find_element(By.ID, 'username').send_keys('Noah.wolfe3@gcu.edu')             # Type ID & Password
driver.find_element(By.ID, 'password').send_keys('Canyon1949!')
# ---------------------------------------------------------------------------------------------------------------- #
## Sign in button click
driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()      # Button Click
time.sleep(20)
driver.get('https://www.linkedin.com/sales/search/people')
WDW(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search keywords']"))) # Wait until page load

# ---------------------------------------------------------------------------------------------------------------- #
# Type the company name
#Read CSV file (Make sure it is right csv)
# fulldf = pd.read_csv('/home/lettuce/WorkCode/SalesNavigator/linkedin_from_excel/company_result/company_100_500.csv')

current_dir = os.getcwd()                                                           # Get the current directory
file_path = current_dir + "/company_result/company_100_500.csv"                     # File name
fulldf = pd.read_csv(file_path)
dfcompany = fulldf["Company"]

# ---------------------------------------------------------------------------------------------------------------- #
#First Itteration on Homepage
# temp_compamny = dfcompany[0]
# print(temp_compamny)
# # temp_compamny = "Liquid Foundation"
# driver.find_element(By.XPATH, "//input[@placeholder='Search keywords']").send_keys(temp_compamny)   # Search bar click and type 
# time.sleep(4)
# driver.find_element(By.XPATH, "//input[@placeholder='Search keywords']").send_keys(Keys.ENTER)
# time.sleep(4)
# text = driver.find_element(By.XPATH, "//body/main[@role='main']/div/div/div/div/ol/li[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]").text
# time.sleep(4)
# print(text)


# ---------------------------------------------------------------------------------------------------------------- #
# Change the li[index] for tracking
# //body/main[@role='main']/div/div/div/div/ol/li[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]

#Click the search bar and type company name
#Get each company name For loop
for x in range(len(dfcompany)):
    print(dfcompany[x])
    temp_compamny = dfcompany[x]
    driver.find_element(By.XPATH, "//input[@placeholder='Search keywords']").send_keys(temp_compamny)     # Search bar click and type 
    time.sleep(4)
    driver.find_element(By.XPATH, "//input[@placeholder='Search keywords']").send_keys(Keys.ENTER)        # Search bar click and type 
    time.sleep(4)
    text = driver.find_element(By.XPATH, "//body/main[@role='main']/div/div/div/div/ol/li[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]").text
    time.sleep(4)
    print(text)
    driver.back()
    time.sleep(4)

    # lines = text.splitlines()
    # seventh_line = lines[6]
    # print(seventh_line)
    # time.sleep(4)

    #Remove Text From Search
    #driver.find_element(By.XPATH, "//button[@id='   ']//li-icon[@type='cancel-icon']//*[name()='svg']").click()  #Click People button
    #time.sleep(4)   
    
        
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