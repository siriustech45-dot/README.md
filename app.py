import pandas as pd
import plotly.express as px
import streamlit as st

# Lendo os dados
car_data = pd.read_csv('vehicles_us.csv')

# Cabeçalho do aplicativo
st.header('Dashboard de Anúncios de Carros')

# Checkbox para histograma
build_histogram = st.checkbox('Criar um histograma')

if build_histogram:
    st.write('Criando um histograma para a coluna odometer')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para gráfico de dispersão
build_scatter = st.checkbox('Criar gráfico de dispersão')

if build_scatter:
    st.write('Criando um gráfico de dispersão: odometer vs price')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)