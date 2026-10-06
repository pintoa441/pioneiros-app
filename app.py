import streamlit as st
import pandas as pd
import os
from datetime import date

# 1. Configuração da página
st.set_page_config(
    page_title="Pista de Progresso - Agrupamento 78",
    page_icon="⚜️",
    layout="wide"
)

# 2. Inicialização do Estado da Sessão
if "perfil" not in st.session_state:
    st.session_state["perfil"] = "Inicio"

if "pioneiro_nome" not in st.session_state:
    st.session_state["pioneiro_nome"] = ""

if "pioneiro_equipa" not in st.session_state:
    st.session_state["pioneiro_equipa"] = ""

if "pioneiro_etapa" not in st.session_state:
    st.session_state["pioneiro_etapa"] = "Adesão"

if "area_selecionada" not in st.session_state:
    st.session_state["area_selecionada"] = None

if "validacoes" not in st.session_state:
    st.session_state["validacoes"] = pd.DataFrame(columns=[
        "ID", "Equipa", "Pioneiro", "Etapa", "Área", "Trilho", "Oportunidade",
        "Data_Pioneiro", "Estado_Guia", "Data_Guia", "Obs_Guia",
        "Estado_Dirigente", "Data_Dirigente", "Obs_Dirigente"
    ])

# Passwords de Acesso
PASSWORD_DIRIGENTE = "escuteiros78"
PASSWORD_GUIAS = "guias78"

# 3. Logótipo e Sidebar
if os.path.exists("logo_78.jpg"):
    st.sidebar.image("logo_78.jpg", use_container_width=True)

st.sidebar.title("⚜️ Agrupamento 78")

if st.session_state["perfil"] != "Inicio":
    if st.sidebar.button("🏠 Voltar ao Ecrã Inicial"):
        st.session_state["perfil"] = "Inicio"
        st.session_state["area_selecionada"] = None
        st.rerun()

# 4. Estrutura Completa das 6 Áreas de Desenvolvimento
TRILHOS_DATA = [
    {
        "area": "Desenvolvimento Físico",
        "icone": "🏃‍♂️",
        "descricao": "Desempenho físico, autoconhecimento e bem-estar corporal.",
        "trilhos": [
            {
                "id": "desempenho",
                "nome": "Desempenho",
                "descricao": "Ter preocupação com o desempenho físico e praticar atividades equilibradas.",
                "objetivos": ["F1 - Tenho preocupação com o meu desempenho físico."],
                "oportunidades": [
                    "Programar e executar um raid para a Equipa/Comunidade.",
                    "Promover uma palestra sobre atividade desportiva, saúde e bem-estar.",
                    "Criar um plano de treino pessoal e praticar atividade física regular.",
                    "Organizar um torneio de provas desportivas."
                ]
            },
            {
                "id": "autoconhecimento",
                "nome": "Autoconhecimento",
                "descricao": "Aceitar-se como é, reconhecendo e respeitando as diferenças físicas.",
                "objetivos": ["F2 - Aceito-me como sou e respeito as diferenças físicas."],
                "oportunidades": [
                    "Arranjar soluções na vida diária para inclusão de pessoas com deficiência.",
                    "Promover um debate sobre prevenção do bullying.",
                    "Fazer uma análise SWOT pessoal de pontos fortes e limitações."
                ]
            },
            {
                "id": "bem_estar",
                "nome": "Bem-Estar Físico",
                "descricao": "Reger-se por um estilo de vida saudável, cuidando da alimentação e repouso.",
                "objetivos": ["F4 - Rejo-me por um estilo de vida saudável."],
                "oportunidades": [
                    "Planear as refeições de um fim de semana de atividade.",
                    "Elaborar um manual de boas práticas de alimentação em campo.",
                    "Promover workshops sobre higiene corporal e saúde oral."
                ]
            }
        ]
    },
    {
        "area": "Desenvolvimento Afetivo",
        "icone": "❤️",
        "descricao": "Relacionamentos, sensibilidade e equilíbrio emocional.",
        "trilhos": [
            {
                "id": "relacionamento",
                "nome": "Relacionamento e Sensibilidade",
                "descricao": "Respeitar os outros nas várias relações e encarar a família como pilar.",
                "objetivos": ["A1 - Reconheço o valor das minhas relações afetivas."],
                "oportunidades": [
                    "Promover discussões sobre prevenção de violência no namoro.",
                    "Manter um diário de vivências e sentimentos.",
                    "Planear um momento de convívio aberto à família e amigos."
                ]
            },
            {
                "id": "equilibrio",
                "nome": "Equilíbrio Emocional",
                "descricao": "Agir de forma ponderada, sabendo gerir os sentimentos.",
                "objetivos": ["A4 - Ajo de forma ponderada e respeito o sentimento dos outros."],
                "oportunidades": [
                    "Escrever um diário de emoções e refletir sobre como atuou.",
                    "Organizar um debate na Equipa sobre opiniões divergentes."
                ]
            }
        ]
    },
    {
        "area
