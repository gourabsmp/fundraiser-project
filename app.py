import streamlit as st
import os
import urllib.parse
import urllib.request

# --- BULLETPROOF IMAGE FINDER ---
def get_image(base_name):
    for ext in ['.jpg', '.jpeg', '.JPG', '.JPEG', '.png', '.PNG']:
        if os.path.exists(base_name + ext):
            return base_name + ext
    return None

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Help Save My Father", page_icon="❤️", layout="centered")

# --- EMOTIONAL & WARM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Playfair+Display:ital,wght@0,500;0,700;1,500&display=swap');

    /* Main App Background */
    .stApp {
        background-color: #fbf9f6 !important;
        color: #2b3a42 !important;
        font-family: 'Inter', sans-serif;
    }
    
    /* --- THE "LAST SECTION" FIX (FORCE LIGHT THEME) --- */
    /* This targets the form container specifically */
    [data-testid="stForm"] {
        background-color: #ffffff !important;
        padding: 30px !important;
        border-radius: 15px !important;
        border: 1px solid #eee !important;
    }

    /* Force Labels to be Dark Grey/Black */
    [data-testid="stForm"] label p {
        color: #2b3a42 !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
    }

    /* Force Input Boxes to be White with Dark Text */
    [data-testid="stForm"] div[data-baseweb="base-input"], 
    [data-testid="stForm"] div[data-baseweb="textarea"] {
        background-color: #fcfcfc !important;
        border: 1px solid #cccccc !important;
        color: #000000 !important;
    }

    /* Force the actual text inside the input to be black */
    [data-testid="stForm"] input, 
    [data-testid="stForm"] textarea {
        color: #000000 !important;
        background-color: transparent !important;
    }

    /* Submit Button - Red Design */
    [data-testid="stForm"] button {
        background-color: #e63946 !important;
        color: white !important;
        border: none !important;
        font-weight: 700 !important;
        height: 3em !important;
    }

    /* General Typography */
    .hero-title {
        font-family: 'Playfair Display', serif;
        color: #1a252f;
        text-align: center;
        font-size: 3.2em;
        font-weight: 700;
        margin-bottom: 5px;
    }
    .hero-subtitle {
        text-align: center;
        color: #e63946;
        font-size: 1.2em;
        font-weight: 600;
        margin-bottom: 35px;
    }

    .campaign-stats-container {
        background-color: #ffffff;
        padding: 40px;
        border-radius: 16px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.05);
        border-top: 5px solid #e63946;
    }
    
    .custom-progress-bg {
        background-color: #f0f2f5;
        border-radius: 20px;
        height: 22px;
        width: 100%;
        overflow: hidden;
    }
    .custom-progress-fill {
        background: linear-gradient(90deg, #f4a261, #e76f51, #2a9d8f);
        height: 100%;
    }

    .section-header {
        font-family: 'Playfair Display', serif;
        text-align: center; 
        color: #1a252f; 
        font-size: 2.4em;
        margin-bottom: 10px;
    }

    hr { border: 0; height: 1px; background: #e2e8f0; margin: 50px 0; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1 class='hero-title'>Help Me Save My Father</h1>", unsafe_allow_html=True)
st.markdown("<p class='hero-subtitle'>Medical Fundraiser for Samir Singha Mahapatra</p>", unsafe_allow_html=True)

# --- PROGRESS ---
target_amount = 500000
raised_amount = 35000 
progress_percent = min((raised_amount / target_amount) * 100, 100)

st.markdown(f"""
<div class='campaign-stats-container'>
    <div style='display: flex; justify-content: space-between; margin-bottom: 10px;'>
        <b>Raised: ₹{raised_amount:,}</b>
        <b>Goal: ₹{target_amount:,}</b>
    </div>
    <div class='custom-progress-bg'>
        <div class='custom-progress-fill' style='width: {progress_percent}%;'></div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- LAST SECTION: MESSAGE FORM ---
st.markdown("<h2 class='section-header'>Leave a Message of Support</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #718096;'>Your kindness gives us strength.</p>", unsafe_allow_html=True)

GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzM1DEP3J3biL5ERQTTe_dVZIpfsNg-FFmhmacy8GwhDvY584ou0EtvsjKLHQGD6koX/exec"

with st.form("support_form", clear_on_submit=True):
    donor_name = st.text_input("Full Name")
    donor_amount = st.text_input("Amount (Optional)")
    donor_message = st.text_area("Your Message of Support")
    
    submitted = st.form_submit_button("Send Message ❤️", use_container_width=True)

    if submitted:
        if donor_name and donor_message:
            try:
                data = urllib.parse.urlencode({
                    'name': donor_name, 
                    'amount': donor_amount, 
                    'message': donor_message
                }).encode('utf-8')
                req = urllib.request.Request(GOOGLE_SCRIPT_URL, data=data)
                urllib.request.urlopen(req)
                st.success("Thank you! Your message has been received.")
                st.balloons()
            except:
                st.error("Submission failed. Please check your internet connection.")
        else:
            st.warning("Please fill in your name and message.")
