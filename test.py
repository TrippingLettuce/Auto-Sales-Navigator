# ---------------------------------------------------------------------------------------------------------------- #
## Python default import packages.
# Colorama module: pip install colorama
# from colorama import init, Fore, Style  # Do not work on MacOS and Linux        ### Uncomment if you are using

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
from selenium.webdriver.chrome.service import Service as ChromeService            # Download chrome automatically
from webdriver_manager.chrome import ChromeDriverManager

# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Packages for Wait method
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

# ---------------------------------------------------------------------------------------------------------------- #
## Options for Chrome Browser
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")                                         # Maximize the window tap
options.add_argument('--ignore-certificate-errors')

# ---------------------------------------------------------------------------------------------------------------- #
# Create a new instance of Chrome WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)        # Download automatically Chromedriver.

driver.get('https://www.linkedin.com/checkpoint/lg/sign-in-another-account')      # Go to LinkedIn website
driver.find_element(By.ID, 'username').send_keys('goldthelim@gmail.com')          # Type ID & Password
driver.find_element(By.ID, 'password').send_keys('!Iw6751qe!')

driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()    # Button Click
# driver.find_element(By.PARTIAL_LINK_TEXT, 'Sales Nav').send_keys(Keys.RETURN)   # Navigate Sales Nav Tap

find_web = driver.find_element(By.TAG_NAME, "input")
find_web.send_keys("rejuvia", Keys.RETURN)

WDW(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="People"]')))     # Wait until found the clickable button
driver.find_element(By.XPATH, '//button[text()="People"]').click()                # Find People Button
time.sleep(5)


#driver.implicitly_wait(4)

# Close the browser window
# driver.quit()


# ADD MORE (Look at prevoius CSV to find)
# title_list = ['CEO','Co-Founder','Business Owner','Director Contract Manufacturing','Owner','COO','Principal Engineer','Founder','Sales Supervisor','Sales Closer','Sales Representative','Director of Operations','Principal','President of Operations','Chief Executive Officer','CTO','Business Development Lead','Marketing Executive']