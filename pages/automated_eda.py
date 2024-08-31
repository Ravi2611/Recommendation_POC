import streamlit as st
import numpy as np
import pandas as pd
from pages import utils
# Custom imports 
from multipage import MultiPage
from pages import pandas_autoprofilling, automtedEDA_autoviz,automatedEDA_dtale


# @st.cache
def app():
    st.markdown("## Select Liberary to see automated EDA")

    # Option to select predition type 
    st.info("Please see the documatation of each library for automated EDA")
    option = st.selectbox(
    "Please Select Your Choice for automated EDA?",
    ("Automate EDA Pandas Profiling", "Automate EDA Autoviz", "Automate EDA Dtale"),index=None,
    placeholder="Select youe choice...")

    st.write("You selected:", option)
    if option == "Automate EDA Pandas Profiling":
        pandas_autoprofilling.app()
    if option == "Automate EDA Autoviz":
        automtedEDA_autoviz.app()
    if option == "Automate EDA Dtale":
        automatedEDA_dtale.app()


  