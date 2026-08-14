import pandas as pd
import plotly.express as px
import streamlit as st

# Título / Cabeçalho do aplicativo
st.header('Dashboard de Anúncios de Vendas de Carros')

# Lendo os dados do arquivo CSV
car_data = pd.read_csv('vehicles.csv')

# Criar caixas de seleção para o usuário escolher quais gráficos deseja visualizar
build_histogram = st.checkbox('Criar um histograma de quilometragem')
build_scatter = st.checkbox(
    'Criar um gráfico de dispersão (Preço vs Quilometragem)')

# Se a caixa de seleção do histograma for marcada
if build_histogram:
    st.write('Criando um histograma para a coluna de quilometragem (odometer)...')
    # Criar o histograma
    fig_hist = px.histogram(
        car_data,
        x="odometer",
        title="Distribuição da Quilometragem dos Veículos"
    )
    # Exibir o gráfico Plotly interativo
    st.plotly_chart(fig_hist, use_container_width=True)

# Se a caixa de seleção do gráfico de dispersão for marcada
if build_scatter:
    st.write('Criando um gráfico de dispersão de Preço vs Quilometragem...')
    # Criar o gráfico de dispersão
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Relação entre Preço e Quilometragem"
    )
    # Exibir o gráfico Plotly interativo
    st.plotly_chart(fig_scatter, use_container_width=True)
