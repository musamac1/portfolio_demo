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
   


# --- SOCIAL LINKS ---

#education

st.write('\n')
st.subheader("Education")
st.write(
    """
- ✔️ University Of Engineering Technology,Lahore (2023-2027)
- 🏆 Electrical Engineering
- ✔️ GCU,Lahore (2021-2023)
- 🏆 FSC-Pre engg
- ✔️ The Educators (2019-2021)
- 🏆 Matriculation-Computer Science
"""
)
# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Veroboard Circuit Designing
- ✔️ knowledge in Python , C and MS OFFICE
- ✔️ PCB designing
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas),C
- 📊 Data Visulization:  MS Excel
- 📚 Modeling: Logistic regression, linear regression, decision trees
- 🏆 Circuit designing: Altium and Multisim
"""
)
st.write('\n')
st.subheader("Certifications")
st.write(
    """
- 👩‍💻Data Science and Machine Learning using python 
- 🏆LUMS(2024)

"""
)
st.write('\n')
st.subheader("Award And Honors")
st.write(
    """
-	✔️Got fifth position in the entrance exam of GCU, Lahore (pre-engineering) out of 15000 students
-   ✔️ Fourth Position in Matric(1094/1100)
"""
)
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
