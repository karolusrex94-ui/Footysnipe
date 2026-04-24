from __future__ import annotations
import json
from datetime import datetime
import pandas as pd
import streamlit as st
from db import (clear_all, count_predictions, delete_prediction, init_db, list_predictions, save_prediction)
from stats import (LeagueContext, TeamStats, analyze_match, apply_adjustments, base_expected_goals, chance_label, comparative, implied_odds, ppg_attack_multiplier)

st.set_page_config(page_title="Footsnipe", page_icon="⚽", layout="centered", initial_sidebar_state="collapsed")
init_db()

def _pct(p: float) -> str: return f"{p * 100:.1f}%"
def _odds(p: float) -> str:
   o = implied_odds(p)
   return "-" if o == float("inf") else f"{o:.2f}"

def chance_md(prob: float, prefix: str = "") -> str:
   info = chance_label(prob)
   txt = f"**{info['label']}** ({_pct(prob)})"
   if prefix: txt = f"{prefix}: {txt}"
   return f"{info['color']}[{txt}]"

st.title("⚽ Footsnipe")
st.caption("Analisis probabilitas pertandingan sepak bola.")

tab_analisis, tab_riwayat = st.tabs(["📊 Analisis", "📚 Riwayat"])

with tab_analisis:
   st.subheader("Data Pertandingan")
   col1, col2 = st.columns(2)
   with col1:
       home_name = st.text_input("Nama tim", value="Home FC", key="home_name")
       home_gs = st.number_input("Gol dicetak", min_value=0.0, value=1.60, key="home_gs")
       home_gc = st.number_input("Gol kebobolan", min_value=0.0, value=1.10, key="home_gc")
   with col2:
       away_name = st.text_input("Nama tim", value="Away FC", key="away_name")
       away_gs = st.number_input("Gol dicetak", min_value=0.0, value=1.20, key="away_gs")
       away_gc = st.number_input("Gol kebobolan", min_value=0.0, value=1.40, key="away_gc")
   
   submitted = st.button("📊 Hitung Probabilitas", type="primary")
   if submitted:
       st.success("Analisis berhasil dijalankan!")
