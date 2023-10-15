import pandas as pd

def read_xlsx_from_sheet2(filename):
    # Leer solo la hoja 2 del archivo XLSX
    df = pd.read_excel(filename, sheet_name=1)  # Las hojas se indexan desde 0
    
    # Descartar la primera fila y reiniciar el índice
    df = df.iloc[1:].reset_index(drop=True)
    
    return df

# Uso de la función
filename = "documentacion/RE_EGR_ACR_TABLA DE DATOS 2022007.xlsx"
data = read_xlsx_from_sheet2(filename)
print(data)
