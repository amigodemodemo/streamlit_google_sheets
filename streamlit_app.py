# Import dependencies
import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Create a connection object
conn = st.connection("gsheets", type=GSheetsConnection)
dataframe = conn.read()

# Streamlit content
"""
Hi there! This is a simple Google Sheets example how to embed an interactive table on a Medium blog with Streamlit!
"""
st.write(pd.DataFrame(dataframe))
st.line_chart(pd.DataFrame(dataframe),x="Date", y="Close")
"""
You can read the blog here:
"""


