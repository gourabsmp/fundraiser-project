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

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Playfair+Display:ital,wght@0,500;0,700;1,500&display=swap');

    .stApp {
        background-color: #fbf9f6; 
        color: #2b3a42;
        font-family: 'Inter', sans-serif;
    }
    
    /* --- THE LAST SECTION COLOR FIX --- */
    /* Targets the form specifically to force a light theme */
    [data-testid="stForm"] {
        background-color: #ffffff !important;
        padding: 30px !important;
        border-radius: 16px !important;
        border: 1px solid #e2e8f0 !important;
    }

    /* Force labels to be dark and readable */
    [data-testid="stForm"] label p {
        color: #2b3a42 !important;
        font-weight: 600 !important;
    }

    /* Force Input & Textarea to have white background and dark text */
    [data-testid="stForm"] div[data-baseweb="base-input"], 
    [data-testid="stForm"] div[data-baseweb="textarea"] {
        background-color: #ffffff !important;
        border: 1px solid #d1d5db !important;
    }

    [data-testid="stForm"] input, 
    [data-testid="stForm"] textarea {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
    }

    /* Submit Button */
    [data-testid="stForm"] button {
        background-color: #e63946 !important;
        color: white !important;
        border: none !important;
        font-weight: 700 !important;
    }

    /* Original Styles Restored */
    .hero-title { font-family: 'Playfair Display', serif; color: #1a252f; text-align: center; font-size: 3.2em; font-weight: 700; margin-bottom: 5px; line-height: 1.2; }
    .hero-subtitle { font-family: 'Inter', sans-serif; text-align: center; color: #e63946; font-size: 1.2em; margin-bottom: 35px; font-weight: 600; letter-spacing: 1px; text-transform: uppercase; }
    .campaign-stats-container { background-color: #ffffff; padding: 40px; border-radius: 16px; box-shadow: 0 10px 40px rgba(0,0,0,0.05); margin-bottom: 40px; border-top: 5px solid #e63946; }
    .stats-flex { display: flex; justify-content: space-between; margin-bottom: 20px; }
    .stat-label { font-size: 0.95em; color: #7f8c8d; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }
    .stat-value { font-family: 'Playfair Display', serif; font-size: 2.5em; font-weight: 700; color: #1a252f; margin-top: 5px; }
    .custom-progress-bg { background-color: #f0f2f5; border-radius: 20px; height: 22px; width: 100%; overflow: hidden; margin-bottom: 10px; }
    .custom-progress-fill { background: linear-gradient(90deg, #f4a261, #e76f51, #2a9d8f); height: 100%; border-radius: 20px; }
    .story-card { background-color: #ffffff; padding: 50px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); line-height: 1.9; font-size: 1.15em; margin-bottom: 40px; color: #4a5568; position: relative; }
    .donate-card { background-color: #ffffff; padding: 35px; border-radius: 16px; box-shadow: 0 8px 30px rgba(0,0,0,0.04); border: 1px solid #edf2f7; flex: 1; transition: transform 0.3s ease; }
    .card-header { font-family: 'Playfair Display', serif; font-weight: 700; font-size: 1.5em; color: #1a252f; margin-bottom: 20px; text-align: center; border-bottom: 1px solid #edf2f7; padding-bottom: 15px; }
    .bank-details-list { list-style: none; padding: 0; color: #4a5568; font-size: 1.1em; line-height: 2; }
    .bank-details-list li span { font-weight: 600; color: #2d3748; display: inline-block; width: 140px; }
    .upi-highlight { background-color: #fff5f5; color: #c53030; padding: 12px 15px; border-radius: 8px; font-weight: 700; text-align: center; font-size: 1.2em; margin-top: 20px; border: 1px dashed #feb2b2; }
    .section-header { font-family: 'Playfair Display', serif; text-align: center; color: #1a252f; font-size: 2.4em; font-weight: 700; margin-bottom: 30px; }
    .caption-text { text-align: center; color: #a0aec0; font-size: 0.9em; font-style: italic; margin-top: 12px; }
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

# --- GOAL & PROGRESS ---
target_amount, raised_amount = 500000, 35000 
progress_percent = min((raised_amount / target_amount) * 100, 100)

st.markdown(f"""
<div class='campaign-stats-container'>
    <div class='stats-flex'>
        <div class='stat-box'><div class='stat-label'>Amount Raised</div><div class='stat-value'>₹{raised_amount:,}</div></div>
        <div class='stat-box' style='text-align: right;'><div class='stat-label'>Target Goal</div><div class='stat-value target'>₹{target_amount:,}</div></div>
    </div>
    <div class='custom-progress-bg'><div class='custom-progress-fill' style='width: {max(progress_percent, 2)}%;'></div></div>
    <div style='text-align: right; color: #718096; font-size: 0.95em; margin-top: 10px;'>{progress_percent:.1f}% Funded</div>
</div>
""", unsafe_allow_html=True)

# --- STORY ---
st.markdown("""
<div class='story-card'>
    <h3>A Son's Appeal</h3>
    <p>Recently, our world came to a halt when my father was diagnosed with Stage 1 cancer. Surgery is March 3rd. I am working night shifts, but we cannot do this alone. Your kindness means everything.</p>
    <p style='margin-top: 30px;'><i>With a grateful heart,</i><br><b>— Gourab Singha Mahapatra</b></p>
</div>
""", unsafe_allow_html=True)

# --- HOW TO DONATE ---
st.markdown("<h2 class='section-header'>How You Can Help</h2>", unsafe_allow_html=True)
col_qr, col_bank = st.columns([1, 1.3])
with col_qr:
    st.markdown("<div class='donate-card'><div class='card-header'>📲 Scan & Pay</div>", unsafe_allow_html=True)
    qr_img = get_image("qr_code")
    if qr_img: st.image(qr_img, use_container_width=True)
    st.markdown("<div class='upi-highlight'>ID: gourabsmp-1@oksbi</div></div>", unsafe_allow_html=True)
with col_bank:
    st.markdown("""<div class='donate-card' style='height: 100%;'><div class='card-header'>🏦 Bank Transfer</div>
        <ul class='bank-details-list'>
            <li><span>Account Name:</span> Gourab Singha Mahapatra</li>
            <li><span>Account No:</span> 34085907201</li>
            <li><span>IFSC Code:</span> SBIN0014054</li>
            <li><span>Bank Name:</span> State Bank of India</li>
        </ul></div>""", unsafe_allow_html=True)

# --- TRANSPARENCY ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h2 class='section-header'>Transparency</h2>", unsafe_allow_html=True)
col_rep1, col_rep2 = st.columns(2)
with col_rep1:
    p_img = get_image("prescription")
    if p_img: st.image(p_img, use_container_width=True)
with col_rep2:
    s_img = get_image("scan")
    if s_img: st.image(s_img, use_container_width=True)

# --- THE MESSAGE FORM (COLOR FIXED) ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h2 class='section-header'>Leave a Message of Support</h2>", unsafe_allow_html=True)

GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzM1DEP3J3biL5ERQTTe_dVZIpfsNg-FFmhmacy8GwhDvY584ou0EtvsjKLHQGD6koX/exec"

with st.form("support_form", clear_on_submit=True):
    donor_name = st.text_input("Your Name")
    donor_amount = st.text_input("Amount Donated (Optional)")
    donor_message = st.text_area("Your Message")
    
    submitted = st.form_submit_button("Send Message ❤️", use_container_width=True)

    if submitted:
        if donor_name and donor_message:
            try:
                data = urllib.parse.urlencode({'name': donor_name, 'amount': donor_amount, 'message': donor_message}).encode('utf-8')
                req = urllib.request.Request(GOOGLE_SCRIPT_URL, data=data)
                urllib.request.urlopen(req)
                st.success(f"Thank you, {donor_name}!")
                st.balloons()
            except: st.error("Submission failed.")
        else: st.warning("Please enter your name and message.")
