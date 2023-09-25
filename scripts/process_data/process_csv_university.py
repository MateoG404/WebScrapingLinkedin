import pandas as pd

class File :

    def __init__(self, Path):
        
        self.PATH = Path 
        self.file = pd.read_excel(self.PATH,sheet_name='Sheet2')
        self.num_engineering = int


    def get_faculty(self,fac_name):
        
        print(self.file.info())        

arhivos = File('/home/user/Desktop/MateoCodes/WebScrapingLinkedin/documentacion/RE_EGR_ACR_TABLA DE DATOS 2022007.xlsx')

arhivos.get_faculty('ingenieria')
