from cgitb import text
import pandas as pd
import streamlit as st
from PIL import Image

imagem = Image.open('CapaDoData.jpg')
st.image(imagem)

st.title('Jornada Além dos Dados')
st.text('Aqui você encontrará uma analise dos sentimentos dos usuários do Twitter em')
st.text('relação aos candidatos a presidência do ano de 2022!')

df = pd.read_csv('Etapa_ 4_dataframe_apresentação.csv')

candidato_unico = sorted(df['Candidato'].unique())
selecionar_candidato = st.sidebar.multiselect('Candidato', candidato_unico, candidato_unico)

df_candidato_selecionado = df[df['Candidato'].isin(selecionar_candidato)]
st.write('Conjunto de Dados ' + str(df_candidato_selecionado.shape[0]) + ' linhas e ' + '6' + ' colunas.')

st.dataframe(df_candidato_selecionado)