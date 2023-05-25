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

driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()    # Button Click
driver.find_element(By.LINK_TEXT, 'Sales Nav').send_keys(Keys.RETURN)             # Navigate Sales Nav Tap

#driver.implicitly_wait(4)
time.sleep(6)
# Close the browser window
# driver.quit()


# ADD MORE (Look at prevoius CSV to find)
# title_list = ['CEO','Co-Founder','Business Owner','Director Contract Manufacturing','Owner','COO','Principal Engineer','Founder','Sales Supervisor','Sales Closer','Sales Representative','Director of Operations','Principal','President of Operations','Chief Executive Officer','CTO','Business Development Lead','Marketing Executive']