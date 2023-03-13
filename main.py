import os
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
load_dotenv()

chrome_driver_path = "C:\development\chromedriver.exe"
chr_options = webdriver.ChromeOptions()
chr_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chr_options)
driver.get("https://www.linkedin.com/")

phone_number_input = driver.find_element(By.NAME, "session_key")
password_input = driver.find_element(By.NAME, "session_password")

phone_number_input.send_keys("08163714177")
password_input.send_keys(os.getenv("PASSWORD"))



