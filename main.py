import os
import time

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
load_dotenv()

chrome_driver_path = "C:\development\chromedriver.exe"
chr_options = webdriver.ChromeOptions()
chr_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chr_options)
driver.get("https://www.linkedin.com/")
driver.maximize_window()

# LOGGING IN
phone_number_input = driver.find_element(By.NAME, "session_key")
password_input = driver.find_element(By.NAME, "session_password")

phone_number_input.send_keys("08163714177")
password_input.send_keys(os.getenv("PASSWORD"))

sign_in_button = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/form[1]/div[2]/button')
sign_in_button.click()

# Skipping some checks
time.sleep(5)

skip_button = driver.find_element(By.CLASS_NAME, "secondary-action-new")
skip_button.click()

# Searching for jobs
time.sleep(20)

jobs_button = driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a/div/div/li-icon')
jobs_button.click()

time.sleep(5)
job_search_input = driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
job_search_input.send_keys("python developer")
job_search_input.send_keys(Keys.ENTER)