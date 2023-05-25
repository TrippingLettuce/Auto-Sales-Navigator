# ---------------------------------------------------------------------------------------------------------------- #
## Python default import packages.
from datetime import datetime as dt
from glob import glob
import sys
import os
# ---------------------------------------------------------------------------------------------------------------- #
## Applicable packages for automation
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager          # Download chrome automatically

from selenium.webdriver.common.by import By                         # By class are used to locate elements on a page
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# ---------------------------------------------------------------------------------------------------------------- #
## Path to Chrome WebDriver executable
# s = Service('/usr/local/bin/chromedriver')
webdriver_path = '/usr/local/bin/chromedriver'                      ### Change the Path depends on the device

# ---------------------------------------------------------------------------------------------------------------- #
## Options for Chrome Browser
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")                           # Maximize the window tap


# ---------------------------------------------------------------------------------------------------------------- #
# Create a new instance of Chrome WebDriver
# driver = webdriver.Chrome(ChromeDriverManager().install())        # Download automatically Chromedriver.
driver = webdriver.Chrome(webdriver_path, options=options)

driver.get('https://www.linkedin.com/checkpoint/lg/sign-in-another-account')      # Go to LinkedIn website
driver.find_element(By.ID, 'username').send_keys('Noah.wolfe3@gcu.edu')           # Type ID & Password
driver.find_element(By.ID, 'password').send_keys('Canyon1949!')

driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()    # Button Click

# Close the browser window
# driver.quit()


# ADD MORE (Look at prevoius CSV to find)
title_list = ['CEO','Co-Founder','Business Owner','Director Contract Manufacturing','Owner','COO','Principal Engineer','Founder','Sales Supervisor','Sales Closer','Sales Representative','Director of Operations','Principal','President of Operations','Chief Executive Officer','CTO','Business Development Lead','Marketing Executive']




