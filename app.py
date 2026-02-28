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

    .stApp {
        background-color: #fbf9f6; /* Soft, warm background */
        color: #2b3a42;
        font-family: 'Inter', sans-serif;
    }
    
    /* --- FORM VISIBILITY FIXES (The "Last Section") --- */
    /* Forces labels to be dark and readable */
    .stTextInput label, .stTextArea label {
        color: #2b3a42 !important;
        font-weight: 600 !important;
        font-size: 1.1em !important;
    }

    /* Forces input boxes to have a white background and visible border */
    div[data-baseweb="input"], div[data-baseweb="textarea"] {
        background-color: #ffffff !important;
        border: 1px solid #d1d5db !important;
        border-radius: 8px !important;
    }

    /* Ensure typed text is dark */
    input, textarea {
        color: #2b3a42 !important;
    }

    /* Submit Button Styling */
    div.stButton > button {
        background-color: #e63946 !important;
        color: white !important;
        border: none !important;
        padding: 15px !important;
        font-weight: 700 !important;
        font-size: 1.1em !important;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #c53030 !important;
        box-shadow: 0 4px 15px rgba(230, 57, 70, 0.3);
    }

    /* Headers */
    .hero-title {
        font-family: 'Playfair Display', serif;
        color: #1a252f;
        text-align: center;
        font-size: 3.2em;
        font-weight: 700;
        margin-bottom: 5px;
        line-height: 1.2;
    }
    .hero-subtitle {
        font-family: 'Inter', sans-serif;
        text-align: center;
        color: #e63946; 
        font-size: 1.2em;
        margin-bottom: 35px;
        font-weight: 600;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    /* Stats & Progress */
    .campaign-stats-container {
        background-color: #ffffff;
        padding: 40px;
        border-radius: 16px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.05);
        margin-bottom: 40px;
        border-top: 5px solid #e63946;
    }
    .stats-flex {
        display: flex;
        justify-content: space-between;
        margin-bottom: 20px;
    }
    .stat-label {
        font-size: 0.95em;
        color: #7f8c8d;
        font-weight: 600;
        text-transform: uppercase;
    }
    .stat-value {
        font-family: 'Playfair Display', serif;
        font-size: 2.5em;
        font-weight: 700;
        color: #1a252f;
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
        border-radius: 20px;
    }
    
    .story-card {
        background-color: #ffffff;
        padding: 50px;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.03);
        line-height: 1.9;
        margin-bottom: 40px;
        color: #4a5568;
    }

    .section-header {
        font-family: 'Playfair Display', serif;
        text-align: center; 
        color: #1a252f; 
        font-size: 2.4em;
        font-weight: 700;
        margin-bottom: 30px;
    }
    
    .caption-text {
        text-align: center; 
        color: #a0aec0; 
        font-size: 0.9em;
        font-style: italic;
        margin-top: 12px;
    }
    
    hr { border: 0; height: 1px; background: #e2e8f0; margin: 50px 0; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1 class='hero-title'>Help Me Save My Father</h1>", unsafe_allow_html=True)
st.markdown("<p class='hero-subtitle'>Medical Fundraiser for Samir Singha Mahapatra</p>", unsafe_allow_html=True)

# --- FATHER'S PHOTO ---
father_img = get_image("father")
if father_img:
    col_img1, col_img2, col_img3 = st.columns([1, 2, 1])
    with col_img2:
        st.image(father_img, use_container_width=True)
        st.markdown("<p class='caption-text'>My Father, Samir Singha Mahapatra</p>", unsafe_allow_html=True)

# --- THE GOAL & PROGRESS ---
target_amount = 500000
raised_amount = 35000 
progress_percent = min((raised_amount / target_amount) * 100, 100)
display_percent = max(progress_percent, 2) 

st.markdown(f"""
<div class='campaign-stats-container'>
    <div class='stats-flex'>
        <div class='stat-box'>
            <div class='stat-label'>Amount Raised</div>
            <div class='stat-value'>₹{raised_amount:,}</div>
        </div>
        <div class='stat-box' style='text-align: right;'>
            <div class='stat-label'>Target Goal</div>
            <div class='stat-value'>₹{target_amount:,}</div>
        </div>
    </div>
    <div class='custom-progress-bg'>
        <div class='custom-progress-fill' style='width: {display_percent}%;'></div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- THE STORY ---
st.markdown("""
<div class='story-card'>
    <h3 style='text-align: center; font-family: "Playfair Display", serif;'>A Son's Appeal</h3>
    <p>Recently, our world came to a sudden and terrifying halt when my father was diagnosed with Stage 1 cancer. Surgery is scheduled for <b>March 3rd</b>.</p>
    <p>I am working long night shifts to support my family, but the financial weight is more than we can carry alone. I am humbly asking for your support.</p>
    <p style='margin-top: 30px;'><i>With a grateful heart,</i><br><b>— Gourab Singha Mahapatra</b></p>
</div>
""", unsafe_allow_html=True)

# --- HOW TO DONATE & TRANSPARENCY (Existing Logic) ---
# [Note: You can keep your Bank/QR code and Medical Docs logic here as it was]

st.markdown("<hr>", unsafe_allow_html=True)

# --- LAST SECTION: LEAVE A MESSAGE FORM ---
st.markdown("<h2 class='section-header'>Leave a Message of Support</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #718096; margin-bottom: 30px;'>Did you contribute or share the page? Leave a message below.</p>", unsafe_allow_html=True)

GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzM1DEP3J3biL5ERQTTe_dVZIpfsNg-FFmhmacy8GwhDvY584ou0EtvsjKLHQGD6koX/exec"

with st.form("support_form", clear_on_submit=True):
    donor_name = st.text_input("Your Name")
    donor_amount = st.text_input("Amount Donated (Optional)")
    donor_message = st.text_area("Your Message")
    
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
                st.success(f"Thank you, {donor_name}! Your message has been sent.")
                st.balloons()
            except Exception as e:
                st.error("Something went wrong connecting to the database.")
        else:
            st.warning("Please enter your name and a message.")
