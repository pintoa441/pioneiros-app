import streamlit as st
import pandas as pd
import os
from datetime import date

# 1. Configuração da página (DEVE SER O PRIMEIRO COMANDO STREAMLIT)
st.set_page_config(
    page_title="Pista de Progresso - Agrupamento 78",
    page_icon="⚜️",
    layout="wide"
)

# 2. Inicialização do Estado da Sessão (Perfil selecionado)
if "perfil" not in st.session_state:
    st.session_state["perfil"] = "Inicio"

# Passwords de Acesso
PASSWORD_DIRIGENTE = "escuteiros78"
PASSWORD_GUIAS = "guias78"

# 3. Exibição do Logótipo e Título na Barra Lateral
if os.path.exists("logo_78.jpg"):
    st.sidebar.image("logo_78.jpg", use_container_width=True)

st.sidebar.title("⚜️ Agrupamento 78")

# Botão na barra lateral para voltar ao início se já estiver num perfil
if st.session_state["perfil"] != "Inicio":
    if st.sidebar.button("🏠 Voltar ao Ecrã Inicial"):
        st.session_state["perfil"] = "Inicio"
        st.rerun()

# 4. Estrutura dos Trilhos e Objetivos
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
        "area": "Desenvolvimento do Carácter",
        "trilhos": [
            {
                "id": "autonomia",
                "nome": "Autonomia",
                "descricao": "Saber fazer opções coerentes com uma matriz de valores.",
                "objetivos": ["C1 - Sou capaz de fazer opções de acordo com os meus valores."],
                "oportunidades": [
                    "Participar ativamente nas escolhas do Empreendimento.",
                    "Traçar um plano concreto para alcançar um objetivo de progresso."
                ]
            },
            {
                "id": "responsabilidade",
                "nome": "Responsabilidade",
                "descricao": "Demonstrar empenho nas tarefas e cumprir compromissos.",
                "objetivos": ["C3 - Reconheço a importância das tarefas atribuídas."],
                "oportunidades": [
                    "Assumir tarefas de preparação de um Empreendimento.",
                    "Exercer a função de Guia/Sub-guia com responsabilidade."
                ]
            }
        ]
    },
    {
        "area": "Desenvolvimento Espiritual",
        "trilhos": [
            {
                "id": "descoberta",
                "nome": "Descoberta",
                "descricao": "Conhecer a revelação de Deus e viver a fé na comunidade.",
                "objetivos": ["E1 - Conheço e compreendo a vida dos principais profetas."],
                "oportunidades": [
                    "Organizar um raid sob um tema ou imaginário bíblico.",
                    "Ajudar na dinamização dos tempos litúrgicos de Advento ou Quaresma."
                ]
            }
        ]
    },
    {
        "area": "Desenvolvimento Intelectual",
        "trilhos": [
            {
                "id": "procura_conhecimento",
                "nome": "Procura do Conhecimento",
                "descricao": "Aumentar os conhecimentos utilizando ferramentas de informação.",
                "objetivos": ["I1 - Procuro sempre aumentar os meus conhecimentos."],
                "oportunidades": [
                    "Dinamizar um workshop técnico para ensinar competências.",
                    "Criar uma ferramenta digital de apoio ao Empreendimento."
                ]
            }
        ]
    },
    {
        "area": "Desenvolvimento Social",
        "trilhos": [
            {
                "id": "cidadania",
                "nome": "Exercer Ativamente Cidadania",
                "descricao": "Conhecer deveres e direitos e intervir em projetos comunitários.",
                "objetivos": ["S1 - Promovo o conhecimento dos deveres e direitos."],
                "oportunidades": [
                    "Participar na Associação de Estudantes ou Orçamento Participativo.",
                    "Realizar trabalho de voluntariado numa instituição local."
                ]
            }
        ]
    }
]

# =========================================================
# 🏠 ECRÃ INICIAL / SELEÇÃO DE PERFIL
# =========================================================
if st.session_state["perfil"] == "Inicio":
    col_l, col_t = st.columns([1, 4])
    with col_l:
        if os.path.exists("logo_78.jpg"):
            st.image("logo_78.jpg", width=110)
    with col_t:
        st.title("⚜️ Caderno de Pista Digital")
        st.caption("Agrupamento 78 Arruda dos Vinhos - III Secção (Pioneiros)")

    st.markdown("---")
    st.subheader("Bem-vindo! Seleciona o teu perfil para continuar:")
    st.write(" ")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("### 🏕️ Pioneiro\n\nConsulta a tua Pista de Progresso, descobre os Trilhos e regista as Oportunidades Concluídas.")
        if st.button("Entrar como Pioneiro ➔", use_container_width=True):
            st.session_state["perfil"] = "Pioneiro"
            st.rerun()

    with col2:
        st.warning("### ⚜️ Guia / Conselho de Guias\n\nAcompanha o progresso das Equipas da Comunidade e valida as Oportunidades submetidas.")
        if st.button("Entrar como Guia ➔", use_container_width=True):
            st.session_state["perfil"] = "Guia"
            st.rerun()

    with col3:
        st.success("### 🛡️ Dirigente / Chefia\n\nPainel de controlo geral da III Secção para acompanhamento e gestão das Etapas.")
        if st.button("Entrar como Dirigente ➔", use_container_width=True):
            st.session_state["perfil"] = "Dirigente"
            st.rerun()

# =========================================================
# 🏕️ MODO 1: ÁREA DO PIONEIRO
# =========================================================
elif st.session_state["perfil"] == "Pioneiro":
    st.title("🏕️ Área do Pioneiro")
    
    st.sidebar.markdown("---")
    st.sidebar.header("👤 Perfil do Escuteiro")
    equipa = st.sidebar.text_input("Equipa", "Equipa Condor")
    nome_pioneiro = st.sidebar.text_input("Nome", "Escuteiro")
    etapa_atual = st.sidebar.selectbox("Etapa Atual", ["Adesão", "Conhecimento", "Desafio", "Partida"])

    st.sidebar.markdown("---")
    area_nomes = [a["area"] for a in TRILHOS_DATA]
    area_selecionada = st.sidebar.selectbox("🎯 Seleciona a Área", area_nomes)

    area_atual = next(a for a in TRILHOS_DATA if a["area"] == area_selecionada)

    st.header(f"Área: {area_atual['area']}")

    trilho_nomes = [t["nome"] for t in area_atual["trilhos"]]
    tabs = st.tabs(trilho_nomes)

    for idx, tab in enumerate(tabs):
        trilho = area_atual["trilhos"][idx]
        with tab:
            st.subheader(f"Trilho: {trilho['nome']}")
            st.write(f"*{trilho['descricao']}*")
            
            st.markdown("##### 🎯 Objetivos de Progresso")
            for obj in trilho["objetivos"]:
                st.info(obj)
                
            st.markdown("##### 🚩 Oportunidades Educativas")
            for op in trilho["oportunidades"]:
                st.checkbox(op, key=f"{trilho['id']}_op_{op}")

# =========================================================
# ⚜️ MODO 2: ÁREA DO GUIA / CONSELHO DE GUIAS
# =========================================================
elif st.session_state["perfil"] == "Guia":
    st.title("⚜️ Área do Guia / Conselho de Guias")
    st.write("Validação e acompanhamento do progresso da Comunidade 78.")
    
    pwd_guias = st.text_input("Palavra-passe do Conselho de Guias:", type="password")
    
    if pwd_guias == PASSWORD_GUIAS:
        st.success("Acesso autorizado ao Conselho de Guias!")
        st.info("Aqui serão apresentadas as validações de progresso das Equipas.")
    elif pwd_guias:
        st.error("Palavra-passe do Conselho de Guias incorreta.")

# =========================================================
# 🛡️ MODO 3: ÁREA DO DIRIGENTE / CHEFIA
# =========================================================
elif st.session_state["perfil"] == "Dirigente":
    st.title("🛡️ Área do Dirigente / Chefia")
    
    with st.form(key="login_form"):
        pwd_input = st.text_input("Palavra-passe de Acesso:", type="password")
        submit_button = st.form_submit_button(label="Entrar")
    
    if submit_button:
        if pwd_input == PASSWORD_DIRIGENTE:
            st.session_state["autenticado"] = True
            st.success("Acesso autorizado!")
        else:
            st.session_state["autenticado"] = False
            st.error("Palavra-passe incorreta.")

    if st.session_state.get("autenticado", False):
        st.markdown("### 📊 Visão Geral da Comunidade 78")
        st.write("Painel de controlo da Chefia para acompanhamento das Etapas de Progresso.")
