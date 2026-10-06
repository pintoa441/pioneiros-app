import streamlit as st
import pandas as pd
import json
import os

# 1. Configuração da página
st.set_page_config(
    page_title="Pista de Progresso - III Secção",
    page_icon="⚜️",
    layout="wide"
)

DB_FILE = "dados_pioneiros.json"

# Função para carregar dados do ficheiro JSON local
def load_data():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

# Função para guardar dados no ficheiro JSON local
def save_data(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# 2. Base de Dados dos 18 Trilhos de Progresso
TRILHOS_DATA = [
    {
        "area": "Desenvolvimento Físico",
        "trilhos": [
            {
                "id": "desempenho",
                "nome": "Desempenho",
                "descricao": "Ter preocupação com o desempenho físico e praticar atividades que contribuem para um desenvolvimento equilibrado.",
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

# 3. Interface Principal
st.title("⚜️ Caderno de Pista Digital - III Secção")

# Sidebar - Dados do Pioneiro
st.sidebar.header("👤 Perfil do Escuteiro")
equipa = st.sidebar.text_input("Equipa", "Equipa Condor")
nome_pioneiro = st.sidebar.text_input("Nome", "Escuteiro")
etapa_atual = st.sidebar.selectbox("Etapa Atual", ["Adesão", "Conhecimento", "Desafio", "Partida"])

st.sidebar.markdown("---")

area_nomes = [a["area"] for a in TRILHOS_DATA]
area_selecionada = st.sidebar.selectbox("🎯 Seleciona a Área", area_nomes)

area_atual = next(a for a in TRILHOS_DATA if a["area"] == area_selecionada)

# Painel Central
st.header(f"Área: {area_atual['area']}")

trilho_nomes = [t["nome"] for t in area_atual["trilhos"]]
tabs = st.tabs(trilho_nomes)

registos = load_data()

for idx, tab in enumerate(tabs):
    trilho = area_atual["trilhos"][idx]
    with tab:
        st.subheader(f"Trilho: {trilho['nome']}")
        st.write(f"*{trilho['descricao']}*")
        
        st.markdown("##### 🎯 Objetivos de Progresso")
        for obj in trilho["objetivos"]:
            st.info(obj)
            
        st.markdown("##### 🚩 Oportunidades Educativas")
        concluidas = 0
        total = len(trilho["oportunidades"])
        
        op_selecionadas = []
        for i, op in enumerate(trilho["oportunidades"]):
            key = f"{trilho['id']}_op_{i}"
            if st.checkbox(op, key=key):
                concluidas += 1
                op_selecionadas.append(op)
                
        progresso = concluidas / total if total > 0 else 0
        st.progress(progresso)
        st.caption(f"Concluídas: {concluidas}/{total} ({int(progresso * 100)}%)")
        
        if st.button(f"💾 Guardar Progresso - {trilho['nome']}", key=f"btn_{trilho['id']}"):
            novos_registos = [r for r in registos if not (r['nome'] == nome_pioneiro and r['trilho'] == trilho['nome'])]
            for op in op_selecionadas:
                novos_registos.append({
                    "equipa": equipa,
                    "nome": nome_pioneiro,
                    "etapa": etapa_atual,
                    "area": area_atual["area"],
                    "trilho": trilho["nome"],
                    "oportunidade": op
                })
            save_data(novos_registos)
            st.success("Progresso atualizado com sucesso!")

# 4. Dashboard de Visualização e Cópia de Segurança
st.markdown("---")
st.header("📊 Painel Geral de Progresso")

registos_atuais = load_data()
df = pd.DataFrame(registos_atuais)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Registos Efetuados")
    if not df.empty:
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Ainda não existem registos guardados.")

with col2:
    st.subheader("💾 Cópia de Segurança (Backup)")
    st.write("Guarda uma cópia dos teus dados no telemóvel/PC para nunca perderes o progresso!")
    
    if not df.empty:
        json_string = json.dumps(registos_atuais, ensure_ascii=False, indent=4)
        st.download_button(
            label="📥 Descarregar Backup (JSON)",
            data=json_string,
            file_name=f"progresso_{nome_pioneiro.replace(' ', '_')}.json",
            mime="application/json"
        )

    # Carregar Backup
    uploaded_file = st.file_uploader("📤 Restaurar Backup (JSON)", type=["json"])
    if uploaded_file is not None:
        try:
            dados_carregados = json.load(uploaded_file)
            save_data(dados_carregados)
            st.success("Backup restaurado com sucesso! Recarrega a página.")
        except Exception:
            st.error("Ficheiro de backup inválido.")
