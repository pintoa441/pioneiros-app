import streamlit as st
import pandas as pd
import json
import os

st.set_page_config(page_title="Pista - Agrupamento 78", page_icon="⚜️", layout="wide")

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

PASSWORD_DIRIGENTE = "escuteiros78"
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

TRILHOS_DATA = [
    {
        "area": "Físico",
        "trilhos": [
            {
                "id": "desempenho",
                "nome": "Desempenho",
                "obj": "F1 - Tenho preocupação com o meu desempenho físico.",
                "ops": ["Programar e executar um raid", "Organizar torneio desportivo"]
            }
        ]
    },
    {
        "area": "Afetivo",
        "trilhos": [
            {
                "id": "relacionamento",
                "nome": "Relacionamento",
                "obj": "A1 - Reconheço o valor das minhas relações afetivas.",
                "ops": ["Manter diário de vivências", "Planear convívio de equipa"]
            }
        ]
    }
]

st.sidebar.title("⚜️ Navegação")
modo = st.sidebar.radio("Selecione:", ["Área do Pioneiro", "Área da Chefia"])
registos = load_data()

if modo == "Área do Pioneiro":
    st.sidebar.markdown("---")
    equipa = st.sidebar.text_input("Equipa", "Equipa Condor")
    nome = st.sidebar.text_input("Nome", "Escuteiro")
    etapa = st.sidebar.selectbox("Etapa", ["Adesão", "Conhecimento", "Desafio", "Partida"])

    area_sel = st.sidebar.selectbox("Área", [a["area"] for a in TRILHOS_DATA])
    area_atual = next(a for a in TRILHOS_DATA if a["area"] == area_sel)

    st.header(f"Área: {area_atual['area']}")
    for trilho in area_atual["trilhos"]:
        st.subheader(f"Trilho: {trilho['nome']}")
        st.info(trilho["obj"])
        ops_feitas = []
        for i, op in enumerate(trilho["ops"]):
            if st.checkbox(op, key=f"{trilho['id']}_{i}"):
                ops_feitas.append(op)
        if st.button(f"Guardar {trilho['nome']}", key=f"btn_{trilho['id']}"):
            novos = [r for r in registos if not (r['nome'] == nome and r['trilho'] == trilho['nome'])]
            for op in ops_feitas:
                novos.append({"equipa": equipa, "nome": nome, "etapa": etapa, "area": area_atual["area"], "trilho": trilho["nome"], "oportunidade": op})
            save_data(novos)
            st.success("Guardado!")
else:
    st.subheader("🛡️ Área da Chefia")
    pwd = st.text_input("Palavra-passe:", type="password")
    if pwd == PASSWORD_DIRIGENTE:
        df = pd.DataFrame(registos)
        if not df.empty:
            st.dataframe(df, use_container_width=True)
        else:
            st.info("Sem registos ainda.")
    elif pwd:
        st.error("Palavra-passe incorreta.")
