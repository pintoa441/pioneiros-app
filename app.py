import streamlit as st
import pandas as pd
import json
import os

# 1. Configuração da página
st.set_page_config(
    page_title="Pista de Progresso - Agrupamento 78",
    page_icon="⚜️",
    layout="wide"
)

# 2. Logótipo no topo e na barra lateral
if os.path.exists("logo_78.jpg"):
    st.sidebar.image("logo_78.jpg", use_container_width=True)

col_logo, col_titulo = st.columns([1, 4])
with col_logo:
    if os.path.exists("logo_78.jpg"):
        st.image("logo_78.jpg", width=100)
with col_titulo:
    st.title("⚜️ Caderno de Pista Digital")
    st.caption("Agrupamento 78 Arruda dos Vinhos - III Secção (Pioneiros)")

st.markdown("---")

# 3. Configurações de dados
PASSWORD_DIRIGENTE = "escuteiros78"
DB_FILE = "dados_pioneiros.json"

def load_data():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_data(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# 4. Estrutura dos Trilhos
TRILHOS_DATA = [
    {
        "area": "Desenvolvimento Físico",
        "trilhos": [
            {
                "id": "desempenho",
                "nome": "Desempenho",
                "descricao": "Ter preocupação com o desempenho físico e praticar atividades equilibradas.",
                "objetivos": ["F1 - Tenho preocupação com o meu desempenho físico."],
                "oportunidades": [
                    "Programar e executar um raid para a Equipa/Comunidade.",
                    "Promover uma palestra sobre atividade desportiva e saúde.",
                    "Criar um plano de treino pessoal e praticar exercício regular.",
                    "Organizar um torneio de provas desportivas."
                ]
            },
            {
                "id": "autoconhecimento",
                "nome": "Autoconhecimento",
                "descricao": "Aceitar-se como é, respeitando as diferenças físicas.",
                "objetivos": ["F2 - Aceito-me como sou e respeito as diferenças físicas."],
                "oportunidades": [
                    "Arranjar soluções para inclusão de pessoas com deficiência.",
                    "Promover um debate sobre prevenção do bullying.",
                    "Fazer uma análise de pontos fortes e limitações pessoais."
                ]
            }
        ]
    },
