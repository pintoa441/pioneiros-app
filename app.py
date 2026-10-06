import sqlite3
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Pista de Progresso - Pioneiros", page_icon="🏕️", layout="wide"
)


# Inicialização da Base de Dados Local (SQLite)
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
            proposta TEXT,
            evidencia TEXT,
            estado TEXT DEFAULT 'Pendente',
            feedback TEXT DEFAULT ''
        )
    """)
  conn.commit()
  conn.close()


init_db()


def guardar_proposta(equipa, nome, etapa, area, trilho, proposta, evidencia):
  conn = sqlite3.connect("progresso_pioneiros.db")
  cursor = conn.cursor()
  cursor.execute(
      """
        INSERT INTO propostas (equipa, nome, etapa, area, trilho, proposta, evidencia)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
      (equipa, nome, etapa, area, trilho, proposta, evidencia),
  )
  conn.commit()
  conn.close()


def carregar_propostas():
  conn = sqlite3.connect("progresso_pioneiros.db")
  df = pd.read_sql_query("SELECT * FROM propostas", conn)
  conn.close()
  return df


def atualizar_estado(proposta_id, novo_estado, feedback):
  conn = sqlite3.connect("progresso_pioneiros.db")
  cursor = conn.cursor()
  cursor.execute(
      """
        UPDATE propostas
        SET estado = ?, feedback = ?
        WHERE id = ?
    """,
      (novo_estado, feedback, proposta_id),
  )
  conn.commit()
  conn.close()


# Interface Principal
st.title("🏕️ Caderno de Pista Digital - III Secção")
st.caption("Agrupamento de Escuteiros - Sistema de Progresso Contínuo")

menu = st.sidebar.radio(
    "Navegação",
    ["📱 Área do Pioneiro", "📊 O Meu Progresso", "⚜️ Validação da Chefia/Guias"],
)

areas_dict = {
    "Físico (F)": [
        "F1: Desempenho",
        "F2: Autoconhecimento",
        "F3: Bem-Estar Físico",
    ],
    "Afetivo (A)": [
        "A1: Relacionamento",
        "A2: Equilíbrio Emocional",
        "A3: Autoestima",
    ],
    "Caráter (C)": [
        "C1: Autonomia",
        "C2: Responsabilidade",
        "C3: Coerência",
    ],
    "Espiritual (E)": [
        "E1: Descoberta",
        "E2: Aprofundamento",
        "E3: Serviço",
    ],
    "Intelectual (I)": [
        "I1: Procura do Conhecimento",
        "I2: Resolução de Problemas",
        "I3: Criatividade",
    ],
    "Social (S)": [
        "S1: Exercer Cidadania",
        "S2: Solidariedade",
        "S3: Cooperação",
    ],
}

if menu == "📱 Área do Pioneiro":
  st.header("Submeter Proposta de Trilho")

  col1, col2, col3 = st.columns(3)
  with col1:
    equipa = st.text_input("A tua Equipa:", value="Equipa Wolf")
  with col2:
    nome = st.text_input("O teu Nome:")
  with col3:
    etapa = st.selectbox(
        "Etapa Atual:",
        ["Desprendimento", "Conhecimento", "Vontade", "Construção"],
    )

  st.markdown("---")
  area = st.selectbox("Escolhe a Área (FACEIS):", list(areas_dict.keys()))
  trilho = st.selectbox("Escolhe o Trilho:", areas_dict[area])

  proposta = st.text_area(
      "O que te propões fazer para este trilho? (Oportunidade Educativa)"
  )
  evidencia = st.text_area(
      "Como vais demonstrar a conclusão? (Fotos, apresentação, relatório, ação)"
  )

  if st.button("🚀 Submeter para Validação no Conselho de Guias"):
    if nome and proposta:
      guardar_proposta(equipa, nome, etapa, area, trilho, proposta, evidencia)
      st.success(
          "Proposta enviada com sucesso! Acompanha o estado no separador 'O"
          " Meu Progresso'."
      )
    else:
      st.error("Por favor preenche o teu nome e a proposta antes de enviar.")

elif menu == "📊 O Meu Progresso":
  st.header("A Tua Pista de Progresso")
  nome_busca = st.text_input("Digita o teu nome para veres o teu progresso:")

  if nome_busca:
    df = carregar_propostas()
    df_pioneiro = df[
        df["nome"].str.lower().str.contains(nome_busca.lower(), na=False)
    ]

    validados = len(df_pioneiro[df_pioneiro["estado"] == "Validado"])
    progresso_pct = min(int((validados / 18) * 100), 100)

    st.markdown(f"### Progresso Total de {nome_busca}: {validados} / 18 Trilhos")
    st.progress(progresso_pct)

    st.subheader("Histórico de Submissões")
    for _, row in df_pioneiro.iterrows():
      cor = "🟡" if row["estado"] == "Pendente" else "🟢"
      with st.expander(f"{cor} {row['trilho']} - Estado: {row['estado']}"):
        st.write(f"**Área:** {row['area']}")
        st.write(f"**Proposta:** {row['proposta']}")
        st.write(f"**Evidência:** {row['evidencia']}")
        if row["feedback"]:
          st.info(f"**Feedback da Chefia/Guias:** {row['feedback']}")

elif menu == "⚜️ Validação da Chefia/Guias":
  st.header("Painel de Validação")
  df = carregar_propostas()

  pendentes = df[df["estado"] == "Pendente"]
  st.write(f"Existem **{len(pendentes)}** propostas pendentes de validação.")

  for _, row in pendentes.iterrows():
    with st.container():
      st.markdown(f"#### {row['nome']} ({row['equipa']}) - {row['trilho']}")
      st.write(f"**Proposta:** {row['proposta']}")
      st.write(f"**Evidência:** {row['evidencia']}")

      col_a, col_b = st.columns(2)
      with col_a:
        feedback = st.text_input(
            "Observações / Feedback:", key=f"fb_{row['id']}"
        )
      with col_b:
        if st.button("✅ Validar Trilho", key=f"val_{row['id']}"):
          atualizar_estado(row["id"], "Validado", feedback)
          st.success("Trilho validado!")
          st.rerun()
      st.markdown("---")
