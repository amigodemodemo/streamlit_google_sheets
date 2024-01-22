# streamlit_app.py

import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.set_page_config(
    page_title="Simple Google Sheets example",
    page_icon=":bar_chart:",
    # layout="wide",
    initial_sidebar_state="collapsed",
)


# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()



st.title("Simple Google Sheets example using Streamlit")

"""

Hi there! This is a simple example how to embed an interactive table on a medium blog!


"""

# ---- SIDEBAR ----
st.sidebar.header("Settings and Filters")

st.write(pd.DataFrame(df))

# ---- SIDEBAR ----
st.sidebar.header("Settings and Filters")
