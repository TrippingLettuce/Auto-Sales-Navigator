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

## Create a new instance of Firefox WebDriver
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)     
driver.maximize_window()
wait = WDW(driver, 10)    

# Go to Google
driver.get('https://www.google.com')

# Find the search box element by its name attribute
wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@id='APjFqb']"))).send_keys("Test Hello", Keys.ENTER)      # Search bar click and type  

