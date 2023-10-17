import pandas as pd
import os
import re

class LinkedinLinks:

    def __init__(self):
        self.df_limpio = pd.DataFrame()
        self.df_sucio = pd.DataFrame()
        self.lista_archivos = []
        self.lista_archivos_leidos = []

    def lectura_archivos(self, path):
        if os.path.exists(path):
            try:
                self.df_limpio = pd.read_excel(path)
            except Exception as e:
                print(f"Error al leer el archivo: {e}")
        else:
            print("La ruta del archivo no es válida.")

    def get_links(self, path):
        self.lectura_archivos(path)
        
        if not self.df_limpio.empty:
            if 'URL' in self.df_limpio.columns:
                self.url_list = list(self.df_limpio['URL'])
                return self.url_list
            else:
                return None

    def get_profiles(self,path):

        names = []
        self.get_links(path)

        
        for url in self.url_list:
            match = re.search(r'/in/([\w-]+)', url)
            if match:
                names.append(match.group(1))
                
        return names
    
    def get_profile(self,profile_name):
        match = re.search(r'/in/([\w-]+)', profile_name) 
        return match.group(1)
    
    def returnDataForBot(self):
        """
        Define various file paths for the web scraping operation.

        Returns:
            tuple: general_path, path_data_bot, file_to_scrape
        """
        # Determine the general path
        general_path = os.path.abspath(os.path.join(os.getcwd(), "..", "..", "..", ".."))

        # Specify the path to store scraped data
        path_data_bot = os.path.join(general_path, "Data", "Links_Linkedin", "BD_egresados", "Data_Bot")
        
        # Specify the Excel file to read
        file_to_scrape = os.path.join(path_data_bot, "Data_BotUnificacion_total.xlsx")
        
        df_data = pd.read_excel(file_to_scrape)
        return df_data
    
if __name__ == "__main__":
    obj = LinkedinLinks()
    obj.returnDataForBot()

    