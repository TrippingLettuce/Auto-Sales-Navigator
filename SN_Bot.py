#Only works in Windoes 
# Colorama module: pip install colorama
from colorama import init, Fore, Style  # Do not work on MacOS and Linux.

# Selenium module imports: pip install selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.common.by import By

# Python default import.
from datetime import datetime as dt
from glob import glob
import sys
import os

#Not all imports are used


# ADD MORE (Look at prevoius CSV to find)
title_list = ['CEO','Co-Founder','Business Owner','Director Contract Manufacturing','Owner','COO','Principal Engineer','Founder','Sales Supervisor','Sales Closer','Sales Representative','Director of Operations','Principal','President of Operations','Chief Executive Officer','CTO','Business Development Lead','Marketing Executive']

#Notes
#Board Memeber or Software Dev if not allot of people



#Take in CSV
#Pandas to make it only DOMAIN and name