import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Caderno de Pista - III Secção",
    page_icon="⚜️",
    layout="wide"
)

# Base de Dados dos 18 Trilhos
TRILHOS_DATA = [
    {
        "area": "Desenvolvimento Físico",
        "cor": "#E53935",
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
                ],
                "imagem": "input_file_0.png#page=18.66&coords=17,133,783,983"
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
                    "Fazer uma análise SWOT pessoal (pontos fortes, fraquezas, oportunidades e ameaças físicas).",
                    "Organizar a semana da mobilidade na escola ou Agrupamento.",
                    "Criar um guião de campo sobre como superar barreiras para escuteiros com mobilidade reduzida."
                ],
                "imagem": "input_file_0.png#page=20.66&coords=21,215,979,723"
            },
            {
                "id": "bem_estar",
                "nome": "Bem-Estar Físico",
                "descricao": "Reger-se por um estilo de vida saudável, cuidando da apresentação, alimentação e repouso.",
                "objetivos": ["F4 - Rejo-me por um estilo de vida saudável, preocupando-me com a minha apresentação, alimentação e repouso."],
                "oportunidades": [
                    "Planear e assumir a responsabilidade pelas refeições de um fim de semana de atividade.",
                    "Elaborar um manual de boas práticas de alimentação saudável em campo.",
                    "Promover ações/workshops sobre higiene corporal, saúde oral ou cuidados dermatológicos.",
                    "Organizar debates sobre prevenção de comportamentos de risco."
                ],
                "imagem": "input_file_0.png#page=22.66&coords=17,255,983,728"
            }
        ]
    },
    {
        "area": "Desenvolvimento Afetivo",
        "cor": "#E91E63",
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
                    "Promover discussões sobre violência no namoro, bullying ou relação com os pais.",
                    "Manter um diário de vivências e sentimentos.",
                    "Convidar a família para momentos marcantes da vida escutista.",
                    "Planear um momento de convívio aberto à família e amigos."
                ],
                "imagem": "input_file_0.png#page=24.66&coords=12,284,988,719"
            },
            {
                "id": "equilibrio",
                "nome": "Equilíbrio Emocional",
                "descricao": "Agir de forma ponderada, sabendo gerir os sentimentos dos outros.",
                "objetivos": ["A4 - Ajo de forma ponderada, respeitando o sentimento dos outros e esforço-me por corrigir quando me excedo."],
                "oportunidades": [
                    "Escrever um diário de emoções do último mês e refletir sobre como atuou.",
                    "Organizar um debate na Equipa e avaliar como lidou com opiniões divergentes.",
                    "Criar um role-play com colisões de opiniões para praticar o autocontrolo."
                ],
                "imagem": "input_file_0.png#page=26.66&coords=17,215,983,723"
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
                    "Realizar um teste de personalidade e dinamizar uma discussão em Equipa.",
                    "Fazer testes psicotécnicos e traçar um plano de formação/estudos.",
                    "Autoavaliar os conhecimentos técnicos e dinamizar um atelier útil para a Comunidade."
                ],
                "imagem": "input_file_0.png#page=28.66&coords=12,210,988,728"
            }
        ]
    }
]

# Título Principal
st.title("⚜️ Progresso Pessoal - Pioneiros (III Secção)")
st.caption("Caderno de Pista Digital")

# Sidebar - Seleção da Área
area_nomes = [a["area"] for a in TRILHOS_DATA]
area_selecionada_nome = st.sidebar.selectbox("Seleciona a Área de Desenvolvimento", area_nomes)

area_atual = next(a for a in TRILHOS_DATA if a["area"] == area_selecionada_nome)

st.header(area_atual["area"])

# Interface de Abas para os Trilhos da Área
trilho_nomes = [t["nome"] for t in area_atual["trilhos"]]
tabs = st.tabs(trilho_nomes)

for idx, tab in enumerate(tabs):
    trilho = area_atual["trilhos"][idx]
    with tab:
        st.subheader(trilho["nome"])
        st.write(f"*{trilho['descricao']}*")
        
        # Bloco de Objetivos de Progresso
        st.markdown("### 🎯 Objetivos de Progresso")
        for obj in trilho["objetivos"]:
            st.info(obj)
            
        # Lista de Checkboxes de Oportunidades Educativas
        st.markdown("### 🚩 Oportunidades Educativas")
        concluidas = 0
        total = len(trilho["oportunidades"])
        
        for i, op in enumerate(trilho["oportunidades"]):
            key = f"{trilho['id']}_op_{i}"
            if st.checkbox(op, key=key):
                concluidas += 1
                
        # Barra de Progresso do Trilho
        progresso = concluidas / total if total > 0 else 0
        st.progress(progresso)
        st.caption(f"Progresso no Trilho: {concluidas}/{total} oportunidades concluídas ({int(progresso * 100)}%)")
