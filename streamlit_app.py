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

# ---- FOOTER ----

footer = """

---

Rerun the app to fetch the latest data. Stock prices are updated every 5 minutes - 3 hours. Fundamentals are updated every 24 hours. 
Filters are in the sidebar :bar_chart:. Read my finance blogs here: [Medium](https://medium.com/@steffenjanbrouwer). 

Information is provided 'as is' and solely for informational purposes, not for trading purposes or advice."""

st.markdown(footer)
