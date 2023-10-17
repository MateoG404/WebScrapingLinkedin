
'''
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
import csv
from dotenv import load_dotenv
import pandas as pd
import os

from class_selenium import Busqueda
from linkedin_links import LinkedinLinks

def login_to_linkedin(driver, username, password):
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)
    
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("password").send_keys(Keys.RETURN)
    time.sleep(3)

def scrape_profile(driver, profile_url):
    driver.get(profile_url)
    time.sleep(3)
    
    # Aquí puede añadir el código para extraer la información específica que necesita
    name = driver.find_element_by_css_selector('.inline.t-24.t-black.t-normal.break-words').text
    return {"name": name}

if __name__ == "__main__":
    busqueda_obj = Busqueda()
    busqueda_obj.iniciar()

    #print("buscando ..", nombre)
    busqueda_obj.driver.get("https://www.google.com")
    busqueda_google = busqueda_obj.driver.find_element(By.NAME, "q")
    busqueda_google.clear()

    objeto_linkedin = LinkedinLinks()
    lista_links = objeto_linkedin.get_links('/home/user/Desktop/MateoCodes/WebScrapingLinkedin/documentacion/NEW_DATA/clean_people_get_link.xlsx')
    
    lista_links = lista_links[500:502]
    
    for profile in lista_links:
        print(busqueda_obj.scrape_profile(profile))
    
    print(lista_links)

'''
'''

    busqueda_google.send_keys(nombre)
    busqueda_google.send_keys(Keys.RETURN)
'''

'''
    
    driver = webdriver.Chrome(executable_path="/path/to/chromedriver")
    login_to_linkedin(driver, "your_username", "your_password")
    
    profile_urls = ["https://www.linkedin.com/in/example1/", "https://www.linkedin.com/in/example2/"]
    for url in profile_urls:
        info = scrape_profile(driver, url)
        print(info)
    
    driver.quit()

'''