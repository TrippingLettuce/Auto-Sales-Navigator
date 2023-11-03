# ---------------------------------------------------------------------------------------------------------------- #
from datetime import datetime as dt
from glob import glob
import sys
import os
import time
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import simpledialog
import tkinter as tk
import threading
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# ---------------------------------------------------------------------------------------------------------------- #
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService           #! Change here for Chrome or Firefox
from webdriver_manager.firefox import GeckoDriverManager       
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Exception Packages
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException, NoSuchWindowException
# ---------------------------------------------------------------------------------------------------------------- #
## Options for Firefox Browser
options = webdriver.FirefoxOptions()
options.accept_insecure_certs = True
# ---------------------------------------------------------------------------------------------------------------- #


email = "Noah.wolfe3@gcu.edu"
password = "heartland#1"
folder_list = ["GCU Leads CXO","GCU Leads CXO 2","GCU Leads CXO 3"]
keywords = ["CEO", "CHIEF","CHIEF EXECUTIVE OFFICER", "CFO", "CHIEF FINANCIAL OFFICER", "COO", "CHIEF OPERATING OFFICER", "CTO", "CHIEF TECHNOLOGY OFFICER", "CMO", "CHIEF MARKETING OFFICER", "CIO", "CHIEF INFORMATION OFFICER", "CHRO", "CHIEF HUMAN RESOURCES OFFICER", "CCO", "CHIEF COMMUNICATIONS OFFICER", "CLO", "CHIEF LEGAL OFFICER", "CSO", "CBO", "CHIEF BUSINESS OFFICER", "CDO", "CHIEF DATA OFFICER", "CPO", "CHIEF PRODUCT OFFICER", "CRO", "CHIEF RISK OFFICER", "CVO", "CHIEF VISIONARY OFFICER", "CXO", "CHIEF EXPERIENCE OFFICER", "CNO", "CHIEF NETWORKING OFFICER"]
folder_size = 999

#Driver And Element Selection Page
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)     
driver.maximize_window()
wait = WDW(driver, 20)                                                              # Define Wait
driver.get('https://www.linkedin.com/checkpoint/lg/sign-in-another-account')        # Go to LinkedIn website
driver.find_element(By.ID, 'username').send_keys(email)             # Type ID & Password
driver.find_element(By.ID, 'password').send_keys(password)
# ---------------------------------------------------------------------------------------------------------------- #
# Sign in button click
driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()      # Button Click
time.sleep(15)



driver.get('https://www.linkedin.com/sales/search/people?query=(recentSearchParam%3A(id%3A3164850436%2CdoLogHistory%3Atrue)%2Cfilters%3AList((type%3ASCHOOL%2Cvalues%3AList((id%3A164037%2Ctext%3AGrand%2520Canyon%2520University%2CselectionType%3AINCLUDED)))%2C(type%3ACOMPANY_HEADCOUNT%2Cvalues%3AList((id%3AF%2Ctext%3A501-1000%2CselectionType%3AINCLUDED)))%2C(type%3ACURRENT_TITLE%2Cvalues%3AList((id%3A8%2Ctext%3AChief%2520Executive%2520Officer%2CselectionType%3AINCLUDED)))))&sessionId=CjtBQyooQLyF%2FxjOVPE4qQ%3D%3D')



wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search keywords']"))) # Wait until page load

folder =  "/html[1]/body[1]/div[1]/div[2]/ul[1]/li[1]/button[1]/div[1]/div[1]/div[1]/span[1]"
x = 1
folder_2 = "/html[1]/body[1]/div[1]/div[2]/ul[1]/li[2]/ul[1]/li[1]/button[1]/div[1]/div[1]/div[1]/span[1]"
folder_3 = "/html[1]/body[1]/div[1]/div[2]/ul[1]/li[2]/ul[1]/li[2]/button[1]/div[1]/div[1]/div[1]"
folder_4 = "/html[1]/body[1]/div[1]/div[2]/ul[1]/li[2]/ul[1]/li[3]/button[1]/div[1]"
folder_5 = "/html[1]/body[1]/div[1]/div[2]/ul[1]/li[2]/ul[1]/li[4]/button[1]/div[1]/div[1]/div[1]/span[1]"

while True:
    
    # Scroll
    if folder_size == 0:
        x = x + 1
        if x == 2:
            folder = folder_2
        elif x == 3:
            folder = folder_3
        elif x == 4:
            folder = folder_4
    
    #Click Page
    time.sleep(5)
    driver.find_element(By.XPATH, "//body/main[@role='main']/div/div/div/div/ol/li[1]").click() #
    actions = ActionChains(driver)

    
    li_count = len(driver.find_elements(By.XPATH, "//ol/li"))
    max_iterations = min(li_count, 24)
    listofindex = []

    
    print("Clicking Started")
        

    select_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/label[1]")))
    select_button.click()
    
    save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[2]/div[1]/button[1]/span[1]/span[1]")))
    save_button.click()
    
    folder_button = wait.until(EC.element_to_be_clickable((By.XPATH, f"{folder}")))
    folder_button.click()
    
    time.sleep(3)
    # Click this button 
    button_next = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Next']"))
    )
    button_next.click()
    # Click 
    #Wait 15 secounds 
    time.sleep(12)
    folder_size = folder_size - 1


