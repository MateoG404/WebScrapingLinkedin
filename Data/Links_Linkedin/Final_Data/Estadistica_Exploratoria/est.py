import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import numpy as np
import seaborn
from unidecode import unidecode
import pickle
import re

def get_dfs():
    # Open the different DataFrames
    path_dataframes = os.path.abspath(os.path.join(os.getcwd(), "..", "Preprocessing_Data"))
    
    list_df = [file for file in os.listdir(path_dataframes) if file.endswith('.pkl')]
    dataframes_list = []
    
    for df in list_df[1:2]:
        df_temp = pd.read_pickle(os.path.join(path_dataframes, df))
        dataframes_list.append(df_temp)
        
    
    return dataframes_list

def limpiar_texto(texto):
    texto = unidecode(texto)  # Eliminar tildes
    texto = re.sub(r'name: programa, dtype: object', '', texto)
    return texto.strip().lower()

def mapeo_carrera(valor):
    valor = unidecode(valor.lower())
    carreras = {
        'electrical': 'Ingeniería Electrica',
        'electricista':'Ingeniería Electrica',
        'mecanico': 'Ingeniería Mecánica',
        'data': 'Ingeniería de Sistemas y Computación',
        'software': 'Ingeniería de Sistemas y Computación',
        'junior': 'Ingeniería de Sistemas y Computación',
        'desarrollador': 'Ingeniería de Sistemas y Computación',
        'systems': 'Ingeniería de Sistemas y Computación',
        'developer': 'Ingeniería de Sistemas y Computación',
        'manager': 'Ingeniería de Sistemas y Computación',
        'químico':'Ingeniería Química',
        'energy':'Ingeniería Electrica',
        'mechatronics':'Ingeniería Mecatrónica',
        'fisicoquímico': 'Ingeniería Química',
        'agrícola': 'Ingeniería Agrícola',
        'agricola': 'Ingeniería Agrícola',
        'hydrology':'Ingeniería Agrícola',
        'ambiental': 'Ingeniería Agrícola',
        'tecnologo':'Ingeniería Química',
        'electronica' : 'Ingeniería Electronica',
        'electrónica' : 'Ingeniería Electronica',
        'electronic': 'Ingeniería Electronica',
        'mecatrónica': 'Ingeniería Mecatrónica',
        'mecatronica': 'Ingeniería Mecatrónica',
        'civil': 'Ingeniería Civil',
        'industrial': 'Ingeniería Industrial',
        'química': 'Ingeniería Química',
        'quimica': 'Ingeniería Química',
        'químico': 'Ingeniería Química',
        'quimico': 'Ingeniería Química',
        'chemical': 'Ingeniería Química',
        'sistemas': 'Ingeniería de Sistemas y Computación',
        'electrica': 'Ingeniería Electrica',
        'regulatorio': 'Ingeniería Electrica',
        'eléctrico': 'Ingeniería Electrica',
        'eléctrica': 'Ingeniería Electrica',
        'mecánica': 'Ingeniería Mecánica',
        'mecanica': 'Ingeniería Mecánica',
        'mechanical': 'Ingeniería Mecánica',
        'obra': 'Ingeniería Civil',
        'comercial':'Ingeniería Electrica',
        'constructora': 'Ingeniería Civil',
        'analista de información': 'Ingeniería Industrial',
        'ingeniero - un': 'Ingeniería Industrial',
        'not found': 'No Encontrado',
        'especialista eléctrico':'Ingeniería Electrica',
        'estudiante': 'No Encontrado'
    }

    for clave, mapeo in carreras.items():
        if clave in valor:
            return mapeo
    
    return 'No encontrado'

def creacion_barras(df,x,y,hue):
    plt.figure(figsize=(15, 8))
    ax = sns.barplot(x=x, y=y, hue=hue, data=df)
    plt.xticks(rotation=45)
    plt.title('Conteo de Personas por Carrera y Sexo')

    # Añadir etiquetas numéricas
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='baseline')


    plt.show()

def creacion_plots(df):

    fig, ax = plt.subplots(1, 1)
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    plt.show()

def estadistica_exploratoria_egresados(df):
    # Normalizar los datos para programa_egresado
    
    print("Conteo de personas por programa \n\n\n")

    df['PROGRAMA_PREGRADO'] = df['PROGRAMA_PREGRADO'].astype(str).str.strip().str.lower().str.replace('\n', '')

    df['PROGRAMA_PREGRADO'] = df['PROGRAMA_PREGRADO'].apply(limpiar_texto).apply(mapeo_carrera)

    grouped_df = df.groupby('PROGRAMA_PREGRADO').size().reset_index(name='Conteo')

    grouped_df = grouped_df.sort_values(by='Conteo', ascending=False)
    
    filas_problematicas = df[df['PROGRAMA_PREGRADO'] == 'Otro']

    grouped_sex = df.groupby(['SEXO', 'PROGRAMA_PREGRADO']).size().reset_index(name='Conteo')
    # Reemplazar 'male' por 'Male' en la columna 'SEXO'
    df['SEXO'].replace('male', 'Male', inplace=True)
    df['SEXO'].replace('female', 'Female', inplace=True)

    grouped_sex = grouped_sex.sort_values(by='Conteo', ascending=False)
    # Creación de plots
    #creacion_plots(grouped_sex)

    #creacion_barras(grouped_sex,'PROGRAMA_PREGRADO','Conteo','SEXO')
    
def modify_2(df):
    indices_problematicos = df[df['PROGRAMA_PREGRADO'] == 'Otro'].index

    
    for idx in indices_problematicos:
        current_job = df.loc[idx, 'CURRENTLY_JOB']
        print(current_job,df.loc[idx,'LINKEDIN_URL'])    
        # Aplicar el mapeo
        nuevo_programa = mapeo_carrera(current_job)
        
        # Actualizar el valor en el DataFrame
        df.loc[idx, 'PROGRAMA_PREGRADO'] = nuevo_programa
    
    grouped_df = df.groupby('PROGRAMA_PREGRADO').size().reset_index(name='Conteo')

    grouped_df.sort_values(by='Conteo', ascending=False)
    
    creacion_plots(grouped_df)

    path_data = os.path.abspath(os.path.join(os.getcwd(),"..","Preprocessing_Data"))
    with open(path_data + '/df_final_user.pkl','wb') as f :
        pickle.dump(df,f)




def modify_df(df):
    df.loc[24, 'PROGRAMA_PREGRADO'] = 'ingeniería civil'

    path_data = os.path.abspath(os.path.join(os.getcwd(),"..","Preprocessing_Data"))

    with open(path_data + '/df_final_user.pkl','wb') as f :
        pickle.dump(df,f)

# Main Execution
if __name__ == "__main__":
    dataframes_list = get_dfs()
    
    if dataframes_list:
        
        estadistica_exploratoria_egresados(dataframes_list[0])
        #print(dataframes_list[0].iloc[0])

        
    else:
        print("No DataFrames loaded.")


    '''
        try:
        
    except Exception as e:
        print(f"An error occurred: {e}")
    '''