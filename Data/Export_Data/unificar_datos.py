import pandas as pd
from unidecode import unidecode

'''
# Cargar el CSV
df = pd.read_csv('/home/user/Desktop/MateoCodes/WebScrapingLinkedin/Data/Export_Data/IDIOMAS.csv')

# Convertir todos los valores en la columna 'LANGUAGE' a minúsculas
df['LANGUAGE'] = df['LANGUAGE'].str.lower()


def map_language(language):
    language = unidecode(language).lower()  # Convertir a minúscula
    if 'ingles' in language or 'english' in language or 'anglais' in language or 'englisch' in language:
        return 'Inglés'
    elif 'castellano' in language or 'espanol' in language or 'spanish' in language or 'espagnol' in language or 'spanisch' in language or 'espanhol' in language or 'spagnolo' in language:
        return 'Español'
    elif 'frances' in language or 'french' in language or 'français' in language or 'französisch' in language or 'francese' in language or 'francais' in language or 'franzosisch' in language: 
        return 'Frances'
    elif 'aleman' in language or 'german' in language or 'deutsch' in language or 'allemand' in language or 'dutch' in language:
        return 'Alemán'
    elif 'Portugues' in language or 'portugiesisch' in language or 'portugues' in language or 'portugais' in language or 'portugués' in language:
        return 'Portugues'
    elif 'italien' in language or 'italiano' in language or 'italienisch' in language or 'italian' in language or 'Italiano' in language:
        return 'Italiano'
    elif 'japones' in language or 'japanese' in language or 'japones-japanese' in language:
        return 'Japones'
    elif 'russian' in language or 'ruso' in language or 'rusiiki' in language:
        return 'Ruso'
    else:
        return language



# Aplicar la función de mapeo a la columna 'LANGUAGE'
df['LANGUAGE'] = df['LANGUAGE'].apply(map_language)


# Guardar el archivo modificado
df.to_excel('IDIOMAS.xlsx', index=False)

'''
def normalize_university_name(name):
    name = unidecode(name).lower().strip()  # Convertir a minúsculas y remover acentos
    # Agrega aquí más reglas de normalización si es necesario
    return name


df = pd.read_csv('/home/user/Desktop/MateoCodes/WebScrapingLinkedin/Data/Export_Data/EDUCACION.csv')

print(df.info())

# Aplicar la normalización
df['UNIVERSIDAD'] = df['UNIVERSIDAD'].apply(normalize_university_name)

university_map = {

    # Universidad Nacional de Colombia
    'universidad nacional de colombia': 'Universidad Nacional de Colombia',
    'univerisdad nacional de colombia': 'Universidad Nacional de Colombia',
    'universidad nacional de colombia sede bogotá': 'Universidad Nacional de Colombia',
    'unal': 'Universidad Nacional de Colombia',
    'u.nal': 'Universidad Nacional de Colombia',
    'national university of colombia': 'Universidad Nacional de Colombia',
    'unversidad nacional de colombia': 'Universidad Nacional de Colombia',
    'universidada nacional de colombia': 'Universidad Nacional de Colombia',

    # Pontificia Universidad Javeriana
    'pontificia universidad javeriana': 'Pontificia Universidad Javeriana',
    'javeriana university': 'Pontificia Universidad Javeriana',

    # Universidad de Los Andes
    'universidad de los andes': 'Universidad de Los Andes',
    'andes university': 'Universidad de Los Andes',

    # Universidad de La Sabana
    'universidad de la sabana': 'Universidad de La Sabana',
    'la sabana university': 'Universidad de La Sabana',

    # Universidad Externado de Colombia
    'universidad externado de colombia': 'Universidad Externado de Colombia',
    'externado university': 'Universidad Externado de Colombia',

    # Universidad del Rosario
    'universidad del rosario': 'Universidad del Rosario',
    'rosario university': 'Universidad del Rosario',

    # Universidad de Antioquia
    'universidad de antioquia': 'Universidad de Antioquia',
    'university of antioquia': 'Universidad de Antioquia',

    # Universidad Politécnica de Valencia
    'universidad politecnica de valencia': 'Universidad Politécnica de Valencia',
    'polytechnic university of valencia': 'Universidad Politécnica de Valencia',
    'universitat politecnica de valencia (upv)': 'Universidad Politécnica de Valencia',

    # Universidad de Granada
    'universidad de granada': 'Universidad de Granada',
    'granada university': 'Universidad de Granada',

    # Servicio Nacional de Aprendizaje (SENA)
    'servicio nacional de aprendizaje (sena)': 'Servicio Nacional de Aprendizaje (SENA)',
    'sena': 'Servicio Nacional de Aprendizaje (SENA)',
    'servicio nacional de aprendizaje - sena.': 'Servicio Nacional de Aprendizaje (SENA)',
    'servicio nacional de aprendizaje – sena': 'Servicio Nacional de Aprendizaje (SENA)',

    # Otros ejemplos
    'universidad de la salle': 'Universidad de La Salle',
    'ef executive language institute': 'EF Executive Language Institute',
    'fundacion universitaria panamericana': 'Fundación Universitaria Panamericana',
    'insa strasbourg': 'INSA Strasbourg',
    'liceo nuestra senora de torcoroma': 'Liceo Nuestra Señora de Torcoroma',
    'fundacion universitaria empresarial de la camara de comercio de bogota': 'Fundación Universitaria Empresarial de la Cámara de Comercio de Bogotá',
    'asociacion colombiana de ciencia y tecnologia de alimentos': 'Asociación Colombiana de Ciencia y Tecnología de Alimentos',
    'universidad europea del atlantico': 'Universidad Europea del Atlántico',
    # Instituto Europeo de Posgrado
    'instituto europeo de posgrado - iep': 'Instituto Europeo de Posgrado',
    
    # Purdue University
    'purdue university': 'Purdue University',

    # Universidad del Norte
    'universidad del norte': 'Universidad del Norte',

    # Grenoble INP
    'grenoble inp - genie industriel': 'Grenoble INP',
    'grenoble inp - ense3': 'Grenoble INP',
    'grenoble inp - phelma': 'Grenoble INP',

    # Holberton School
    'holberton school': 'Holberton School',

    # Universidad Sergio Arboleda
    'universidad sergio arboleda': 'Universidad Sergio Arboleda',

    # Politécnico Grancolombiano
    'politecnico grancolombiano': 'Politécnico Grancolombiano',

    # Universidad Politécnica de Madrid
    'universidad politecnica de madrid': 'Universidad Politécnica de Madrid',

    # Universidad El Bosque
    'universidad el bosque': 'Universidad El Bosque',

    # Leibniz Universität Hannover
    'leibniz universitat hannover': 'Leibniz Universität Hannover',

    # Technical University of Munich
    'technical university of munich': 'Technical University of Munich',

    # Escuela Colombiana de Ingeniería Julio Garavito
    'escuela colombiana de ingenieria julio garavito': 'Escuela Colombiana de Ingeniería Julio Garavito',

    # Universidad Jorge Tadeo Lozano
    'universidad jorge tadeo lozano': 'Universidad Jorge Tadeo Lozano',

    # Massachusetts Institute of Technology
    'massachusetts institute of technology': 'Massachusetts Institute of Technology',
    'mitx courses': 'Massachusetts Institute of Technology',

    # British Council
    'british council': 'British Council',

    # Universidad ECCI
    'universidad ecci': 'Universidad ECCI',

    # Universidad de Costa Rica
    'universidad de costa rica ucr': 'Universidad de Costa Rica',

    # Stanford University
    'stanford university': 'Stanford University',

    # Karlsruhe Institute of Technology (KIT)
    'karlsruhe institute of technology (kit)': 'Karlsruhe Institute of Technology',

    # Universitat de Barcelona
    'universitat de barcelona': 'Universitat de Barcelona',

    # Universidad Libre
    'universidad libre': 'Universidad Libre',
    'universidad libre ®': 'Universidad Libre',

    # Universidad de Pamplona
    'universidad de pamplona': 'Universidad de Pamplona',

    # Universidad de Antioquia
    'universidad de antioquia': 'Universidad de Antioquia',

    # Coursera
    'coursera': 'Coursera',
    
}


df['UNIVERSIDAD'] = df['UNIVERSIDAD'].map(university_map).fillna(df['UNIVERSIDAD'])

# Obtener e imprimir los idiomas únicos
unique_languages = df['TITULO_OBTENIDO'].unique()
print(unique_languages)

# Guardar el archivo modificado
df.to_excel('EDUCACION.xlsx', index=False)