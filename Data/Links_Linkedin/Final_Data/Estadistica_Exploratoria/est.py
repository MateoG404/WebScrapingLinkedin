import pandas as pd
from collections import Counter
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
    
    for df in list_df:
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

    df['PROGRAMA_PREGRADO'] = df['PROGRAMA_PREGRADO'].apply(limpiar_texto)
    
    df['PROGRAMA_PREGRADO'] = df['PROGRAMA_PREGRADO'].apply(mapeo_carrera)
    print("aaaa")
    print(df['CAMPO_ESTUDIO_antes_mapeo'][10:])

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
    
    #creacion_barras_simple(df_trabajos,df_trabajos['Category'],df_trabajos['Count'])
 
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

    # Set up the plots
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

def mapeo_carrera(field):
    field = unidecode(field.lower().strip())
    print(field)

    if 'telecommunications' in field or 'computing' in field or 'systems' in field or 'tecnologias' in field or 'software' in field or 'data'in field or 'java' in field or 'informacion' in field or 'information' in field:
        return 'Ingeniería de Sistemas y Computación'
    
    if 'agricola' in field or 'environnement' in field:
        return 'Ingeniería Agricola'

    if 'chimique' in field or 'cosmetologia' in field: 
        return 'Ingeniería Química'
    
    if 'datos' in field or 'telecomunicaciones' in field or 'computer'  in field or 'programacion'  in field or 'automatizacion' in field or 'informatica' in field or 'computador'  in field or 'informatics'  in field:
         return 'Ingeniería de Sistemas y Computación'
    
    if  'operations' in field or 'commerce'in field or 'industrial' in field or 'supply' in field or 'management' in field or 'industriel'in field:
        return 'Ingeniería Industrial'
    
    if 'matematicas' in field or 'mathematics' in field or 'statistics' in field:
        return 'Ciencias Puras'
    
    if 'marketing' in field or 'contabilidad' in field or  'finanzas' in field or 'business' in field or 'administracion' in field or 'economics' in field or 'gerencia' in field:
        return 'Administración de Empresas'
    
    if 'artes' in field or 'arquitectura' in field:
        return 'Artes'
    
    if 'geotecnica'in field or 'materiales' in field or 'hydraulique'  in field or 'civil' in field or ' hidraulicos' in field or 'structural' in field :
        return 'Ingeniería Civil'
    
    if 'english' in field or 'idiomas' in field :
        return 'Ciencias Humanas'
    
    if 'especializacion' in field or 'engineer' in field or 'adultos' in field or 'alimentos' in field or 'ingenierie' in field or 'incendios' in field or 'diplomado' in field or 'investigacion' in field: 
        return 'Otras especializaciones ingeniería'

    if 'renovables' in field :
        return 'Ingeniería Eléctrica y Electrónica'

    if  'protecciones' in field or 'mecatronica' in field or'control' in field or 'mechatronic' in field or 'mecanica' in field or 'process' in field:
        return 'Ingeniería Mecatrónica y Mécanica'

    if 'electricidad' in field:
        return 'Ingeniería Eléctrica y Electrónica'
    
    

    return field

def eda_universidad(df):
    
    
    university_counts = df['UNIVERSIDAD'].value_counts().reset_index()
    university_counts.columns = ['UNIVERSIDAD', 'Count']

    # Plotting
    plt.figure(figsize=(12, 8))
    ax = sns.barplot(x='Count', y='UNIVERSIDAD', data=university_counts.head(20))  # Show top 20 universities

    # Adding annotations to each bar
    for p in ax.patches:
        ax.annotate(f'{int(p.get_width())}', (p.get_width(), p.get_y() + p.get_height() / 2),
                    ha='left', va='center')

    plt.title('Frequency of Each University')
    plt.xlabel('Count')
    plt.ylabel('University')
    plt.show()
    
    # For CAMPO_ESTUDIO
    # Standardize the text and combine similar categories
    df['CAMPO_ESTUDIO'] = df['CAMPO_ESTUDIO'].apply(lambda x: unidecode(str(x).lower().strip()))#.str.strip().str.lower()
    
    df['CAMPO_ESTUDIO_antes_mapeo'] = df['CAMPO_ESTUDIO'].copy()
    

    replacement_dict = {
    'ingenieria electronica':'Ingeniería Eléctrica y Electrónica',
    'ingenieria electrica': 'Ingeniería Eléctrica y Electrónica',
    'ingenieria':'Otras especializaciones ingeniería',
    'no':'Otras especializaciones ingeniería',
    'ingenieria quimica': 'Ingeniería Química',
    'ingenieria civil/ geotecnia':'Ingeniería Civil',
    'mechatronics engineer':'Ingeniería Mecatrónica y Mécanica',
    'industrial engineering': 'Ingeniería Industrial',
    'mechanical engineering': 'Ingeniería Mecatrónica y Mécanica',
    'ingeniero agricola': 'Ingeniería Agricola',
    'computer science':'Ingeniería de Sistemas y Computación',
    'chemical engineering':'Ingeniería Química',
    'ingenieria de sistemas':'Ingeniería de Sistemas y Computación',
    'ingenieria electrica': 'Ingeniería Eléctrica y Electrónica',
    'ingenieria electronica, robotica y mecatronica':'Ingeniería Eléctrica y Electrónica',
    'ingenieria civil':'Ingeniería Civil',
    'ingenieria mecanica': 'Ingeniería Mecatrónica y Mécanica',
    'civil engineering':'Ingeniería Civil',
    'ingenieria de sistemas':'Ingeniería de Sistemas y Computación',
    'ingenieria industrial':'Ingeniería Industrial',
    'ingenieria electrica':'Ingeniería Eléctrica y Electrónica',
    'ingenieria electronica, robotica y mecatronica':'Ingeniería Eléctrica y Electrónica',
    'ingenieria industrial':'Ingeniería Industrial',
    'ingenieria agricola': 'Ingeniería Agricola',
    'ingenieria mecanica': 'Ingeniería Mecatrónica y Mécanica',
    'ingenieria quimica':'Ingeniería Química',
    'electrical and electronics engineering': 'Ingeniería Eléctrica y Electrónica',
    'ingenieria electrica y electronica': 'Ingeniería Eléctrica y Electrónica',
    'gestion de proyectos':'Administración de Empresas',
    'mechatronics, robotics, and automation engineering':'Ingeniería Mecatrónica y Mécanica',
    'administracion y gestion de empresas, general':'Administración de Empresas',
    'ingenieria de sistemas y computacion':'Ingeniería de Sistemas y Computación',
    'computer software engineering':'Ingeniería de Sistemas y Computación',
    'ingenieria de software':'Ingeniería de Sistemas y Computación',
    'electrical engineering': 'Ingeniería Eléctrica y Electrónica',
    'engineering':'Otras especializaciones ingeniería',
    'project management':'Administración de Empresas',
    'ingenieria electrica, electronica y de comunicaciones': 'Ingeniería Eléctrica y Electrónica',
    'business administration and management, general':'Administración de Empresas',
    'ingenieria informatica':'Ingeniería de Sistemas y Computación',
    'derecho':'Ciencias Humanas',
    'ensenanza de ingles como lengua extranjera':'Ciencias Humanas',
    'ingenieria estructural':'Ingeniería Civil',
    'ciencia y tecnologia de los alimentos':'Otras especializaciones ingeniería',
    'systems engineering':'Ingeniería de Sistemas y Computación',
    'ingenieria mecatronica':'Ingeniería Mecatrónica y Mécanica',
    'inteligencia artificial':'Ingeniería de Sistemas y Computación',
    'computer engineering':'Ingeniería de Sistemas y Computación',
    'marketing':'Administración de Empresas',
    'mechatronics engineering':'Ingeniería Mecatrónica y Mécanica',
    'ingenieria':'Otras especializaciones ingeniería',
    'desarrollo de aplicaciones web':'Ingeniería de Sistemas y Computación',
    'electronics engineering': 'Ingeniería Eléctrica y Electrónica',
    'data science':'Ingeniería de Sistemas y Computación',
    'economia':'Administración de Empresas',
    'computer and systems engineering':'Ingeniería de Sistemas y Computación',
    'tecnologia de la informacion':'Ingeniería de Sistemas y Computación',
    'geotecnia':'Ingeniería Civil',
    'gerencia de proyectos':'Administración de Empresas',
    'ciencias de la computacion':'Ingeniería de Sistemas y Computación',
    'emprendimiento/estudios sobre emprendimiento':'Administración de Empresas',
    'agricultural engineering': 'Ingeniería Agricola',
    'gestion de la construccion':'Ingeniería Civil',
    'gestion logistica, de materiales y de la cadena de suministro': 'Ingeniería Industrial',
    'tecnologia/tecnico de ingenieria electrica, electronica y de comunicaciones': 'Ingeniería Eléctrica y Electrónica',
    'finanzas, general':'Administración de Empresas',
    'estadistica':'Ciencias Puras',
    'ingenieria de transporte/ingenieria de trafico':'Otras especializaciones ingeniería',
    'automatizacion industrial':'Otras especializaciones ingeniería',
    'ingenieria civil':'Ingeniería Civil',
    'engineering/industrial management': 'Ingeniería Industrial',
    'quimica':'Ciencias Puras',
    'business':'Administración de Empresas',
    'sistemas y computacion':'Ingeniería de Sistemas y Computación',
    'sistemas':'Ingeniería de Sistemas y Computación',
    'mecanica':'Ingeniería Mecatrónica y Mécanica',
    'ingenieria biomedica/medica':'Otras especializaciones ingeniería',
    'logistics, materials, and supply chain management':'Ingeniería Industrial',
    'gerencia':'Administración de Empresas',
    'psicologia':'Ciencias Humanas',
    'mechanical engineer':'Ingeniería Mecatrónica y Mécanica',
    'auditoria':'Otras especializaciones ingeniería',
    'desarrollo de paginas web, contenido digital/multimedia y recursos informaticos':'Ingeniería de Sistemas y Computación',
    'ingenieria informatica':'Ingeniería de Sistemas y Computación',
    'ingenieria electrica y electronica':'Ingeniería Eléctrica y Electrónica',
    'ingenieria agricola':'Ingeniería Agricola',
    'gestion de proyectos':'Administración de Empresas',
    'ingenieria de sistemas y computacion':'Ingeniería de Sistemas y Computación',
    'administracion y gestion de empresas, general':'Administración de Empresas',
    'ingenieria ambiental':'Otras especializaciones ingeniería',
    'mecanica industrial':'Ingeniería Mecatrónica y Mécanica',
    'gestion de recursos humanos/administracion de personal, general':'Administración de Empresas',
    'seguridad informatica y de sistemas':'Ingeniería de Sistemas y Computación',
    'food science and technology':'Otras especializaciones ingeniería',
    'ingenieria de materiales':'Otras especializaciones ingeniería',
    'educacion secundaria':'Ciencias Humanas',
    'pedagogia':'Ciencias Humanas',
    'genie civi':'Ingeniería Civil',
    'ingenieria geotecnica y geoambiental':'Ingeniería Civil',
    'hidrologia y gestion de recursos hidricos ':'Ingeniería Civil',
    'ingenierie electrique et electronique':'Ingeniería Eléctrica y Electrónica',
    'procesamiento de datos':'Ingeniería de Sistemas y Computación',
    'systems and computing engineering':'Ingeniería de Sistemas y Computación',
    'procesamiento de datos':'Ingeniería de Sistemas y Computación',
    'matematicas':'Ciencias Puras',
    'gestion industrial/de ingenieria':'Ingeniería Industrial',
    'calidad':'Ingeniería Industrial',
    '.':'Otras especializaciones ingeniería',
    'agricultura, actividades agricolas y actividades afines':'Ingeniería Agricola',
    'genie civil':'Ingeniería Civil',
    'arquitectura':'Artes',
    'ingenieria de la construccion':'Ingeniería Civil',
    'hidrologia y gestion de recursos hidricos':'Ingeniería Civil',
    'ingeniero civil':'Ingeniería Civil',
    'programacion informatica':'Ingeniería de Sistemas y Computación',
    'tecnologia informatica/tecnologia de sistemas informaticos':'Ingeniería de Sistemas y Computación',
    'electronic engineering':'Ingeniería Eléctrica y Electrónica',
    'educacion':'Ciencias Humanas',
    'electronic engineer':'Ingeniería Eléctrica y Electrónica',
    'tecnologia/tecnico de ingenieria de automatizacion':'Ingeniería de Sistemas y Computación',
    'tecnologia/tecnico de control de calidad':'Ingeniería de Sistemas y Computación',
    'tecnologia/tecnico auxiliar en sistemas informaticos':'Ingeniería de Sistemas y Computación',
    'innovacion':'Administración de Empresas',
    'none':'No se encontro campo de estudio',
    'information and comunication techonologies':'Ingeniería de Sistemas y Computación',
    'data analytics':'Ingeniería de Sistemas y Computación',
    'ingenieria  electronica':'Ingeniería Eléctrica y Electrónica',
    'mecatronica':'Ingeniería Mecatrónica y Mécanica',
    'derechos humanos':'Ciencias Humanas',
    'administracion y gestion de empresas':'Administración de Empresas',
    'genie des procedes':'Otras especializaciones ingeniería',
    'ingles':'Ciencias Humanas',
    'electrical, electronics and communications engineering'
    'electrical enginee':'Ingeniería Eléctrica y Electrónica',
    'software informatico y aplicaciones multimedia':'Ingeniería de Sistemas y Computación',
    'curso':'Ingeniería de Sistemas y Computación',
    'medio ambiente y naturaleza':'Ingeniería Agricola',
    'water resources engineering':'Ingeniería Agricola',
    'electrical engineer':'Ingeniería Eléctrica y Electrónica',
    'electrical, electronics and communications engineering':'Ingeniería Eléctrica y Electrónica',
    'maschinenbau':'Otras especializaciones ingeniería',
    'electricista':'Ingeniería Eléctrica y Electrónica',
    'materials science and engineering':'Ingeniería de Sistemas y Computación',
    'materials engineering':'Ingeniería de Sistemas y Computación',
    }
    
    df['CAMPO_ESTUDIO'] = df['CAMPO_ESTUDIO'].apply(mapeo_carrera)
    df['CAMPO_ESTUDIO'].replace(replacement_dict, inplace=True)
    

    print(df['CAMPO_ESTUDIO'].value_counts().head(30))
        
    # For CAMPO_ESTUDIO
    field_counts = df['CAMPO_ESTUDIO'].value_counts().reset_index()
    field_counts.columns = ['CAMPO_ESTUDIO', 'Count']

    plt.figure(figsize=(12, 8))
    ax2 = sns.barplot(x='Count', y='CAMPO_ESTUDIO', data=field_counts.head(10))  # Show top 20 fields of study

    # Adding annotations to each bar
    for p in ax2.patches:
        ax2.annotate(f'{int(p.get_width())}', (p.get_width(), p.get_y() + p.get_height() / 2),
                    ha='left', va='center')

    plt.title('Frecuencia de cada campo de estudio')
    plt.xlabel('Conteo')
    plt.ylabel('Campo de Estudio')
    plt.show()


    
    '''
    # For TITULO_OBTENIDO
    title_counts = df['TITULO_OBTENIDO'].value_counts().reset_index()
    title_counts.columns = ['TITULO_OBTENIDO', 'Count']

    plt.figure(figsize=(12, 8))
    ax1 = sns.barplot(x='Count', y='TITULO_OBTENIDO', data=title_counts.head(20))  # Show top 20 titles

    # Adding annotations to each bar
    for p in ax1.patches:
        ax1.annotate(f'{int(p.get_width())}', (p.get_width(), p.get_y() + p.get_height() / 2),
                    ha='left', va='center')

    plt.title('Frequency of Each Title Obtained')
    plt.xlabel('Count')
    plt.ylabel('Title Obtained')
    plt.show()
    '''


def campo_estudio(df):

    # Contar la frecuencia de cada campo de estudio
    campo_estudio_counts = df['CAMPO_ESTUDIO'].value_counts()
    resultados_artificial = campo_estudio_counts.filter(like='emprendimiento')
    print(resultados_artificial)

    # Inteligencia artificial & Data Science 49
    # Gestión de proyectos 105
    # Ingeniería estructural 47
    # Ciencia y tecnología de los alimentos  38
    # Desarrollo web / mobile 80
    # Emprendimiento/Estudios sobre emprendimiento 13
    # Mechatronics, Robotics, and Automation Engineerin 83
    

    # Crear un DataFrame
    data = {
        'Campo': ['Inteligencia artificial & Data Science', 'Gestión de proyectos', 'Ingeniería estructural', 
                'Ciencia y tecnología de los alimentos', 'Desarrollo web / mobile', 
                'Emprendimiento/Estudios sobre emprendimiento', 'Mechatronics, Robotics, and Automation Engineering'],
        'Cantidad': [49, 105, 47, 38, 80, 13, 83]
    }

    df = pd.DataFrame(data)
    # Gráfica
    plt.figure(figsize=(12, 8))
    bars = plt.barh(df['Campo'], df['Cantidad'], color='purple')

    # Agregar etiquetas de número
    for bar in bars:
        plt.text(bar.get_width() - 3, bar.get_y() + bar.get_height()/2 - 0.1, str(bar.get_width()), va='center', ha='left', color='white')

    plt.xlabel('Cantidad')
    plt.ylabel('Campo')
    plt.title('Distribución de Campos de Especialización')
    plt.show()
    
    # Gestión de la construcción
    

    # Obtener los 10 campos de estudio más comunes para enfocar la visualización
    '''
    
    top_10_campo_estudio = campo_estudio_counts.nlargest(10)

    # Crear la gráfica
    plt.figure(figsize=(12, 6))
    top_10_campo_estudio.plot(kind='bar', color='skyblue')
    plt.title("Top 10 Campos de Estudio entre Egresados")
    plt.xlabel("Campo de Estudio")
    plt.ylabel("Número de Egresados")
    plt.xticks(rotation=45)
    plt.show()
    '''

# Función de mapeo
def map_language(language):
    language = unidecode(language).lower()  # Convertir a minúscula
    if 'ingles' in language or 'english' in language or 'anglais' in language or 'englisch' in language:
        return 'Inglés'
    elif 'espanol' in language or 'spanish' in language or 'espagnol' in language or 'spanisch' in language or 'espanhol' in language or 'spagnolo' in language:
        return 'Español'
    elif 'frances' in language or 'french' in language or 'français' in language or 'französisch' in language or 'francese' in language or 'francais' in language or 'franzosisch' in language: 
        return 'Frances'
    elif 'aleman' in language or 'german' in language or 'deutsch' in language or 'allemand'  in language or 'dutch' in language:
        return 'Alemán'
    elif 'portugiesisch' in language or 'portugues' in language or 'portugais'in language or 'portugués' in language:
        return 'Portugues'
    elif 'italiano'in language or 'italienisch' in language or 'italian' in language:
        return 'Italiano'
    else:
        return 'Otro'
def grafica_idiomas(df):

    df['LANGUAGE_MAPEADO'] = df['LANGUAGE'].apply( map_language)
    # Encontrar los índices de las filas donde 'LANGUAGE_MAPEADO' es 'Español'
    indices_to_drop = df[df['LANGUAGE_MAPEADO'] == 'Español'].index

    # Eliminar estas filas del DataFrame
    df.drop(indices_to_drop, inplace=True)

    #df.drop(df[(df['precio_unitario'] >400) & (df['precio_unitario'] < 600)].index, inplace=True)

    # Crear una tabla de contingencia para contar la frecuencia de cada combinación de 'LANGUAGE' y 'NIVEL'
    print(df['LANGUAGE_MAPEADO'].value_counts())
    contingency_table = pd.crosstab(df['LANGUAGE_MAPEADO'], df['NIVEL'])

    # Gráfico de barras apiladas
    contingency_table.plot(kind='bar', stacked=True, figsize=(10, 7))
    plt.xlabel('Idioma')
    plt.ylabel('Cantidad')
    plt.title('Distribución de Niveles por Idioma')
    plt.show()



def lluvia_palabras_skills(df):

    # Combina todas las filas de la columna 'SKILLS' en una sola cadena de texto
    text = ' '.join(str(row) for row in df['SKILLS'].dropna())

    # Usa Counter para obtener la frecuencia de cada palabra
    word_freq = Counter(text.split())

    # Filtrado de palabras comunes o irrelevantes (puedes ajustar esta lista según tus necesidades)
    stopwords = ["de", "y", "en", "la", "el", "None"] # Ejemplo de palabras a filtrar
    for word in stopwords:
        if word in word_freq:
            del word_freq[word]

    # Obtener las habilidades más comunes y sus frecuencias

    # Obtener las habilidades más comunes y sus frecuencias
    top_skills = word_freq.most_common(10)
    skills, counts = zip(*top_skills)

    # Creación del gráfico de barras
    plt.figure(figsize=(15, 8))
    bars = plt.bar(skills, counts, color='skyblue')
    plt.xlabel('Habilidades')
    plt.ylabel('Frecuencia')
    plt.title('Las 10 habilidades más comunes')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Agrega etiquetas con el valor exacto sobre cada barra
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 5, round(yval,2), ha='center', va='bottom', color='black')

    plt.show()

    # Código para la nube de palabras
    font_path = "/home/user/Desktop/MateoCodes/WebScrapingLinkedin/Documentation/arial.ttf"
    wordcloud




    # El resto del código para visualizar la nube de palabras
    font_path = "/home/user/Desktop/MateoCodes/WebScrapingLinkedin/Documentation/arial.ttf"
    wordcloud = WordCloud(font_path=font_path, background_color='white', width=800, height=400).generate_from_frequencies(word_freq)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def lluvia_palabras_descripcion(df):


    # Descargar los stopwords en caso de que no los tengas
    nltk.download('stopwords')
    from nltk.corpus import stopwords

    # Combina todas las filas de la columna 'DESCRIPCION' en una sola cadena de texto
    df = df[df['DESCRIPCION'].astype(str) != '[None]']
    df = df[df['DESCRIPCION'].astype(str) != 'I']
    text = ' '.join(str(row) for row in df['DESCRIPCION'].dropna())
    print()
    # Usa Counter para obtener la frecuencia de cada palabra
    word_freq = Counter(text.split())

    # Filtrado de palabras comunes o irrelevantes
    stop_words = set(stopwords.words('spanish')).union(stopwords.words('english'))
    for word in stop_words:
        if word in word_freq:
            del word_freq[word]
    # Eliminar la palabra 'I' del contador
    if 'I' in word_freq:
        del word_freq['I']
    # Obtener las palabras más comunes y sus frecuencias
    
    top_words = word_freq.most_common(10)
    words, counts = zip(*top_words)
    print(top_words)
    # Creación del gráfico de barras
    plt.figure(figsize=(15, 8))
    bars = plt.bar(words, counts, color='skyblue')
    plt.xlabel('Palabras')
    plt.ylabel('Frecuencia')
    plt.title('Las 10 palabras más comunes en DESCRIPCION')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Agrega etiquetas con el valor exacto sobre cada barra
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 5, round(yval,2), ha='center', va='bottom', color='black')

    plt.show()

    # Código para la nube de palabras
    font_path = "/home/user/Desktop/MateoCodes/WebScrapingLinkedin/Documentation/arial.ttf"
    wordcloud = WordCloud(font_path=font_path, background_color='white', width=800, height=400).generate_from_frequencies(word_freq)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

   
# Main Execution
if __name__ == "__main__":
    dataframes_list = get_dfs()
    
    if dataframes_list:
        
        #estadistica_exploratoria_egresados(dataframes_list[0])
        print(dataframes_list[1].info())
        print(dataframes_list[1]['DESCRIPCION'])
        #lluvia_palabras_descripcion(dataframes_list[1])
        #lluvia_palabras_skills(dataframes_list[1])
        #grafica_idiomas(dataframes_list[3])

        #campo_estudio(dataframes_list[0])
        #eda_universidad(dataframes_list[0])
        #print(dataframes_list[0].info())
        #print(dataframes_list[0].head())

        
    else:
        print("No DataFrames loaded.")


    '''
        try:
        
    except Exception as e:
        print(f"An error occurred: {e}")
    '''