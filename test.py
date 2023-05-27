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


# ---------------------------------------------------------------------------------------------------------------- #
## Change the li[index] for tracking
# //body/main[@role='main']/div/div/div/div/ol/li[Change This Index]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]

# Click the search bar and type company name
# Get each company name For loop
for x in range(len(dfcompany)):
    print(dfcompany[x])                 # print- company name
    temp_compamny = dfcompany[x]
    #Define the list for company name
    companys_list = []
    position_list = []
    

    try:
        # Wait until the presence of Search Bar element. 
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search keywords']"))).send_keys(temp_compamny, Keys.ENTER)      # Search bar click and type  
        # Wait until the profile element is presence
        text_obj = wait.until(EC.presence_of_element_located((By.XPATH, "//body/main[@role='main']/div/div/div/div/ol/li[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]")))
    
        # Scroll
            #Click Page
            
        driver.find_element(By.XPATH, "//div[@id='search-results-container']").click()
            #Get Driver
        actions = ActionChains(driver)
            #Scroll Through Page
        for _ in range(10):  # scroll ammount
            actions.send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(.3) # scroll time
        
        # Loop Through People (24 per page: Maximum element in the page)
        # for y in range(1, 24):
        # Find the count of <li> elements
        li_count = len(driver.find_elements(By.XPATH, "//ol/li"))
        print(li_count)                 # print- li count
        # Define the maximum number of iterations
        max_iterations = min(li_count, 24)

        for y in range(1, max_iterations + 1):
            try:
                # Define XPATH for company element and position element
                company_obj_xpath = f"//body/main[@role='main']/div/div/div/div/ol/li[{y}]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]"
                position_xpath = f"//body/main[@role='main']/div/div/div/div/ol/li[{y}]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/span[1]"

                # Grab a text file from company object
                company_obj = wait.until(EC.presence_of_element_located((By.XPATH, company_obj_xpath))).text
                position = wait.until(EC.presence_of_element_located((By.XPATH, position_xpath))).text
                company = company_obj.replace(position+" ", "")

            # ------ After  : Do comparison action here ------ #
                print("Position: " + position, "|", "Company: " + company)                                 # print- position & company
                #print(temp_compamny + "----" + company)
                if company.replace(" ", "").lower() == temp_compamny.replace(" ","").lower(): # added strip method to erase the blank
                    companys_list.append(y)
                    position_list.append(position)
                    print("\n" + str(companys_list) + "\n")

                    # Mark in List
            # ------ Before : Do comparison action here ------ #
            except NoSuchElementException:
                break
                # Check Title and Company List
        # title_list = ['Chairman of the Board','President & CEO', 'CEO', 'Co-Founder', 'Business Owner', 'Director Contract Manufacturing', 'Owner', 'COO', 'Principal Engineer', 'Founder', 'Sales Supervisor', 'Sales Closer', 'Sales Representative', 'Director of Operations', 'Principal', 'President of Operations', 'Chief Executive Officer', 'CTO', 'Business Development Lead', 'Marketing Executive', 'CEO', 'Chief Executive Officer', 'C.E.O.', 'Founder', 'Co founder', 'Cofounder', 'Director of Development', 'Business Development', 'Retail', 'ecommerce', 'Digital Marketing', 'CMO', 'Chief Marketing Officer', 'CTO', 'Chief Technology Officer', 'Director of Marketing', 'Software', 'Fundraising', 'Partner', 'Donor', 'President', 'Owner', 'Partnership', 'Marketing manager']
        keyword = ['ceo','president','lead','owner','engineer','senior','chief','partner','director','head',
                'development','officer','retail','fundraising','cto','cmo','founder','coo','chairman','honor','manager']

        if len(companys_list) == 0:
            print("No Companies")

        elif len(companys_list) < 3:
            print("\n" + str(companys_list) + "\n")
            for m in companys_list:
                wait.until(EC.element_to_be_clickable((By.XPATH, f"/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/ol[1]/li[{m}]/div[1]/div[1]/div[1]/label[1]"))).click() 

        elif len(companys_list) >= 3:
            indices_to_pop = []
            for x in range(len(position_list)):
                if not any(keyword in position_list[x].lower() for keyword in keyword):
                    indices_to_pop.append(x)
            
            for index in reversed(indices_to_pop):
                companys_list.pop(index)
                position_list.pop(index)
            
            print("\n" + str(companys_list) + "\n")

            for m in companys_list:
                try:
                    wait.until(EC.element_to_be_clickable((By.XPATH, f"/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/ol[1]/li[{m}]/div[1]/div[1]/div[1]/label[1]"))).click() 
                # except NoSuchElementException:
                #     continue
                except ElementNotInteractableException:
                    pass
                
            time.sleep(2)

        # time.sleep(4) # to see the check mark is right on
        driver.back()                               # Go to the back of the page
        
    except TimeoutException:
        driver.back()                               # Go to the back of the page
    



#Get pos


# ADD MORE (Look at prevoius CSV to find)

# ---------------------------------------------------------------------------------------------------------------- #
## Task Required
# 1) Auto Navigation for Sales Nav tab [x]
# 2) Scroll through the page and grab profile [x]
# 3) Compare correct company with required position [ ]
#   - May require to find out right company name
# 4) Press check mark for people who will save [ ]
# 5) Save people correspond to right folder [ ]
# ---------------------------------------------------------------------------------------------------------------- #