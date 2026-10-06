import sqlite3
import pandas as pd
import streamlit as st

# 1. Configuração da página
st.set_page_config(
    page_title="Pista de Progresso - III Secção",
    page_icon="⚜️",
    layout="wide"
)

# 2. Inicialização da Base de Dados Local (SQLite)
def init_db():
    conn = sqlite3.connect("progresso_pioneiros.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS propostas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            equipa TEXT,
            nome TEXT,
            etapa TEXT,
            area TEXT,
            trilho TEXT,
            objetivo_codigo TEXT,
            oportunidade TEXT,
            data_registo TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db()

# 3. Base de Dados dos Trilhos de Progresso
TRILHOS_DATA = [
    {
        "area": "Desenvolvimento Físico",
        "trilhos": [
            {
                "id": "desempenho",
                "nome": "Desempenho",
                "descricao": "Ter preocupação com o desempenho físico e praticar atividades que contribuem para um desenvolvimento equilibrado.",
                "objetivos": ["F1 - Tenho preocupação com o meu desempenho físico. Pratico atividades que contribuem para o meu desenvolvimento equilibrado."],
                "oportunidades": [
                    "Programar e executar um raid para a Equipa/Comunidade com planeamento de esforço, descanso e alimentação.",
                    "Promover uma palestra sobre atividade desportiva, saúde e bem-estar.",
                    "Criar um plano de treino pessoal e praticar atividade física regular.",
                    "Organizar um torneio de provas desportivas.",
                    "Fazer uma avaliação das limitações físicas e organizar uma atividade para superar novos desafios.",
                    "Inscrever-se numa atividade nova fora da zona de conforto."
                ]
            },
            {
                "id": "autoconhecimento",
                "nome": "Autoconhecimento",
                "descricao": "Aceitar-se como é, reconhecendo e respeitando as diferenças físicas e o sexo oposto.",
                "objetivos": [
                    "F2 - Aceito-me como sou e respeito as diferenças físicas entre as pessoas.",
                    "F3 - Reconheço e respeito as diferenças entre homens e mulheres e as necessidades de cada um."
                ],
                "oportunidades": [
                    "Arranjar soluções na vida diária para inclusão de pessoas com deficiência.",
                    "Promover um debate, palestra ou campanha sobre prevenção do bullying ou discriminação.",
                    "Fazer uma análise SWOT pessoal de pontos fortes e limitações físicas.",
                    "Organizar a semana da mobilidade na escola ou Agrupamento.",
                    "Criar um guião de campo sobre como superar barreiras para escuteiros com mobilidade reduzida."
                ]
            },
            {
                "id": "bem_estar",
                "nome": "Bem-Estar Físico",
                "descricao": "Reger-se por um estilo de vida saudável, cuidando da apresentação, alimentação e repouso.",
                "objetivos": ["F4 - Rejo-me por um estilo de vida saudável, preocupando-me com a minha apresentação, alimentação e repouso."],
                "oportunidades": [
                    "Planear e assumir a responsabilidade pelas refeições de um fim de semana de atividade.",
                    "Elaborar um manual de boas práticas de alimentação saudável em campo.",
                    "Promover ações ou workshops sobre higiene corporal e saúde oral.",
                    "Organizar debates sobre prevenção de comportamentos de risco."
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
                "descricao": "Respeitar os outros nas várias relações e encarar a família como pilar de vida.",
                "objetivos": [
                    "A1 - Reconheço o valor das minhas relações afetivas e da minha sexualidade.",
                    "A2 - Reconheço o valor da família e comprometo-me com o bem-estar da mesma.",
                    "A3 - Demonstro maturidade perante os conflitos e reconheço diferentes sensibilidades."
                ],
                "oportunidades": [
                    "Promover discussões sobre prevenção de violência no namoro ou bullying.",
                    "Manter um diário de vivências e sentimentos.",
                    "Convidar a família para momentos marcantes da vida escutista.",
                    "Planear um momento de convívio aberto à família e amigos."
                ]
            },
            {
                "id": "equilibrio",
                "nome": "Equilíbrio Emocional",
                "descricao": "Agir de forma ponderada, sabendo gerir os sentimentos dos outros.",
                "objetivos": ["A4 - Ajo de forma ponderada, respeitando o sentimento dos outros e esforço-me por corrigir quando me excedo."],
                "oportunidades": [
                    "Escrever um diário de emoções do último mês e refletir sobre como atuou.",
                    "Organizar um debate na Equipa e avaliar como lidou com opiniões divergentes.",
                    "Criar uma dinâmica de dramatização para praticar a gestão de conflitos."
                ]
            },
            {
                "id": "autoestima",
                "nome": "Autoestima",
                "descricao": "Conhecer e aceitar a própria personalidade, esforçando-se para superar limitações.",
                "objetivos": [
                    "A5 - Reconheço as características da minha personalidade, trabalhando para corrigir as menos positivas.",
                    "A6 - Procuro desenvolver continuamente as minhas aptidões."
                ],
                "oportunidades": [
                    "Realizar um teste de personalidade e debater em Equipa.",
                    "Fazer testes psicotécnicos e traçar um plano de formação.",
                    "Autoavaliar conhecimentos técnicos e dinamizar um atelier útil."
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
                "descricao": "Saber fazer opções coerentes com uma matriz de valores, assumindo a responsabilidade.",
                "objetivos": [
                    "C1 - Sou capaz de fazer opções de acordo com os meus valores fundamentais.",
                    "C2 - Estabeleço para mim, com regularidade, metas a atingir."
                ],
                "oportunidades": [
                    "Participar ativamente nas escolhas do Empreendimento.",
                    "Traçar um plano concreto para alcançar um objetivo.",
                    "Criar soluções de autonomia para gerir tarefas diárias."
                ]
            },
            {
                "id": "responsabilidade",
                "nome": "Responsabilidade",
                "descricao": "Demonstrar empenho nas tarefas atribuídas, cumprir compromissos e ser persistente.",
                "objetivos": [
                    "C3 - Reconheço a importância das tarefas atribuídas e estabeleço prioridades.",
                    "C4 - Enfrento as dificuldades sem desistir de encontrar soluções."
                ],
                "oportunidades": [
                    "Assumir tarefas de preparação de um Empreendimento.",
                    "Exercer a função de Guia assumindo as respetivas responsabilidades.",
                    "Estabelecer 3 metas de vida pessoal com compromisso real."
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
                "descricao": "Conhecer a revelação de Deus através dos profetas e de Jesus Cristo.",
                "objetivos": [
                    "E1 - Conheço e compreendo a vida dos principais profetas.",
                    "E2 - Conheço a forma como Jesus se deu a conhecer aos Apóstolos."
                ],
                "oportunidades": [
                    "Organizar um raid sob um tema ou imaginário bíblico.",
                    "Ajudar na dinamização dos tempos litúrgicos de Advento ou Quaresma.",
                    "Promover um ciclo de conversas sobre a vivência da fé."
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
                "objetivos": [
                    "I1 - Procuro sempre aumentar os meus conhecimentos.",
                    "I2 - Reconheço as minhas aptidões e faço escolhas de futuro."
                ],
                "oportunidades": [
                    "Dinamizar um workshop técnico para ensinar competências.",
                    "Participar em formações jovens organizadas no município.",
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
                "objetivos": [
                    "S1 - Promovo o conhecimento dos deveres e direitos.",
                    "S2 - Participo ativamente nas comunidades intervindo em causas comuns."
                ],
                "oportunidades": [
                    "Participar na Associação de Estudantes ou Orçamento Participativo Jovem.",
                    "Realizar trabalho de voluntariado contínuo numa instituição local.",
                    "Desenvolver uma campanha de sensibilização sobre cidadania."
                ]
            }
        ]
    }
]

# 4. Interface Principal
st.title("⚜️️ Pista de Progresso - III Secção")

# Sidebar
st.sidebar.header("👤 Dados do Pioneiro")
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
        st.caption(f"Progresso: {concluidas}/{total} concluídas ({int(progresso * 100)}%)")
        
        if st.button(f"💾 Guardar Progresso - {trilho['nome']}", key=f"btn_{trilho['id']}"):
            conn = sqlite3.connect("progresso_pioneiros.db")
            cursor = conn.cursor()
            obj_cod = trilho["objetivos"][0].split(" - ")[0] if trilho["objetivos"] else ""
            for op in op_selecionadas:
                cursor.execute("""
                    INSERT INTO propostas (equipa, nome, etapa, area, trilho, objetivo_codigo, oportunidade)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (equipa, nome_pioneiro, etapa_atual, area_atual["area"], trilho["nome"], obj_cod, op))
            conn.commit()
            conn.close()
            st.success("Guardado com sucesso!")

# 5. Consulta da Base de Dados
st.markdown("---")
with st.expander("📊 Ver Base de Dados (SQLite)"):
    conn = sqlite3.connect("progresso_pioneiros.db")
    df = pd.read_sql_query("SELECT * FROM propostas ORDER BY data_registo DESC", conn)
    conn.close()
    
    if not df.empty:
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Nenhum registo guardado ainda.")
