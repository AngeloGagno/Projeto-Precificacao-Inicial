import streamlit as st
from backend.calculate_price import Price

st.header('Precificacao Inicial')
st.subheader('Projeto com o Objetivo de dar um panorama inicial do valor da diária dos apartamentos e enviar-los para um banco de dados para armanezar seus resultados')
tier = [3,4,5]
N_acc = st.text_input('Digite o Nome da Acomodacao(sem a Zona)', placeholder="Nome")
tier_acc = st.selectbox('Selecione o Tier do Acomodacao',options=tier, placeholder= 'Tier')
value = st.number_input('Digite o Valor encontrado', placeholder="Valor", step=1,min_value=0,max_value=10000000)


if st.button("Enviar"):
    price = Price(value=value,tier=tier_acc)   
    st.write(price.base_price())