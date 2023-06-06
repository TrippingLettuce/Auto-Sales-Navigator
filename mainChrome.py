# ---------------------------------------------------------------------------------------------------------------- #
## Python default import packages.
# Colorama module: pip install colorama
# from colorama import init, Fore, Style  # Do not work on MacOS and Linux   #! Uncomment if you are using it.

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
from selenium.webdriver.chrome.service import Service as ChromeService       #! Change here for Chrome
from webdriver_manager.chrome import ChromeDriverManager       
from selenium.webdriver.common.action_chains import ActionChains

# Packages for web control
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Exception Packages
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException
# ---------------------------------------------------------------------------------------------------------------- #
## Options for Chrome Browser
## Options for Chrome Browser
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")                                     # Maximize the window tap
options.add_argument('--ignore-certificate-errors')

# ---------------------------------------------------------------------------------------------------------------- #
## Create a new instance of Chrome WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)     
driver.maximize_window()
wait = WDW(driver, 10)                                                              # Define Wait

driver.get('https://www.linkedin.com/checkpoint/lg/sign-in-another-account')        # Go to LinkedIn website
driver.find_element(By.ID, 'username').send_keys('Noah.wolfe3@gcu.edu')             # Type ID & Password
driver.find_element(By.ID, 'password').send_keys('Canyon1949!')
# ---------------------------------------------------------------------------------------------------------------- #
## Sign in button click
driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()      # Button Click
time.sleep(8)
driver.get('https://www.linkedin.com/sales/search/people')
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search keywords']"))) # Wait until page load

# ---------------------------------------------------------------------------------------------------------------- #
## Company Data Import
# Read CSV file (Make sure it is right csv)
#current_dir = os.getcwd()                                                           # Get the current directory
#file_path = current_dir + "/company_result/company_501_1k.csv"                     #! Chagne File name Depends on the company list
file_path = "C:\\Users\\VRLab\\Downloads\\Auto-Sales-Navigator-main\\Auto-Sales-Navigator-main\\company_result\\company_5k_10k_nonexist.csv"

fulldf = pd.read_csv(file_path)
dfcompany = fulldf["Company"]

# DataFrame to check not_found profile company list
not_found = pd.DataFrame(columns=['Name','Email','Company','Domain'])

# save_list folder name
folder_list = ['5k-10k 1.0']                           #! always make more capacity then expectation.
# ---------------------------------------------------------------------------------------------------------------- #

## Change the li[index] for tracking
# //body/main[@role='main']/div/div/div/div/ol/li[Change This Index]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]

# Click the search bar and type company name
# Get each company name For loop
for x in range(len(dfcompany)):
    print(dfcompany[x])                 # print- company name
    temp_company = dfcompany[x]
    #Define the list for company name
    companys_list = []
    position_list = []

    try:
        # Wait until the presence of Search Bar element. 
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search keywords']"))).send_keys(temp_company, Keys.ENTER)      # Search bar click and type  
        # Wait until the profile element is presence
        text_obj = wait.until(EC.presence_of_element_located((By.XPATH, "//body/main[@role='main']/div/div/div/div/ol/li[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]")))
        time.sleep(10)
        # Scroll
            #Click Page
        # driver.find_element(By.XPATH, "//div[@id='search-results-container']").click() ### Error Found
        driver.find_element(By.XPATH, "//body/main[@role='main']/div/div/div/div/ol/li[1]").click() #
            #Get Driver
        actions = ActionChains(driver)
            #Scroll Through Page
        for _ in range(10):  # scroll ammount
            actions.send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(0.2) # scroll time
        
        # Loop Through People (24 per page: Maximum element in the page)
        # Find the count of <li> elements
        li_count = len(driver.find_elements(By.XPATH, "//ol/li"))
        # print(li_count)                 # print - li count

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

                if company_obj == "":
                    continue
                
                company = company.replace(" ", "").lower()
                temp_company = temp_company.replace(" ", "").lower()
            # ------ After  : Do comparison action here ------ #
                # print("Position: " + position, "|", "Company: " + company)                                 # print- position & company
                #print(temp_compamny + "----" + company)
                if company == temp_company: # added strip method to erase the blank
                    companys_list.append(y)
                    position_list.append(position)
                    print("\n" + str(companys_list) + "\n")

                    # Mark in List
            # ------ Before : Do comparison action here ------ #
            except NoSuchElementException:
                print('No Such Element Exception -- companys_list')
                continue
            except TimeoutException:
                print('Timeout Exception -- companys_list')
                continue

                # Check Title and Company List
        # title_list = ['Chairman of the Board','President & CEO', 'CEO', 'Co-Founder', 'Business Owner', 'Director Contract Manufacturing', 'Owner', 'COO', 'Principal Engineer', 'Founder', 'Sales Supervisor', 'Sales Closer', 'Sales Representative', 'Director of Operations', 'Principal', 'President of Operations', 'Chief Executive Officer', 'CTO', 'Business Development Lead', 'Marketing Executive', 'CEO', 'Chief Executive Officer', 'C.E.O.', 'Founder', 'Co founder', 'Cofounder', 'Director of Development', 'Business Development', 'Retail', 'ecommerce', 'Digital Marketing', 'CMO', 'Chief Marketing Officer', 'CTO', 'Chief Technology Officer', 'Director of Marketing', 'Software', 'Fundraising', 'Partner', 'Donor', 'President', 'Owner', 'Partnership', 'Marketing manager']
        # Define the keyword that we are searching from the position instead
        keyword = ['ceo','president','lead','owner','engineer','senior','chief','partner','director','head','vp','evp','manager','advisor',
                'development','officer','executive','retail','fundraising','cto','cmo','founder','coo','chairman','honor','cfo','sr']

        # If no company found from the search, add that company to dataframe to trackdown the list.
        if len(companys_list) == 0:
            not_found_company_row = fulldf.iloc[x]
            add_row = pd.DataFrame([not_found_company_row], columns=not_found.columns)

            # Concatenate the original DataFrame with new row
            not_found = pd.concat([not_found, add_row], ignore_index=True)
            # print(not_found)

        elif len(companys_list) < 3:
            print("\n" + str(companys_list) + "\n")
            for m in companys_list:
                temp = wait.until(EC.element_to_be_clickable((By.XPATH, f"/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/ol[1]/li[{m}]/div[1]/div[1]/div[1]/label[1]"))) 
                temp = temp.find_element(By.XPATH, f"/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/ol[1]/li[{m}]/div[1]/div[1]/div[1]/label[1]")
                driver.execute_script("arguments[0].click();", temp)
                
        # Commpanys are more than 3
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
                if m < 3:
                    try:
                        wait.until(EC.element_to_be_clickable((By.XPATH, f"/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/ol[1]/li[{m}]/div[1]/div[1]/div[1]/label[1]"))).click() 
                        print(f"Clicked {m}") 
                    except ElementNotInteractableException:
                        print(f"Element Not Interactable Exception -- Clicking element m < 3")
                        continue
                    except TimeoutException:
                        print(f"Timeout Exception -- Clicking element m < 3")
                        continue
                elif m > 3:
                    try:
                        element = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/ol[1]/li[{m}]/div[1]/div[1]/div[1]/label[1]')))
                        element = element.find_element(By.XPATH, f'/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/ol[1]/li[{m}]/div[1]/div[1]/div[1]/label[1]')
                        # element = driver.find_element("xpath", f'/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/ol[1]/li[{m}]/div[1]/div[1]/div[1]/label[1]')
                        # driver.execute_script("arguments[0].scrollIntoView();", element)
                        driver.execute_script("arguments[0].click();", element)
                        print(f"Clicked {m}")
                    except (ElementNotInteractableException,NoSuchElementException):
                        print(f"Element Not Interactable Exception -- Clicking element m > 3")
                        continue
                    except TimeoutException:
                        print(f"Timeout Exception -- Clicking element m > 3")
                        continue
        # If company & position exist, save profile into the folder
        if len(companys_list) > 0:
            save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Save all selected leads to a custom list.']")))
            save_button.click()
            not_found.to_csv(f'C:\\Users\\VRLab\\Downloads\\Auto-Sales-Navigator-main\\Auto-Sales-Navigator-main\\COMPANY_NOT_FOUND\\Not_Found_List_Company_5k_10k_2.csv', index=False)

            # Find the parent element that contains the list of <li> elements
            save_list = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div[1]/div[2]/div[1]/div[2]/div/div[3]/div/div/ul/li[2]/ul')))
            save_list.find_element(By.XPATH, '/html/body/main/div[1]/div[2]/div[1]/div[2]/div/div[3]/div/div/ul/li[2]/ul')
            
            # Find the elements for folders
            child_li = save_list.find_elements(By.TAG_NAME, 'li')

            # Count the number of folder list
            li_count = len(child_li)
            
            # Loop through Folders
            for i in range(1, li_count + 1):
                try:
                    # Target folder
                    target = save_list.find_element(By.XPATH, f'/html/body/main/div[1]/div[2]/div[1]/div[2]/div/div[3]/div/div/ul/li[2]/ul/li[{i}]/div/div/div[1]').text
                    # Number of profile listed on the folder
                    storage = save_list.find_element(By.XPATH, f'/html/body/main/div[1]/div[2]/div[1]/div[2]/div/div[3]/div/div/ul/li[2]/ul/li[{i}]/div/div/div[2]').text

                    # Make the storage string into the integer
                    chars_to_replace = ['(', ',', ')', '*']
                    for char in chars_to_replace:
                        storage = storage.replace(char, '')
                    storage = int(storage)

            # if the folder is full, export csv file of current not_found company list
                    # if storage == 1000:
                    #     not_found.to_csv(f'COMPANY_NOT_FOUND/Not_Found_List_Company_100_500{len(folder_list)}.csv', index=False)

            # ---------------------------------------------------------------------------------------------------------------- #
            # Algorithm for countdown the storage number and save onto right folder
            # If target == folder_list[0] & ((1000 - storage) > len(companys_list)):
            #   click the folder
                    if target == folder_list[0] and ((1000 - storage) >= len(companys_list)):
                        driver.find_element(By.XPATH, f'/html/body/main/div[1]/div[2]/div[1]/div[2]/div/div[3]/div/div/ul/li[2]/ul/li[{i}]').click()
                        print('Saved Profile')
                        break
            # elif target == folder_list[0] & ((1000 - storage) < len(companys_list)):
            #   folder_list.pop(0) (pop the first list out of it)
                    elif target == folder_list[0] and ((1000 - storage) < len(companys_list)):
                        folder_list.pop(0)
                        driver.find_element(By.XPATH, f'/html/body/main/div[1]/div[2]/div[1]/div[2]/div/div[3]/div/div/ul/li[2]/ul/li[{i+1}]').click()
                        print('Saved Profile')
                except NoSuchElementException:
                    driver.find_element(By.XPATH, f'/html/body/main/div[1]/div[2]/div[1]/div[2]/div/div[3]/div/div/ul/li[2]/ul/li[{i}]').click()
                    print("NoSuchElementException -- saving to folder")
                    break
            # ---------------------------------------------------------------------------------------------------------------- #

            time.sleep(0.5)

            #! Export the not found list to csv file
            # not_found.to_csv(f'COMPANY_NOT_FOUND/Not_Found_List_Company_100_500_{count}.csv', index=False)

        driver.back()                               # Go to the back of the page

    except TimeoutException:
        print("TimeoutException -- Selenium Timeout")
        driver.back()                                      # Go to the back of the page
    

not_found.to_csv(f'C:\\Users\\VRLab\\Downloads\\Auto-Sales-Navigator-main\\Auto-Sales-Navigator-main\\COMPANY_NOT_FOUND\\Not_Found_List_Company_5k_10k_2.csv', index=False)
#Get pos


# ADD MORE (Look at prevoius CSV to find)

# ---------------------------------------------------------------------------------------------------------------- #
## Task Required
# 1) Auto Navigation for Sales Nav tab [x]
# 2) Scroll through the page and grab profile [x]
# 3) Compare correct company with required position [x]
#   - May require to find out right company name
# 4) Press check mark for people who will save [ ]
#   - Scroll down problem occurred (06/01/23 00:07)
# 5) Save people correspond to right folder [ ]
# ---------------------------------------------------------------------------------------------------------------- #
