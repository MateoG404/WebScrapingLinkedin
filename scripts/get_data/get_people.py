
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time


options = Options()
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
'''

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://linkedin.com/uas/login")
time.sleep(5)

# Creating a webdriver instance
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
                                                                                                                   
# This instance will be used to log into LinkedIn

# Opening linkedIn's login page
driver.get("https://linkedin.com/uas/login")

# waiting for the page to load
time.sleep(5)

# entering username
username = driver.find_element(By.ID, "username")

# In case of an error, try changing the element
# tag used here.

# Enter Your Email Address
username.send_keys("mateogutierremel@gmail.com")

# entering password
pword = driver.find_element(By.ID, "CMZrmx75")
# In case of an error, try changing the element
# tag used here.

# Enter Your Password
pword.send_keys("mateogutierremel@gmail.com")	

# Clicking on the log in button
# Format (syntax) of writing XPath -->
# //tagname[@attribute='value']
driver.find_element(By.XPATH, "//button[@type='submit']").click()
# In case of an error, try changing the
# XPath used here.
'''