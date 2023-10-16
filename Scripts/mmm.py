

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from linkedin_scraper import Person, actions
from selenium import webdriver
options = Options()
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--incognito')
    
driver =webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
email = "xineb45323@dixiser.com"
password = "c&'n~yuA3faM2Tr"
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal

time.sleep(20)
person = Person("https://www.linkedin.com/in/andre-iguodala-65b48ab5", driver=driver)