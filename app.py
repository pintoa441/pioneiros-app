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

# 2. Inicialização do Estado da Sessão (Perfis, Utilizadores e Validações)
if "perfil" not in st.session_state:
    st.session_state["perfil"] = "Inicio"

if "pioneiro_ativo" not in st.session_state:
    st.session_state["pioneiro_ativo"] = None  # Guarda o perfil do pioneiro autenticado

# Tabela simulada de Pioneiros registados (Nome, Equipa, Etapa, PIN)
if "utilizadores_pioneiros" not in st.session_state:
    st.session_state["utilizadores_pioneiros"] = pd.DataFrame(columns=[
        "Nome", "Equipa", "Etapa", "PIN"
    ])

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
        st.session_state["pioneiro_ativo"] = None
        st.session_state["area_selecionada"] = None
        st.rerun()

# 4. Estrutura Completa das 6 Áreas de Desenvolvimento
TRILHOS_DATA = [
    {
        "area": "Desenvolvimento Físico",
        "icone": "🏃‍♂️️",
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
            }
        ]
    },
    {
        "area": "Desenvolvimento do Carácter",
        "icone": "🧭",
        "descricao": "Autonomia, responsabilidade e matriz de valores.",
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
    },
    {
        "area": "Desenvolvimento Espiritual",
        "icone": "✝️",
        "descricao": "Descoberta da fé, vivência comunitária e espiritualidade.",
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
        "icone": "💡",
        "descricao": "Procura do conhecimento, resolução de problemas e criatividade.",
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
        "icone": "🤝",
        "descricao": "Cidadania ativa, serviço comunitário e trabalho em equipa.",
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
    st.subheader("Seleciona o teu perfil de acesso:")
    st.write(" ")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("### 🏕️ 1. Pioneiro\n\nAcede ao teu perfil pessoal com palavra-passe e gere os teus Trilhos.")
        if st.button("Entrar como Pioneiro ➔", use_container_width=True):
            st.session_state["perfil"] = "Pioneiro"
            st.rerun()

    with col2:
        st.warning("### ⚜️ 2. Conselho de Guias\n\nAvalia, comenta e valida as propostas submetidas pelas Equipas.")
        if st.button("Entrar como Guia ➔", use_container_width=True):
            st.session_state["perfil"] = "Guia"
            st.rerun()

    with col3:
        st.success("### 🛡️ 3. Chefia / Dirigente\n\nHomologação final, atribuição de Etapas e histórico global de progresso.")
        if st.button("Entrar como Dirigente ➔", use_container_width=True):
            st.session_state["perfil"] = "Dirigente"
            st.rerun()

# =========================================================
# 🏕️ ÁREA DO PIONEIRO (Com Autenticação Individual)
# =========================================================
elif st.session_state["perfil"] == "Pioneiro":
    st.title("🏕️ Área Privada do Pioneiro")

    df_pioneiros = st.session_state["utilizadores_pioneiros"]

    # PASSAGEM 1: Login ou Registo de Novo Pioneiro
    if st.session_state["pioneiro_ativo"] is None:
        tab_login, tab_registo = st.tabs(["🔑 Aceder ao Meu Caderno", "📝 Criar Novo Perfil"])

        # Separador 1: Entrar com PIN
        with tab_login:
            st.subheader("Entrar no meu Caderno de Pista")
            if df_pioneiros.empty:
                st.info("Ainda não existem Pioneiros registados. Cria o teu perfil no separador ao lado!")
            else:
                lista_pioneiros = df_pioneiros["Nome"].tolist()
                pioneiro_selecionado = st.selectbox("Escolhe o teu Nome:", lista_pioneiros)
                pin_input = st.text_input("Palavra-passe / PIN pessoal:", type="password", key="login_pin")
                
                if st.button("Desbloquear Caderno 🔓"):
                    user_row = df_pioneiros[df_pioneiros["Nome"] == pioneiro_selecionado].iloc[0]
                    if str(pin_input) == str(user_row["PIN"]):
                        st.session_state["pioneiro_ativo"] = user_row.to_dict()
                        st.success(f"Bem-vindo, {user_row['Nome']}!")
                        st.rerun()
                    else:
                        st.error("PIN / Palavra-passe incorreta.")

        # Separador 2: Registar Novo Perfil
        with tab_registo:
            st.subheader("Registar Novo Pioneiro")
            with st.form(key="form_novo_pioneiro"):
                novo_nome = st.text_input("Nome Completo:")
                nova_equipa = st.text_input("Equipa (ex: Equipa Condor):")
                nova_etapa = st.selectbox("Etapa Atual:", ["Adesão", "Conhecimento", "Desafio", "Partida"])
                novo_pin = st.text_input("Cria a tua Palavra-passe / PIN (ex: 1234):", type="password")
                
                btn_registo = st.form_submit_button("Criar o meu Caderno 🚀")
                
                if btn_registo:
                    if novo_nome.strip() and nova_equipa.strip() and novo_pin.strip():
                        if novo_nome.strip() in df_pioneiros["Nome"].values:
                            st.error("Já existe um Pioneiro registado com esse nome!")
                        else:
                            novo_utilizador = {
                                "Nome": novo_nome.strip(),
                                "Equipa": nova_equipa.strip(),
                                "Etapa": nova_etapa,
                                "PIN": str(novo_pin.strip())
                            }
                            st.session_state["utilizadores_pioneiros"] = pd.concat([
                                st.session_state["utilizadores_pioneiros"], 
                                pd.DataFrame([novo_utilizador])
                            ], ignore_index=True)
                            
                            st.session_state["pioneiro_ativo"] = novo_utilizador
                            st.success("Perfil criado com sucesso!")
                            st.rerun()
                    else:
                        st.error("Por favor, preenche todos os campos para criar o perfil.")

    # PASSAGEM 2: Vista das Áreas para o Pioneiro Autenticado
    else:
        p_ativo = st.session_state["pioneiro_ativo"]

        # Cabeçalho do perfil autenticado
        col_inf1, col_inf2, col_inf3, col_btn = st.columns([2, 2, 2, 1])
        with col_inf1:
            st.markdown(f"👤 **Pioneiro:** {p_ativo['Nome']}")
        with col_inf2:
            st.markdown(f"🏕️ **Equipa:** {p_ativo['Equipa']}")
        with col_inf3:
            st.markdown(f"⚜️ **Etapa:** {p_ativo['Etapa']}")
        with col_btn:
            if st.button("🔒 Sair", help="Terminar sessão"):
                st.session_state["pioneiro_ativo"] = None
                st.session_state["area_selecionada"] = None
                st.rerun()

        st.markdown("---")

        # Seleção das Áreas de Desenvolvimento
        if st.session_state["area_selecionada"] is None:
            st.markdown("### 🎯 Escolhe a Área de Desenvolvimento:")
            st.write("Clica numa das caixas para veres os respetivos Trilhos e Oportunidades:")
            st.write(" ")

            grid_col1, grid_col2 = st.columns(2)

            for i, area_item in enumerate(TRILHOS_DATA):
                col_destino = grid_col1 if i % 2 == 0 else grid_col2
                with col_destino:
                    st.info(f"### {area_item['icone']} {area_item['area']}\n\n*{area_item['descricao']}*")
                    if st.button(f"Explorar {area_item['area']} ➔", key=f"btn_area_{i}", use_container_width=True):
                        st.session_state["area_selecionada"] = area_item["area"]
                        st.rerun()
                    st.write(" ")

        # Detalhe do Trilho e Submissão
        else:
            col_voltar, col_tit = st.columns([1, 4])
            with col_voltar:
                if st.button("⬅️ Outras Áreas"):
                    st.session_state["area_selecionada"] = None
                    st.rerun()
            with col_tit:
                st.header(f"Área: {st.session_state['area_selecionada']}")

            area_atual = next(a for a in TRILHOS_DATA if a["area"] == st.session_state["area_selecionada"])
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
                        
                    st.markdown("##### 🚩 Submeter Oportunidade Concluída")
                    
                    with st.form(key=f"form_pioneiro_{trilho['id']}"):
                        op_selecionada = st.selectbox("Escolhe a oportunidade que realizaste:", trilho["oportunidades"])
                        data_pioneiro = st.date_input("Data de Conclusão / Validação Pessoal:", date.today())
                        btn_submeter = st.form_submit_button("📩 Submeter para Validação do Conselho de Guias")
                        
                        if btn_submeter:
                            novo_id = len(st.session_state["validacoes"]) + 1
                            nova_linha = {
                                "ID": novo_id,
                                "Equipa": p_ativo["Equipa"],
                                "Pioneiro": p_ativo["Nome"],
                                "Etapa": p_ativo["Etapa"],
                                "Área": st.session_state["area_selecionada"],
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
                            st.success("Proposta submetida com sucesso ao Conselho de Guias!")

# =========================================================
# ⚜️ MODO 2: ÁREA DO CONSELHO DE GUIAS
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
# 🛡️ MODO 3: ÁREA DA CHEFIA / DIRIGENTE
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
            st.markdown("### 👥 Utilizadores Registados (Pioneiros)")
            st.dataframe(st.session_state["utilizadores_pioneiros"], use_container_width=True)

            st.markdown("### 📊 Histórico Global de Validações da Comunidade")
            st.dataframe(st.session_state["validacoes"], use_container_width=True)
        else:
            st.error("Palavra-passe incorreta.")
