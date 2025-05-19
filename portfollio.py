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
PAGE_TITLE = "Digital CV | Rahima Sarfraz"
PAGE_ICON = ":wave:"
NAME = "Rahima Sarfraz💞"
DESCRIPTION = """
Cherry, Pookie
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
   





st.subheader("HAPPY BIRTHDAY")
st.write(
"""
Happy Birthday, Rahima ❤️
Every moment with you feels like magic,
I’m so grateful for your love, your laughter, and your beautiful heart.Rahima, you’ve brought so much love and happiness into my life that I honestly can’t imagine a world without you in it.
On this special day I just want you to know how incredibly grateful I am for you  I hope this year brings you all the happiness and success your heart desires because you deserve nothing less than the absolute best.
my heart, my joy, my everything. I’m so lucky to be loved by you, and I promise to keep loving you more and more with every passing year I promise to stand by you, cheer for you, support you, and love you through every high and low
😊🎉💖🥰🎂🌹 💘اللہ تمہیں ہمیشہ ہنستا مسکراتا رکھے 😊✨
میری دعائیں ہمیشہ تمہارے ساتھ ہیں 💌
"""
)
