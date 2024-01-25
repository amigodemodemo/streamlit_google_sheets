# Import dependencies
import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Create a connection object
conn = st.connection("gsheets", type=GSheetsConnection)
dataframe = conn.read()

# Introduction text
"""
Hi there! This is a simple Google Sheets example on how to embed a dynamic table on a Medium blog with Streamlit! 
"""

# Define tabs
tab1, tab2 = st.tabs(["Table", "Graph"])

# Streamlit content
with tab1:
  st.write(pd.DataFrame(dataframe))
with tab2:
  st.line_chart(pd.DataFrame(dataframe),x="Date", y="Close")

# Footer text
"""
The data shown above is the historic stock price of Google. In the "Graph" tab I have put an example of a simple graph that can be embedded. 
"""
"""
You can read my blog here:
"""
