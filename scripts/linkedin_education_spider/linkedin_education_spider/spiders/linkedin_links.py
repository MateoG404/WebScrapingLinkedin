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
            
if __name__ == "__main__":
    obj = LinkedinLinks()
    print(obj.get_links('/home/user/Desktop/MateoCodes/WebScrapingLinkedin/documentacion/NEW_DATA/clean_people_get_link.xlsx')[:2])

    