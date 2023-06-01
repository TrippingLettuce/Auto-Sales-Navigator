# ---------------------------------------------------------------------------------------------------------------- #
## Python default import packages.
from datetime import datetime as dt
import sys
import os
import time
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException
# ---------------------------------------------------------------------------------------------------------------- #
## Applicable packages for automation
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService  
from webdriver_manager.firefox import GeckoDriverManager  

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ---------------------------------------------------------------------------------------------------------------- #
## Options for Firefox Browser
options = webdriver.FirefoxOptions()
options.accept_insecure_certs = True

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
driver.maximize_window()
wait = WDW(driver, 10)    

# Go to Google
driver.get('https://www.google.com')

#Get CSV
df = pd.read_csv('/home/lettuce/WorkCode/SalesNavigator/linkedin_from_excel/company_result/company_100_500.csv')
dfcompany = df["Company"]

for x in range(len(dfcompany)):
    temp_compamny = dfcompany[x]

    # Find the search box element by its name attribute
    search_box = wait.until(EC.presence_of_element_located((By.NAME, 'q')))    # Google's search box name is 'q'
    search_box.send_keys(temp_compamny, Keys.ENTER) 

    wait.until(EC.element_to_be_clickable((By.ID, "res")))
    try:
        company_obj = wait.until(EC.presence_of_element_located((By.XPATH, "//p[@role='heading']//a[1]"))).text
        df.loc[x, 'Company'] = company_obj  # Update 'Company' field in your dataframe
    except (ElementNotInteractableException, NoSuchElementException, TimeoutException) as e:
        print(f"No autocorrect element for {temp_compamny} or another issue occurred. Error: {e}")
        driver.back() 
        continue
    
    driver.back()  # Go to the back of the page

# Save dataframe to a new csv
df.to_csv('/home/lettuce/WorkCode/SalesNavigator/linkedin_from_excel/company_result/filter2.csv', index=False)

