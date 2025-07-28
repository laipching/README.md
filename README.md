# Aplicación Web de Análisis de Vehículos en Venta

Este proyecto es una aplicación web interactiva desarrollada con **Streamlit**, diseñada para visualizar de forma sencilla datos de anuncios de venta de vehículos en EE.UU.

## Objetivo del Proyecto

El objetivo es practicar habilidades clave de ingeniería de software y análisis de datos, incluyendo:
- Creación de entornos virtuales en Python
- Análisis exploratorio de datos con Jupyter Notebook
- Visualización de datos con Plotly Express
- Desarrollo de una aplicación web con Streamlit
- Uso de Git, GitHub y Render para control de versiones y despliegue

## Tecnologías Utilizadas

- Python
- pandas
- plotly.express
- streamlit
- Jupyter Notebook
- Git & GitHub
- Render (opcional para despliegue)

## Estructura del Proyecto

vehiculos-en-venta/
├── app.py # Aplicación Streamlit
├── vehicles_us.csv # Dataset
├── requirements.txt # Dependencias
├── README.md # Descripción del proyecto
└── notebooks
└── EDA.ipynb # Análisis exploratorio (EDA)


## Funcionalidades de la App

La aplicación permite:
- Visualizar un **histograma** del odómetro (kilometraje)
- Ver un **gráfico de dispersión** entre precio y kilometraje
- Interacción mediante botones

## Cómo ejecutar el proyecto

1. Clona este repositorio:  
   `https://github.com/laipching/vehiculos-en-venta.git`

2. Accede al directorio del proyecto:  
   `cd vehiculos-en-venta`

3. Crea un entorno virtual (opcional pero recomendado):  
   `python -m venv env`

4. Activa el entorno virtual:  
   - En Windows: `.\env\Scripts\activate`  
   - En macOS/Linux: `source env/bin/activate`

5. Instala las dependencias necesarias:  
   `pip install -r requirements.txt`

6. Ejecuta la aplicación:  
   `streamlit run app.py`


## Despliegue del Proyecto

Puedes ver la aplicación en funcionamiento en el siguiente enlace:

[Análisis de Vehículos en Venta](https://analisis-vehiculos-app.onrender.com)

## 🗓️ Versión del Proyecto

Versión 1.0 - Julio 2025  
Proyecto realizado como parte del bootcamp de análisis de datos de **TripleTen**.

## 👩‍💻 Créditos

Desarrollado por **Lai Yi Peña Ching**  
Bootcamp: **TripleTen – Análisis de Datos**
