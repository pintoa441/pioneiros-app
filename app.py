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

# 2. Inicialização do Estado da Sessão (Perfil e Tabela de Validações)
if "perfil" not in st.session_state:
    st.session_state["perfil"] = "Inicio"

if "validacoes" not in st.session_state:
    # Estrutura de dados simulada para o fluxo de validação
    st.session_state["validacoes"] = pd.DataFrame(columns=[
        "ID", "Equipa", "Pioneiro", "Área", "Trilho", "Oportunidade",
        "Data_Pioneiro", "Estado_Guia", "Data_Guia", "Obs_Guia",
        "Estado_Dirigente", "Data_Dirigente", "Obs_Dirigente"
    ])

# Passwords de Acesso
PASSWORD_DIRIGENTE = "escuteiros78"
PASSWORD_GUIAS = "guias78"

# 3. Exibição do Logótipo e Título na Barra Lateral
if os.path.exists("logo_78.jpg"):
    st.sidebar.image("logo_78.jpg", use_container_width=True)

st.sidebar.title("⚜️ Agrupamento 78")

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
    st.subheader("Selecciona o teu perfil de acesso:")
    st.write(" ")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("### 🏕️ 1. Pioneiro\n\nSubmete as tuas Oportunidades concluídas e regista a tua data de validação pessoal.")
        if st.button("Entrar como Pioneiro ➔", use_container_width=True):
            st.session_state["perfil"] = "Pioneiro"
            st.rerun()

    with col2:
        st.warning("### ⚜️ 2. Conselho de Guias\n\nAvalia, comenta e valida as propostas submetidas pelos Pioneiros da Comunidade.")
        if st.button("Entrar como Guia ➔", use_container_width=True):
            st.session_state["perfil"] = "Guia"
            st.rerun()

    with col3:
        st.success("### 🛡️ 3. Chefia / Dirigente\n\nHomologação final, atribuição de Etapas e histórico global de progresso.")
        if st.button("Entrar como Dirigente ➔", use_container_width=True):
            st.session_state["perfil"] = "Dirigente"
            st.rerun()

# =========================================================
# 🏕️ ETAPA 1: ÁREA DO PIONEIRO (Submissão)
# =========================================================
elif st.session_state["perfil"] == "Pioneiro":
    st.title("🏕️ Área do Pioneiro - Submissão de Proposta")
    
    st.sidebar.markdown("---")
    st.sidebar.header("👤 Identificação")
    equipa = st.sidebar.text_input("Equipa", "Equipa Condor")
    nome_pioneiro = st.sidebar.text_input("Nome do Pioneiro", "Afonso Pinto")
    etapa_atual = st.sidebar.selectbox("Etapa Atual", ["Adesão", "Conhecimento", "Desafio", "Partida"])

    st.sidebar.markdown("---")
    area_nomes = [a["area"] for a in TRILHOS_DATA]
    area_selecionada = st.sidebar.selectbox("🎯 Área de Desenvolvimento", area_nomes)

    area_atual = next(a for a in TRILHOS_DATA if a["area"] == area_selecionada)

    st.header(f"Área: {area_atual['area']}")

    trilho_nomes = [t["nome"] for t in area_atual["trilhos"]]
    tabs = st.tabs(trilho_nomes)

    for idx, tab in enumerate(tabs):
        trilho = area_atual["trilhos"][idx]
        with tab:
            st.subheader(f"Trilho: {trilho['nome']}")
            st.write(f"*{trilho['descricao']}*")
            
            st.markdown("##### 🎯 Objetivos do Trilho")
            for obj in trilho["objetivos"]:
                st.info(obj)
                
            st.markdown("##### 🚩 Oportunidades Educativas")
            
            with st.form(key=f"form_pioneiro_{trilho['id']}"):
                op_selecionada = st.selectbox("Escolhe a oportunidade que realizaste:", trilho["oportunidades"])
                data_pioneiro = st.date_input("Data de Conclusão / Validação Pessoal", date.today())
                btn_submeter = st.form_submit_button("📩 Submeter para Validação do Conselho de Guias")
                
                if btn_submeter:
                    novo_id = len(st.session_state["validacoes"]) + 1
                    nova_linha = {
                        "ID": novo_id,
                        "Equipa": equipa,
                        "Pioneiro": nome_pioneiro,
                        "Área": area_selecionada,
                        "Trilho": trilho["nome"],
                        "Oportunidade": op_selecionada,
                        "Data_Pioneiro": str(data_pioneiro),
                        "Estado_Guia": "Pendente",
                        "Data_Guia": "-",
                        "Obs_Guia": "-",
                        "Estado_Dirigente": "Pendente",
                        "Data_Dirigente": "-",
                        "Obs_Dirigente": "-"
                    }
                    st.session_state["validacoes"] = pd.concat([st.session_state["validacoes"], pd.DataFrame([nova_linha])], ignore_index=True)
                    st.success(" Proposta submetida com sucesso ao Conselho de Guias!")

# =========================================================
# ⚜️ ETAPA 2: ÁREA DO CONSELHO DE GUIAS (Validação Intermédia)
# =========================================================
elif st.session_state["perfil"] == "Guia":
    st.title("⚜️ Área do Conselho de Guias")
    
    pwd_guias = st.text_input("Palavra-passe do Conselho de Guias:", type="password")
    
    if pwd_guias == PASSWORD_GUIAS:
        st.success("Acesso Autorizado!")
        st.markdown("### 📋 Propostas Pendentes de Validação")
        
        df = st.session_state["validacoes"]
        pendentes = df[df["Estado_Guia"] == "Pendente"]
        
        if pendentes.empty:
            st.info("Não existem propostas pendentes para o Conselho de Guias.")
        else:
            for idx, row in pendentes.iterrows():
                with st.expander(f"📌 [{row['Equipa']}] {row['Pioneiro']} - {row['Trilho']}"):
                    st.write(f"**Área:** {row['Área']}")
                    st.write(f"**Oportunidade:** {row['Oportunidade']}")
                    st.write(f"**Data Submissão pelo Pioneiro:** {row['Data_Pioneiro']}")
                    
                    col_g1, col_g2 = st.columns(2)
                    with col_g1:
                        decisao_guia = st.radio(f"Decisão do Conselho ({row['ID']}):", ["Aprovado", "Rejeitado"], key=f"dec_g_{row['ID']}")
                    with col_g2:
                        data_g = st.date_input(f"Data Validação Guia ({row['ID']}):", date.today(), key=f"dt_g_{row['ID']}")
                        obs_g = st.text_input(f"Comentários/Observações ({row['ID']}):", key=f"obs_g_{row['ID']}")
                    
                    if st.button(f"Guardar Validação #{row['ID']}", key=f"btn_g_{row['ID']}"):
                        st.session_state["validacoes"].loc[st.session_state["validacoes"]["ID"] == row["ID"], "Estado_Guia"] = decisao_guia
                        st.session_state["validacoes"].loc[st.session_state["validacoes"]["ID"] == row["ID"], "Data_Guia"] = str(data_g)
                        st.session_state["validacoes"].loc[st.session_state["validacoes"]["ID"] == row["ID"], "Obs_Guia"] = obs_g
                        st.success("Validação do Conselho de Guias registada!")
                        st.rerun()

# =========================================================
# 🛡️ ETAPA 3: ÁREA DA CHEFIA / DIRIGENTE (Validação Final)
# =========================================================
elif st.session_state["perfil"] == "Dirigente":
    st.title("🛡️ Área da Chefia / Dirigente")
    
    with st.form(key="login_form"):
        pwd_input = st.text_input("Palavra-passe de Acesso:", type="password")
        submit_button = st.form_submit_button(label="Entrar")
    
    if submit_button or st.session_state.get("autenticado", False):
        if pwd_input == PASSWORD_DIRIGENTE or st.session_state.get("autenticado", False):
            st.session_state["autenticado"] = True
            
            st.markdown("### 🏛️ Validação Final & Homologação")
            df = st.session_state["validacoes"]
            pendentes_dir = df[(df["Estado_Guia"] == "Aprovado") & (df["Estado_Dirigente"] == "Pendente")]
            
            if pendentes_dir.empty:
                st.info("Não existem propostas validadas pelo Conselho de Guias a aguardar homologação da Chefia.")
            else:
                for idx, row in pendentes_dir.iterrows():
                    with st.expander(f"⚜️ Homologação: {row['Pioneiro']} ({row['Equipa']}) - {row['Trilho']}"):
                        st.write(f"**Oportunidade:** {row['Oportunidade']}")
                        st.write(f"📅 **Data Pioneiro:** {row['Data_Pioneiro']} | 📅 **Data Guia:** {row['Data_Guia']}")
                        st.write(f"💬 **Obs. Guia:** {row['Obs_Guia']}")
                        
                        col_d1, col_d2 = st.columns(2)
                        with col_d1:
                            decisao_d = st.radio(f"Homologação Final ({row['ID']}):", ["Validado", "Necessita Revisão"], key=f"dec_d_{row['ID']}")
                        with col_d2:
                            data_d = st.date_input(f"Data Validação Dirigente ({row['ID']}):", date.today(), key=f"dt_d_{row['ID']}")
                            obs_d = st.text_input(f"Observações da Chefia ({row['ID']}):", key=f"obs_d_{row['ID']}")
                        
                        if st.button(f"Homologar Oportunidade #{row['ID']}", key=f"btn_d_{row['ID']}"):
                            st.session_state["validacoes"].loc[st.session_state["validacoes"]["ID"] == row["ID"], "Estado_Dirigente"] = decisao_d
                            st.session_state["validacoes"].loc[st.session_state["validacoes"]["ID"] == row["ID"], "Data_Dirigente"] = str(data_d)
                            st.session_state["validacoes"].loc[st.session_state["validacoes"]["ID"] == row["ID"], "Obs_Dirigente"] = obs_d
                            st.success("Homologação registada com sucesso!")
                            st.rerun()
            
            st.markdown("---")
            st.markdown("### 📊 Histórico Global de Validações da Comunidade")
            st.dataframe(st.session_state["validacoes"], use_container_width=True)
        else:
            st.error("Palavra-passe incorreta.")
