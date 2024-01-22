# streamlit_app.py

import streamlit as st
import panda
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

st.write(pd.DataFrame(df))