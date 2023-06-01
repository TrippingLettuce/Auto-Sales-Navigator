# LinkedIn from Excel 

This repository contains a Python script that allows you to grab a list of company website links from an Excel file, validate their accessibility through HTTP requests, and automatically retrieve the profiles of high-level board members using the Selenium Python package. The retrieved information is then saved to a list for further analysis or processing.

## Purpose
The main purpose of this project is to streamline the process of finding and retrieving LinkedIn profiles of high-level executives from a list of company websites. By automating the validation of website accessibility and using Selenium to navigate LinkedIn, the script saves time and effort that would otherwise be spent manually searching for and compiling this information.

## Features
- Import company website links from an Excel file.
- Validate website accessibility through HTTP requests.
- Use Selenium to automate the retrieval of LinkedIn profiles.
- Collect information about high-level board members.
- Save the retrieved information to a list for further analysis.

## FlowChart
![Sales Navigator FlowChart](https://github.com/TrippingLettuce/linkedin_from_excel/assets/82426784/175ddef7-b2b4-4f54-a9a5-dadb2c32409e)

## Prerequisites
Before running the script, ensure you have the following:

Python (version 3.6 or higher) installed on your machine.
Selenium Python package installed. You can install it using the following command:
- pip install selenium

A compatible web driver for Selenium. The script supports various web drivers, such as ChromeDriver and GeckoDriver. Make sure to download the appropriate driver and add its location to your system's PATH variable.

## Usage
1) Clone the repository to your local machine:

[bash]
- git clone https://github.com/TrippingLettuce/linkedin_from_excel.git

2) Install the required dependencies by navigating to the repository's directory and executing the following command:
- pip install -r requirements.txt

3) Prepare your Excel (csv) file containing the list of company website links. Ensure that the file meets the following requirements:
- The website links should be in a single column.
- The first row of the column should contain the header "Website" (without quotes).
- The subsequent rows should contain the website links.

4) Open the main.py file in a text editor and update the following variables at the top of the script:
- EXCEL_FILE: Specify the path to your Excel file.
- SHEET_NAME: Specify the name of the sheet containing the website links.
- WEB_DRIVER: Specify the web driver you are using (e.g., "chrome" or "firefox").
- Run the script by executing the following command:
-- python main.py

The script will validate the website links, navigate LinkedIn using Selenium, and retrieve the profiles of high-level board members. The retrieved information will be saved to a file named output.txt in the repository's directory.

## Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the GCU student (Caleb and Kyungchan Im)'s License.
