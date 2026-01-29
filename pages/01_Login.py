import streamlit as st
from datetime import date


st.header("Preencha com seus dados para entrar no espaço Fica Aqui Entre Nós🫂")

st.markdown("""---""")

with st.form("login_form"):
    
    nome = st.text_input("Informe seu Nome" , placeholder="Seu nome aqui")
    email = st.text_input("Informe seu E-mail", placeholder="seuemail@email.com")
    datanascimento = st.date_input("Data de Nascimento" , format="DD/MM/YYYY" , min_value=date(1900, 1, 1), max_value=date.today())
    botaocadastro = st.form_submit_button("Entrar no Espaço Seguro.")

    if botaocadastro:
        if not nome:
            st.error("Por favor, insira seu nome.")
        elif len(nome) < 3:
            st.error("Por favor, insira um nome válido com pelo menos 3 caracteres.")

