# WebScrapingLinkedin
# Proyecto de Web Scraping con Scrapy

## Propuesta de Extracción de Información de Egresados en LinkedIn

Esta es una breve descripción de la propuesta para la extracción de información de egresados en LinkedIn. La propuesta completa, con todos los detalles y el flujo del proceso, se encuentra en el siguiente documento PDF:

[Descargar Propuesta en PDF](Propuesta.pdf)

Este proyecto utiliza la biblioteca Scrapy para llevar a cabo tareas de web scraping en sitios web. A continuación, se detalla cómo instalar los requisitos necesarios para ejecutar el proyecto.

## Requisitos Previos

Asegúrate de tener instalado Python en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/) o utilizar un manejador de paquetes como `conda` si lo prefieres.

## Instalación de Dependencias

Para instalar las dependencias necesarias, sigue estos pasos:

1. **Clona el Repositorio**: Clona este repositorio en tu máquina local o descárgalo como archivo ZIP.

```bash
git clone https://github.com/MateoG404/WebScrapingLinkedin.git
```
2. **Actova Entorno Virtual**: Navega hasta el directorio para activar el entorno virtual y ejecuta:

```bash
source nombre_del_entorno/bin/activate
```

2. Ingresa al Directorio del Proyecto: Navega al directorio del proyecto que has clonado.

```bash

cd WebScrapingLinkedin
```
3. Instala las Dependencias: Ejecuta el siguiente comando para instalar las dependencias del proyecto utilizando pip.

```bash

pip install -r requirements.txt
```
4. Para hacer un webscraping debes ir a la carpeta linkedin_education_spider

```bash

cd linkedin_education_spider
```
5. Luego debes ejecutar el siguiente codigo para hacer el webscraping de los perfiles

```bash

scrapy crawl linkedin_people_profile -o salida.json

```

## Requerimientos funcionales

Creación de propuesta para extraer información de egresados en LINKEDIN la cual debe contener el flujo del proceso, un esquema de base de datos con la información que se extraiga y un documento corto en donde se indique el proceso a seguir. 

