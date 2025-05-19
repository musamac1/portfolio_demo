from pathlib import Path

import streamlit as st
from PIL import Image
import re

import streamlit as st
import requests  # pip install requests



# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

profile_pic = current_dir / "assets" / "boss.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Muhammad Musa Maqsood"
PAGE_ICON = ":wave:"
NAME = "Muhammad Musa Maqsood"
DESCRIPTION = """
Data Analyst, Electrical Engineer
"""


  


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
   




st.write('\n')
st.subheader("Projects")
st.write(
"""
-  🏆Sentimental Analysis 
-  🏆Movie Recommendation System
-  🏆User Management System
-  🏆Credit Card Fraud Detection
-  🏆Weather app
-  🏆Voice Recognition System
-  🏆Restaurant Reservation System
-  🏆loan eligibility system
-  🏆Scrapping data from google maps
"""
)
