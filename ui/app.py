import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

import streamlit as st
from core.loader import load_data
from agent.hugo_agent import hugo_answer


st.set_page_config(page_title="Hugo AI", layout="centered")
st.title("🤖🛒 Hugo – Procurement AI Agent")

data = load_data("data")

q = st.text_input("Ask Hugo about operations:")
if q:
    st.success(hugo_answer(q, data))
