import os
import streamlit as st
import numpy as np
from PIL import  Image

# Custom imports 
from multipage import MultiPage
from pages import data_upload, machine_learning, metadata, data_visualize, redundant, recommandation, automated_eda # import your pages here

# Create an instance of the app 
app = MultiPage()

# Title of the main page
#display = Image.open('Logo.png')
#display = np.array(display)
# st.image(display, width = 400)
# st.title("Data Storyteller Application")
col1, col2 = st.columns(2)
#col1.image(display, width = 400)
st.title("Recommandation Application")

# Add all your application here
app.add_page("Type of Recom Model", recommandation.app)
app.add_page("Upload Data", data_upload.app)
app.add_page("Change Metadata", metadata.app)
#app.add_page("Machine Learning", machine_learning.app)
app.add_page("Data Analysis",data_visualize.app)
app.add_page("Automated EDA",automated_eda.app)
#app.add_page("Y-Parameter Optimization",redundant.app)

# The main app
app.run()
