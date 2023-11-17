import pandas as pd
import os

list_files = os.listdir(os.getcwd())

print(list_files)

for file in list_files:
    if file.endswith('.csv'):  # Asegurarse de que solo se procesen archivos CSV
        a = os.path.join(os.path.abspath(os.getcwd()), file)
        print("Leyendo ", file)
        try:
            df_temp = pd.read_csv(a, error_bad_lines=False, header=0)  # Usar la primera fila como encabezado
            xlsx_file = file.replace('.csv', '.xlsx')
            df_temp.to_excel(xlsx_file, index=False)  # Conservar los nombres de las columnas
        except Exception as e:
            print("Error al procesar el archivo:", file)
            print(e)


'''
# Asume que el archivo CSV se llama 'data.csv' y el archivo de salida deseado es 'data.xlsx'
csv_file = 'data.csv'
xlsx_file = 'data.xlsx'

# Leer el archivo CSV
df = pd.read_csv(csv_file)

# Guardar en formato Excel
df.to_excel(xlsx_file, index=False)
'''