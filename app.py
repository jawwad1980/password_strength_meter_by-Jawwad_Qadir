# Password Strength Meter

import re
import streamlit as st

# Styling
st.set_page_config(page_title="Password Strength Meter by Jawwad Qadir",page_icon= "🔑", layout="centered",)

# custom css
st.markdown("""
<style>
    .main {text-align:center;}
    .stTextInput {width:60% !important; margin:auto;}
    .stButton button {width:50%; background-color: blue; color: white; font-size : 18px; }
    .stButton button:hover {background-color : green;}
</style>
""", unsafe_allow_html=True)

# page title and discription
st.title("Password Strength Meter")
st.write ("Enter your Password to check the strength")

# function to check the security level
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append ("❌ Password must be 8 Character long")
    
    if re.search(r"[A to Z]", password) and re.search (r"[a to z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include both upper case and lower case")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should atleast one digit")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append ("❌ Password should include atleast special character")    

    
    if score == 4:
        st.success ("✅ Strong Password")
    elif score == 3:
        st.info ("⚠️ Moderate Password")
    else:
        st.error ("Weak Password")

# feedback
    if feedback:
        with st.expander ("Improve your password"):
            for item in feedback:
                st.write (item)

# Input
password = st.text_input ("Enter ypur password", type="password", help="Improve your password")


# button
if st.button ("Check Password strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning ("Please enter your password first")    

    




