import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.read_csv('vehicles_us.csv')

# Título principal
st.title('Análisis de Vehículos en Venta 🚗📊')

# Botón 1: Histograma del odómetro
if st.button('Mostrar histograma del odómetro'):
    st.subheader('Histograma del Odómetro (km)')
    fig = px.histogram(df, x='odometer', title='Distribución del odómetro (km)')
    st.plotly_chart(fig, use_container_width=True)

# Botón 2: Gráfico de dispersión precio vs odómetro
if st.button('Mostrar gráfico de dispersión (precio vs odómetro)'):
    st.subheader('Relación entre precio y kilometraje')
    fig = px.scatter(
        df,
        x='odometer',
        y='price',
        title='Precio vs. Odómetro',
        labels={'odometer': 'Kilometraje', 'price': 'Precio (USD)'}
    )
    st.plotly_chart(fig, use_container_width=True)
