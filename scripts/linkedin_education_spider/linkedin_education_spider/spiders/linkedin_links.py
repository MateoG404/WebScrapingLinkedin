import pandas as pd
import os

class LinkedinLinks:

    def __init__(self):
        self.df_limpio = pd.DataFrame()
        self.df_sucio = pd.DataFrame()
        self.lista_archivos = []
        self.lista_archivos_leidos = []

    def lectura_archivos(self):
        self.path_root = '/home/user/Desktop/MateoCodes/WebScrapingLinkedin/documentacion/copy'
        self.lista_archivos = os.listdir(self.path_root)

        for archivo in self.lista_archivos:
            print("Comenzando lectura archivo ...", archivo)
            df_temp = pd.read_excel(self.path_root + "/" + archivo)
            self.limpieza_links(df_temp)

    def limpieza_links(self, archivo):
        df_limpio_temp = archivo[archivo['URL'].str.contains('linkedin', na=False)]
        df_sucio_temp = archivo[~archivo['URL'].str.contains('linkedin', na=False)]

        self.df_limpio = pd.concat([self.df_limpio, df_limpio_temp], ignore_index=True)
        self.df_sucio = pd.concat([self.df_sucio, df_sucio_temp], ignore_index=True)

    def remove_duplicates(self):
        self.df_limpio.drop_duplicates(subset=['URL'], keep='first', inplace=True)
        self.df_sucio.drop_duplicates(subset=['URL'], keep='first', inplace=True)


    def exportar(self,df,nombre):
        self.remove_duplicates()
        print(self.df_limpio.info())
        df.to_excel(self.path_root + "/" + nombre +".xlsx")

if __name__ == "__main__":
    obj = LinkedinLinks()
    obj.lectura_archivos()
    
    obj.exportar(obj.df_limpio,'df_limpio')
    obj.exportar(obj.df_sucio,'df_sucio')
