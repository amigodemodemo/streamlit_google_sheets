# streamlit_app.py

import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()


st.title("European Magic Formula")

"""

Hi there! These are the best stocks on Euronext, Deutsche Börse and London Stock Exchange according to Joel Greenblatt's Magic Formula from 'The Little Book That Beats the Market' :blue_book:. 


"""

st.write(pd.DataFrame(df))
