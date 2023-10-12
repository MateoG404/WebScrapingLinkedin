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

class Busqueda:

    def __init__(self) -> None:
        load_dotenv()
        options = Options()
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--incognito')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def login_with_email(self):
        driver = self.driver
        email = driver.find_element(By.XPATH,'//*[@id="username"]')
        email.send_keys(os.environ.get('EMAIL'))
        password = driver.find_element(By.XPATH,'//*[@id="password"]')
        password.send_keys(os.environ.get('PASSWORD'))
        self.sesion = driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button').click()
        time.sleep(60)

    def scrape_profile(self, profile_url):
        
        driver = self.driver
        
        driver.get(profile_url)
        time.sleep(3)
        
        profile_data = {}
        
        # Extraer nombre
        name = driver.find_element_by_css_selector('.inline.t-24.t-black.t-normal.break-words').text
        profile_data['name'] = name
        
        # Extraer descripción
        description = driver.find_element_by_css_selector('.mt1.t-18.t-black.t-normal.break-words').text
        profile_data['description'] = description
        
        # Extraer ubicación
        location = driver.find_element_by_css_selector('.t-16.t-black.t-normal.inline-block').text
        profile_data['location'] = location
        
        # Extraer seguidores
        followers = driver.find_element_by_css_selector('.align-self-center.t-16.t-black--light').text
        profile_data['followers'] = followers
        
        # Extraer conexiones
        connections = driver.find_element_by_css_selector('.pv-top-card--list.pv-top-card--list-bullet.mt1').text
        profile_data['connections'] = connections
        
        # Aquí puede continuar con la extracción de más campos como 'about', 'experience', 'education', etc.
        
        return profile_data

    def abrir_navegador(self):
        self.url = "https://linkedin.com/uas/login"
        self.driver.get(self.url)
        self.login_with_email()

    def iniciar(self):
        self.abrir_navegador()
