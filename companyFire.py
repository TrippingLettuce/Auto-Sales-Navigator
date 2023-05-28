# ---------------------------------------------------------------------------------------------------------------- #
## Python default import packages.
from datetime import datetime as dt
import sys
import os
import time
import pandas as pd
import numpy as np
from selenium import webdriver

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

# Find the search box element by its name attribute
search_box = wait.until(EC.presence_of_element_located((By.NAME, 'q')))    # Google's search box name is 'q'
search_box.send_keys("Test Hello", Keys.ENTER) 

# Wait for some time for the page to load
time.sleep(5)

# Now add a scroll to bottom feature
#last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     # Scroll down to the bottom of the page
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     # Wait for new page segment to load
#     time.sleep(2)

#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height

element = driver.find_element_by_xpath('/html[1]/body[1]/div[7]/div[1]/div[13]/div[1]/div[2]/div[2]/div[1]/div[1]/div[10]/div[1]/div[1]/div[1]/div[1]/div[1]')
driver.execute_script("arguments[0].scrollIntoView();", element)