import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import numpy as np
from unidecode import unidecode
import geopandas as gpd
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

def mapeo_location(valor):
    valor = unidecode(valor.lower())
    location = {
        'colombia' : 'Colombia',
        'none' : 'Ninguno',
        'germany':'Alemania',
        'italy': 'Italia',
        'ecuador':'Ecuador',
        'france':'Francia',
        'portugal':'Portugal',
        'indonesia':'Indonesia',
        'spain':'España',
        'españa':'España',
        'united states': 'Estados Unidos',
        'mexico':'Mexico',
        'united kingdom': 'Reino Unido',
        'australia':'Australia',
        'venezuela':'Venezuela',
        'belgium':'Belgica',
        'canada':'Canada',
        'costa rica':'Costa Rica',
        'dominican':'Republica Dominicana',
        'czechia':'Republica Checa',
        'ireland':'Irlanda',
        'brazil':'Brazil',
        'peru':'Peru',
        'turkey':'Turquia',
        'switzerland':'Suiza',
        'japan':'Japon',
        'argentina':'Argentina',
        'arab':'Emiratos Arabes',
        'netherlands':'Paises Bajos',
        'salvador':'El Salvador',
        'austria':'Austria',
        'puerto rico':'Puerto Rico',
        'sweden':'Suecia',
        'china':'China',
        'guatemala':'Guatemala',
        'uruguay':'Uruguay',
        'malta':'Malta',
        'chile':'Chile',
        'israel':'Israel',
        'qatar':'Qatar',
        'panama':'Panama',
        'finland':'Finlandia',
        'estonia':'Estonia',
        'denmark':'Dinamarca',
        'norway':'Noruega'
    }
    for clave, mapeo in location.items():
        if clave in valor:
            return mapeo
    
    return valor#.capitalize()#.replace(" ","")

def creacion_barras(df,x,y,hue= None):
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

def creacion_barras_simple(df,x,y,hue = None):

    # Create bar chart
    plt.figure(figsize=(15, 8))
    ax = sns.barplot(x=x, y=y, hue=hue, data=df)
    plt.xticks(rotation=45)
    plt.title('Conteo de Personas por Carrera y Sexo')

    # Añadir etiquetas numéricas
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='baseline')

    # Show the chart
    plt.show()

def estadistica_exploratoria_egresados(df):
    # Normalizar los datos para programa_egresado
    

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
    
    df['LUGAR_VIVE'] = df['LUGAR_VIVE'].apply(mapeo_location)

    location_counts = df['LUGAR_VIVE'].value_counts().reset_index()
    location_counts.columns = ['LUGAR_VIVE', 'Conteo']

    
    # Creación de plots
    #creacion_plots(location_counts)

    #creacion_barras(grouped_sex,'PROGRAMA_PREGRADO','Conteo','SEXO')
    #print(df['LUGAR_VIVE'])
    
    #creacion_plots(location_counts)
    #crear_mapa(location_counts)
    
    df_trabajos = categorizar_trabajos(df['CURRENTLY_JOB'],df_completo=df,custom_categories=None)
    print(df_trabajos)
    creacion_barras_simple(df_trabajos,df_trabajos['Category'],df_trabajos['Count'])

def categorizar_trabajos(df_serie, df_completo ,custom_categories=None):
    df = pd.DataFrame(data = {'CURRENTLY_JOB': df_serie})
    
    # Text Preprocessing: Tokenize and remove special characters
    df['Processed_Titles'] = df['CURRENTLY_JOB'].apply(lambda x: word_tokenize(re.sub(r'[^\w\s]', '', unidecode(x.lower()))))
    
    # Use custom categories if provided, else use default
    categories = custom_categories if custom_categories else {


        'software y tecnología': ['systems','dev','development','technical','programador','cloud','ibm','datos','globant','ios','system','android','ai', 'ml','ia','bigdata', 'desarrollador','computer','sistemas','computación','machine learning','machinelearning','data','software', 'tech', 'information', 'unix admin', 'pythonista', 'automatization', 'data architecture', 'project management', 'azure', 'prompt engineering', 'software development', 'sr. cloud infra. architect', 'tendering specialist', 'simulation specialist', 'salesforce specialist', 'lead cloud engineer', 'aws certified solutions architect', 'tech lead frontend', 'javascript', 'react', 'react native', 'angular', 'data scientist', 'machine learning', 'data scientist at fna', 'devops', 'software engineer', 'developer', 'data analyst', 'data scientist', 'backend developer', 'ingeniero de sistemas', 'computing', 'computer and systems engineer', 'full-stack engineer', 'developer', 'software engineer', 'java developer', 'backend developer', 'risk management', 'data analyst', 'data engineer', 'data engineer', 'data analyst', 'senior data engineer', 'analista de información', 'analista de tecnología', 'ethical hacker', 'programming analyst', 'software engineer', 'developer', 'cto', 'backend', 'devsecops', 'sre', 'test automation', 'unity', 'python', 'data science', 'game developer', 'game programmer', 'software dev'],
        'academia y educación': ['profesor',    'Universidad','I+D+i','grado','investigador','research','études','docteur','attended','student','investigacion','research assistant', 'corrector de estilo y editor', 'comunicador social - periodista', 'm.sc. management student at tum', 'estudiante', 'phd student', 'master', 'research assistant', 'docente', 'biophysicist', 'nanotechnology', 'laboratory', 'estudiante', 'phd student', 'master', 'mba', 'bachelor', 'phd. student', 'profesor', 'docente', 'teacher', 'educational', 'estudiante', 'docente', 'master', 'phd', 'research assistant', 'laboratory coordinator'],
        'ingeniería civil': ['materials','materiales','structural','infraestructura','pavimentos','estructuras','estructural','construction','magister en tecnología de materiales', 'ingeniero residente', 'm.sc. on engineering and construction management', 'structural engineering', 'ingeniero civil', 'civil engineer', 'civil'],
        'ingeniería mecanica y mecatronica': ['mecatronico','mechatronic','mecánica','mechanical','mechatronics', 'flight simulator technician', 'mechatronics engineer', 'cars', 'automation', 'control engineer', 'automatización', 'ingeniero mecánico', 'mechanical engineer', 'ingeniería aeroespacial', 'mecánico'],
        'ingeniería agricola': ['ingenieria agricola','ingeniera agrícola','agrícola', 'm.sc. en manejo sostenible de agua y suelo', 'ingeniera agrícola', 'ingeniero agricola', 'agricultural engineer - universidad nacional de colombia', 'ingeniero agrícola', 'agricultural engineer', 'ingeniería agrícola', 'agrícola'],
        'ingeniería quimica': ['ingeniera química','process','ingenieria química','planta','chemical','formulation scientist', 'analista químico', 'r+d / chemical engineering / cosmetic chemistry', 'chemistry', 'chemical process engineer', 'ingeniero químico', 'chemical engineer', 'ingeniería bioquímica', 'químico'],
        'ingeniería electrica y electronica': ['electricista','energy','enel','electrical','electrónico','especialista eléctrico', 'hydrology and hydraulics', 'hydrometry', 'irrigation', 'water resources modeling', 'environmental', 'sustainability', 'sustainable', 'renewable energy', 'energy management', 'solar energy', 'wind energy', 'hydrogen', 'energías renovables', 'environmental conservation', 'ingeniería eléctrica', 'hydraulic', 'geotechnical'],
        'ingenieria de alimentos': ['food science', 'beverage', 'foods'],
        'ingenieria industrial': ['industrial','revenue management', 'simulation specialist', 'practicante de manufactura', 'ingeniera de calidad', 'risk', 'security', 'it compliance', 'logistics', 'supply chain', 'procurement'],
        'ingenieria ambiental': ['ingeniera ambiental', 'ms in environment and resource management'],
        'ingeniería electronica': ['electronic','electronica','electronic engineering', 'electronic engineer', 'ingeniero electrónico', 'electronic'],
        'arquitectura y diseño': ['diseño','arquitecto', 'diseñador', 'interiorista'],
        'control de procesos': ['calidad', 'procesos','quality', 'process specialist', 'analista de calidad'],
        'transporte y logistica': ['movilidad','transporte','logistica','jefe de logística de abastecimiento', 'planning professional', 'warehouse coordinator', 'planeación', 'logistics', 'transporte', 'supply chain manager', 'head of postharvest operations'],
        'operación y mantenimiento': ['mantenimiento', 'operations', 'production'],
        'bioingenieria y farmacia': ['pharmaceutical marketing', 'pharma industry', 'biotecnología', 'medicina', 'healthcare'],
        'servicio cliente': ['cliente','servicio de atención al cliente', 'customer service', 'support', 'customer care', 'customer success'],
        'emprendimiento y liderazgo': ['jefe','cheaf','lider','leader','ceo','entrepreneur', 'co-founder', 'cto', 'leadership', 'emprendedor', 'entrepreneur', 'co-founder', 'manager', 'gerente', 'director', 'project manager', 'asesor técnico', 'business analyst', 'coordinador', 'project manager', 'gerente general', 'director de proyecto'],
        'ventas y marketing': ['financial','finan','costos','comercial','profesional en calidad y gestión comercial', 'market development specialist', 'commercial specialist', 'negociador', 'sales specialist', 'coordinadora growth marketing', 'especialista de producto'],
        'consultoria': ['consultoría','consultant','senior consultant', 'quality assurance', 'iso', 'compliance', 'auditor', 'haccp'],
        'ley y gobierno': ['patentes','ley','derecho', 'legal', 'governance'],   
        'finanzas y negocios': ['finanzas','financiero','business','negocios','salesforce','business service officer', 'regional territory planning specialist', 'senior consultant', 'financial & admin business associate', 'auxiliar administrativo', 'financial analyst', 'economía', 'economics', 'finance', 'business analyst', 'business intelligence', 'product manager', 'strategy', 'innovation', 'agile', 'project manager', 'project management', 'pmp', 'scrum master', 'portfolio administrator', 'business analyst', 'supply chain', 'scientific', 'commercial', 'negociador', 'sales', 'ingeniería de licitaciones', 'marketing', 'pre-sales', 'business intelligence', 'asesor', 'consultor', 'advisor', 'business analyst', 'coordinador', 'manager', 'gerente', 'director', 'project manager', 'supply chain', 'procurement', 'operational', 'financial & admin business associate'],
        'Ingenieria Aeroespacial': ['aeroespacial','espacio','aereo'],
        'Ingenieria especialista':['especialista','specialist'],
        'análisis de riesgos': ['riesgos','incendios.','profesional senior analisis de riesgo'],
        'Traducción y Linguistica': ['linguistic','cultura','cultural'],

        
        'Other': []

    
    }
    # Normalize categories
    normalized_categories = {re.sub(r'[^\w\s]', '', unidecode(k.lower())): [re.sub(r'[^\w\s]', '', unidecode(i.lower())) for i in v] for k, v in categories.items()}
    
    def categorize(title_tokens):
        for category, keywords in normalized_categories.items():
            if any(keyword in title_tokens for keyword in keywords):
                return category
        return 'Other'
    
    df['Category'] = df['Processed_Titles'].apply(categorize)
    

    # Create a DataFrame from the value counts
    category_counts_df = df['Category'].value_counts().reset_index()
    category_counts_df.columns = ['Category', 'Count']

    return category_counts_df

def crear_mapa(df):


    # Crear el gráfico   de pastel
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    # Merge the GeoDataFrame with your DataFrame
    merged = world.set_index('name').join(df.set_index('LUGAR_VIVE'))

    # Set up the plot
    fig, ax = plt.subplots(1, figsize=(15, 10))

    # Plot boundaries
    merged.boundary.plot(ax=ax)

    # Plot using logarithmic color scale
    merged['Log_Conteo'] = np.log(merged['Conteo'])

    # Set minimum and maximum values for the color scale
    val_min = np.log(1)  # Log of minimum value
    val_max = np.log(3200)  # Log of maximum value

    merged.plot(column='Log_Conteo', ax=ax, legend=False, cmap='OrRd',
                legend_kwds={'label': "Logarithmic Count by Country"},
                vmin=val_min, vmax=val_max)

    
    # Show the plot
    plt.show()


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