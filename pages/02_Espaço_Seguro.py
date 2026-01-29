import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.title("Espaço Seguro - Fica Aqui Entre Nós")


def carregar_animacao(url: str):
    requisicao = requests.get(url)
    if requisicao.status_code != 200:
        return None
    return requisicao.json()


url_animacao = "https://lottie.host/3dbc9002-6208-46b8-87c1-47d520ac91d0/sXQz6oosq4.json"
animacao = carregar_animacao(url_animacao)

st_lottie(animacao, key="animacao")
