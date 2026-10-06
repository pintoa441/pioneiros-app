st.set_page_config(
    page_title="Caderno de Pista - Agrupamento 78",
    page_icon="⚜️",  # Ou podes usar o caminho da imagem "logo_78.jpg"
    layout="wide"
)
import streamlit as st
import pandas as pd
import json
import os
from datetime import date

# 1. Configuração da página
st.set_page_config(
    page_title="Pista de Progresso - Agrupamento 78",
    page_icon="⚜️",
    layout="wide"
)

# 2. Exibição do Logótipo
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

# 3. Passwords e Base de Dados
PASSWORD_DIRIGENTE = "escuteiros78"
PASSWORD_GUIAS = "guias78"
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

# 4. Estrutura de Trilhos
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
# 5. Navegação principal
st.sidebar.title("⚜️ Navegação")
modo = st.sidebar.radio("Selecione a Área:", [
    "Área do Pioneiro", 
    "Área do Conselho de Guias", 
    "Área da Chefia / Dirigente"
])

registos = load_data()

# ---------------------------------------------------------
# MODO 1: ÁREA DO PIONEIRO
# ---------------------------------------------------------
if modo == "Área do Pioneiro":
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
                
            st.markdown("##### 🚩 Submeter Oportunidades Concluídas")
            
            novos_submetidos = []
            for i, op in enumerate(trilho["oportunidades"]):
                # Verificar se já foi aprovado pelo Conselho de Guias
                ja_aprovado = any(
                    r['nome'] == nome_pioneiro and 
                    r['trilho'] == trilho['nome'] and 
                    r['oportunidade'] == op and 
                    r.get('validado_cg', False)
                    for r in registos
                )
                
                col_check, col_data = st.columns([3, 1])
                with col_check:
                    if ja_aprovado:
                        st.success(f"✅ **{op}** (Validado pelo Conselho de Guias)")
                    else:
                        fazer_pedido = st.checkbox(op, key=f"{trilho['id']}_op_{i}")
                with col_data:
                    if not ja_aprovado and fazer_pedido:
                        dt_pioneiro = st.date_input("Data de Conclusão:", value=date.today(), key=f"dt_p_{trilho['id']}_{i}")
                        novos_submetidos.append({"op": op, "data_pioneiro": str(dt_pioneiro)})

            if st.button(f"📩 Submeter para o Conselho de Guias - {trilho['nome']}", key=f"btn_{trilho['id']}"):
                # Mantém os registos de outros pioneiros ou de outros trilhos
                novos_registos = [r for r in registos if not (r['nome'] == nome_pioneiro and r['trilho'] == trilho['nome'] and not r.get('validado_cg', False))]
                
                for item in novos_submetidos:
                    novos_registos.append({
                        "equipa": equipa,
                        "nome": nome_pioneiro,
                        "etapa": etapa_atual,
                        "area": area_atual["area"],
                        "trilho": trilho["nome"],
                        "oportunidade": item["op"],
                        "data_pioneiro": item["data_pioneiro"],
                        "validado_cg": False,
                        "data_cg": "-"
                    })
                save_data(novos_registos)
                st.success("Enviado para validação do Conselho de Guias!")

# ---------------------------------------------------------
# MODO 2: ÁREA DO CONSELHO DE GUIAS
# ---------------------------------------------------------
elif modo == "Área do Conselho de Guias":
    st.subheader("⚜️ Área do Conselho de Guias")
    st.write("Validação de progresso das Equipas da Comunidade 78.")
    
    pwd_guias = st.text_input("Palavra-passe do Conselho de Guias:", type="password")
    
    if pwd_guias == PASSWORD_GUIAS:
        st.success("Acesso autorizado ao Conselho de Guias!")
        
        pendentes = [r for r in registos if not r.get("validado_cg", False)]
        
        if pendentes:
            st.markdown("### 📋 Pedidos de Validação Pendentes")
            
            for idx, r in enumerate(pendentes):
                with st.expander(f"📌 {r['nome']} ({r['equipa']}) - {r['trilho']} | {r['oportunidade']}"):
                    st.write(f"**Área:** {r['area']}")
                    st.write(f"**Etapa:** {r['etapa']}")
                    st.write(f"**Data em que o Pioneiro concluiu:** {r.get('data_pioneiro', 'N/A')}")
                    
                    data_val_cg = st.date_input("Data de Validação pelo CG:", value=date.today(), key=f"val_dt_{idx}")
                    
                    if st.button("✅ Validar e Aprovar Trilho", key=f"btn_val_{idx}"):
                        for reg in registos:
                            if reg == r:
                                reg['validado_cg'] = True
                                reg['data_cg'] = str(data_val_cg)
                        save_data(registos)
                        st.success(f"Validação gravada com sucesso para {r['nome']}!")
                        st.rerun()
        else:
            st.info("Não existem pedidos de validação pendentes de momento.")
            
    elif pwd_guias:
        st.error("Palavra-passe do Conselho de Guias incorreta.")

# ---------------------------------------------------------
# MODO 3: ÁREA DA CHEFIA / DIRIGENTE
# ---------------------------------------------------------
else:
    st.subheader("🛡️️ Área do Dirigente / Chefia")
    
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
        df = pd.DataFrame(registos)
        
        if not df.empty:
            st.markdown("### 📊 Registos Globais da Comunidade")
            st.dataframe(df, use_container_width=True)
            
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Descarregar Relatório Completo (CSV)",
                data=csv,
                file_name="progresso_comunidade_pioneiros.csv",
                mime="text/csv"
            )
        else:
            st.info("Ainda não existem registos no sistema.")
