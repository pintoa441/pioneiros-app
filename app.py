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
    # Recria a tabela limpa para os testes
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

# 3. Estrutura Completa dos 18 Trilhos de Progresso
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
                    "F3 - Reconheço e respeito as diferenças entre homens e mulheres e as necessidades de cada um, agindo sempre em conformidade."
                ],
                "oportunidades": [
                    "Arranjar soluções na vida diária para inclusão de pessoas com deficiência.",
                    "Promover um debate, palestra ou campanha sobre prevenção do bullying ou discriminação.",
                    "Fazer uma análise SWOT pessoal (pontos fortes, fraquezas, oportunidades e ameaças físicas).",
                    "Organizar a semana da mobilidade na escola ou Agrupamento.",
                    "Criar um guião de campo sobre como superar barreiras para escuteiros com mobilidade reduzida."
                ]
            },
            {
                "id": "bem_estar",
                "nome": "Bem-Estar Físico",
                "descricao": "Reger-se por um estilo de vida saudável, cuidando da apresentação, alimentação e repouso.",
                "objetivos": ["F4 - Rejo-me por um estilo de vida saudável, preocupando-me com a minha apresentação, alimentação e repouso, evitando comportamentos e substâncias de risco."],
                "oportunidades": [
                    "Planear e assumir a responsabilidade pelas refeições de um fim de semana de atividade, segundo a Roda dos Alimentos.",
                    "Elaborar um manual de boas práticas de alimentação saudável em campo.",
                    "Promover ações/workshops sobre higiene corporal, saúde oral ou cuidados dermatológicos.",
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
                    "A1 - Reconheço o valor das minhas relações afetivas e da minha sexualidade, respeitando os outros.",
                    "A2 - Reconheço o valor da família e comprometo-me com o bem-estar da mesma.",
                    "A3 - Demonstro maturidade perante os conflitos e reconheço diferentes sensibilidades e gostos."
                ],
                "oportunidades": [
                    "Promover discussões sobre violência no namoro, bullying ou relação com os pais.",
                    "Manter um diário de vivências e sentimentos.",
                    "Convidar a família para momentos marcantes da vida escutista, escolar ou desportiva.",
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
                    "Criar um role-play com colisões de opiniões para praticar o autocontrolo e a gestão de conflitos.",
                    "Definir pontos de esforço pessoais durante um período e avaliar atitudes diárias."
                ]
            },
            {
                "id": "autoestima",
                "nome": "Autoestima",
                "descricao": "Conhecer e aceitar a própria personalidade, esforçando-se para superar limitações.",
                "objetivos": [
                    "A5 - Reconheço as características da minha personalidade, trabalhando sempre para corrigir as menos positivas.",
                    "A6 - Procuro desenvolver continuamente as minhas aptidões e esforço-me para melhorar as minhas limitações."
                ],
                "oportunidades": [
                    "Realizar um teste de personalidade e dinamizar uma discussão em Equipa sobre como lidar com personalidades diferentes.",
                    "Fazer testes psicotécnicos e traçar um plano de formação/estudos para o futuro.",
                    "Autoavaliar os conhecimentos técnicos e dinamizar um atelier útil para a Comunidade.",
                    "Elaborar uma carta de compromisso com os valores a praticar no dia a dia."
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
                    "C1 - Sou capaz de fazer opções, de acordo com a minha referência de valores fundamentais, aceitando as suas implicações.",
                    "C2 - Estabeleço para mim, com regularidade, metas a atingir em várias áreas da minha vida."
                ],
                "oportunidades": [
                    "Participar ativamente nas discussões e escolhas do Empreendimento.",
                    "Traçar um plano concreto para alcançar um objetivo (especialidade ou cargo).",
                    "Decidir de forma consciente uma área de estudos.",
                    "Criar soluções de autonomia para gerir tarefas diárias sem depender dos pais."
                ]
            },
            {
                "id": "responsabilidade",
                "nome": "Responsabilidade",
                "descricao": "Demonstrar empenho nas tarefas atribuídas, cumprir compromissos e ser persistente.",
                "objetivos": [
                    "C3 - Reconheço a importância das tarefas que me foram atribuídas, estabeleço prioridades e respeito-as.",
                    "C4 - Enfrento as dificuldades sem desistir de encontrar soluções ou alternativas.",
                    "C5 - Reconheço que as minhas ações/decisões têm influência nos grupos de que faço parte."
                ],
                "oportunidades": [
                    "Assumir tarefas de preparação de um Empreendimento e dinamizar momentos formativos.",
                    "Exercer a função de Guia ou responsável de tarefa assumindo as consequências.",
                    "Assumir o cargo de delegado de turma ou funções de responsabilidade na escola.",
                    "Estabelecer 3 metas de vida pessoal com compromisso real."
                ]
            },
            {
                "id": "coerencia",
                "nome": "Coerência",
                "descricao": "Viver o dia a dia segundo as convicções de vida, partilhando e defendendo valores morais.",
                "objetivos": [
                    "C6 - Partilho e defendo aquilo em que acredito de forma serena e fundamentada.",
                    "C7 - Ajo cada dia de acordo com as minhas convicções de referências."
                ],
                "oportunidades": [
                    "Criar pontos de esforço mensais com boas ações e testemunho de valores.",
                    "Organizar uma apresentação/dinâmica sobre o Escutismo na escola ou grupo exterior.",
                    "Identificar e registar 10 momentos da vida quotidiana onde colocou em prática a Lei do Escuta.",
                    "Partilhar com a família/comunidade os valores que o orientam."
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
                    "E1 - Conheço e compreendo a vida dos principais profetas e a sua relação com Deus.",
                    "E2 - Conheço a forma como Jesus se deu progressivamente a conhecer aos Apóstolos.",
                    "E3 - Reconheço que na Igreja todos os membros são diferentes e que, unidos nas diferenças, tornamos a comunidade mais rica."
                ],
                "oportunidades": [
                    "Organizar um raid sob um tema ou imaginário bíblico.",
                    "Escolher frequentar a disciplina de EMRC na escola.",
                    "Ajudar na dinamização dos tempos litúrgicos de Advento ou Quaresma.",
                    "Promover um ciclo de conversas sobre a vivência da fé cristã no quotidiano."
                ]
            },
            {
                "id": "aprofundamento",
                "nome": "Aprofundamento",
                "descricao": "Cultivar a oração pessoal e comunitária, participar na Eucaristia e aprofundar a fé.",
                "objetivos": [
                    "E4 - Aprofundando os hábitos de oração diários e participo nas celebrações comunitárias.",
                    "E5 - Conheço o ponto de vista da Igreja sobre os temas principais.",
                    "E6 - Aprofundo a minha identidade católica no contacto com as outras religiões."
                ],
                "oportunidades": [
                    "Fazer o Sacramento do Crisma.",
                    "Fazer a leitura e reflexão em grupo de uma homilia ou documento do Papa.",
                    "Dinamizar um grupo de jovens ou catequese na Paróquia.",
                    "Organizar uma visita a locais de culto de outras confissões religiosas."
                ]
            },
            {
                "id": "servico_espiritual",
                "nome": "Serviço",
                "descricao": "Assumir a responsabilidade pelo cuidado da Criação e defender a vida humana.",
                "objetivos": [
                    "E7 - Protejo a Natureza e a vida humana como obra de Deus, defendendo a última como valor absoluto.",
                    "E8 - Ponho-me ao serviço dos outros, marcando positivamente, como cristão, todos os grupos."
                ],
                "oportunidades": [
                    "Colaborar ativamente como acólito, leitor ou catequista.",
                    "Dinamizar a partilha da Luz da Paz de Belém na localidade.",
                    "Criar iniciativas ecológicas para reduzir a pegada ambiental na Sede.",
                    "Dinamizar uma atividade de serviço social ou animação numa comunidade isolada."
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
                "descricao": "Aumentar os conhecimentos utilizando ferramentas de informação e gerindo competências.",
                "objetivos": [
                    "I1 - Procuro sempre aumentar os meus conhecimentos, sabendo utilizar as ferramentas de informação.",
                    "I2 - Reconheço as minhas aptidões e faço as minhas opções na área profissional ou de estudos."
                ],
                "oportunidades": [
                    "Dinamizar uma oficina/workshop técnico para ensinar competências à Comunidade.",
                    "Criar um folheto informativo sobre a área profissional que ambiciona seguir.",
                    "Participar em formações jovens organizadas pela freguesia ou município.",
                    "Criar uma ferramenta ou plataforma digital de apoio à preparação do Empreendimento."
                ]
            },
            {
                "id": "resolucao_problemas",
                "nome": "Resolução de Problemas",
                "descricao": "Avaliar experiências de vida criticamente e resolver imprevistos com autonomia.",
                "objetivos": [
                    "I3 - Sei avaliar as experiências que vivo e utilizo-as de forma criativa nas novas situações.",
                    "I4 - Consigo analisar problemas, propor soluções e escolher a mais adequada."
                ],
                "oportunidades": [
                    "Assumir uma função nova e desafiante na preparação do próximo Empreendimento.",
                    "Dinamizar um brainstorming para encontrar soluções sustentáveis para o Agrupamento.",
                    "Diagnosticar e executar 5 melhorias necessárias na Sede.",
                    "Desenvolver o plano de emergência e simulação de evacuação para a Sede."
                ]
            },
            {
                "id": "criatividade",
                "nome": "Criatividade e Expressão",
                "descricao": "Imaginar e concretizar ideias inovadoras utilizando diversas formas de comunicação.",
                "objetivos": [
                    "I5 - Desafio-me a criar ideias e projetos inovadores, de acordo com os meus conhecimentos e gostos.",
                    "I6 - Exploro diferentes técnicas, ideias e meios e apresento-as de forma criativa."
                ],
                "oportunidades": [
                    "Organizar uma exposição artística ou fotográfica na Sede.",
                    "Criar a maquete e a planta de construções para o acampamento.",
                    "Preparar ou animar uma peça de Fogo de Conselho.",
                    "Concorrer à criação de insígnias ou projetos de inovação escutista."
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
                "descricao": "Conhecer deveres e direitos e intervir democraticamente em projetos comunitários.",
                "objetivos": [
                    "S1 - Promovo ativamente o conhecimento dos meus deveres e direitos por todos.",
                    "S2 - Participo ativamente nas comunidades em que me insiro intervindo em causas comuns.",
                    "S3 - Aceito a decisão de uma votação e ainda que perca, trabalho no sentido do todo."
                ],
                "oportunidades": [
                    "Participar ativamente na Associação de Estudantes ou Orçamento Participativo Jovem.",
                    "Realizar trabalho de voluntariado contínuo numa instituição local.",
                    "Desenvolver uma campanha de sensibilização sobre um tema de cidadania atual."
                ]
            },
            {
                "id": "solidariedade",
                "nome": "Solidariedade e Tolerância",
                "descricao": "Estar atento às necessidades dos outros e apoiar a resolução de problemas sociais
