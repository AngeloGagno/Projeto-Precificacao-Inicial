import streamlit as st
from backend.calculate_price import Price
from backend.main import main
import streamlit as st


st.title("🏠 Precificação de Acomodações")

st.markdown(
    """
    Preencha as informações abaixo para calcular e armazenar os valores de diárias das acomodações.
    """
)

col1, col2 = st.columns(2)

with col1:
    N_acc = st.text_input(
        "🏢 **Nome da Acomodação**",
        placeholder="Digite o nome",
        help="Defina o nome do apartamento no sistema."
    )

with col2:
    tier_acc = st.selectbox(
        "⭐ **Tier da Acomodação**",
        options=[3,4,5],
        placeholder="Selecione o Tier",
        help="O Tier do apartamento é a classificação em estrelas."
    )

value = st.number_input(
    "💰 **Valor da Diária**",
    placeholder="Digite o valor no AirDna",
    step=1,
    min_value=1000,
    max_value=10000000,
    help="Insira o valor precificado no AirDna para a acomodação."
)

st.divider()
if st.button("📤 **Enviar Dados**"):
    price = Price(value=value,tier=tier_acc)   
    min_price = price.minimum_price()
    base_price = price.base_price()
    data = {'name':N_acc, 
            'price': value,
            'tier':tier_acc,
            'min_price':min_price,
            'base_price': base_price
            }
    main(data)