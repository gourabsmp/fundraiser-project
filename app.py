import streamlit as st
import os

# --- BULLETPROOF IMAGE FINDER ---
def get_image(base_name):
    for ext in ['.jpg', '.jpeg', '.JPG', '.JPEG', '.png', '.PNG']:
        if os.path.exists(base_name + ext):
            return base_name + ext
    return None

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Fundraiser: Help Samir Singha Mahapatra", page_icon="🤍", layout="centered")

# --- CLEAN, TRUSTWORTHY MEDICAL CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    .stApp {
        background-color: #f8f9fa;
        color: #2b3a42;
        font-family: 'Inter', sans-serif;
    }
    
    .main-title {
        color: #1a252f;
        text-align: center;
        font-size: 2.8em;
        font-weight: 700;
        margin-bottom: 5px;
        line-height: 1.2;
    }
    .sub-title {
        text-align: center;
        color: #7f8c8d;
        font-size: 1.2em;
        margin-bottom: 30px;
        font-weight: 400;
    }
    
    .progress-box {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 30px;
        border-top: 5px solid #2ecc71; /* Medical/Hopeful Green */
        text-align: center;
    }
    .stats-text {
        font-size: 1.6em;
        font-weight: 700;
        color: #2c3e50;
    }

    .story-box {
        background-color: #ffffff;
        padding: 40px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        line-height: 1.8;
        font-size: 1.15em;
        margin-bottom: 40px;
        color: #34495e;
        border-left: 5px solid #3498db;
    }
    
    .payment-container {
        background-color: #ffffff;
        padding: 40px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 40px;
        border: 1px solid #e1e8ed;
    }
    
    .bank-details {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 8px;
        border-left: 4px solid #f1c40f;
        font-size: 1.1em;
        color: #2c3e50;
        line-height: 1.6;
    }

    .section-header {
        text-align: center; 
        color: #2c3e50; 
        font-size: 2em;
        font-weight: 700;
        margin-bottom: 25px;
    }
    
    .caption-text {
        text-align: center; 
        color: #7f8c8d; 
        font-size: 0.9em;
        font-style: italic;
        margin-top: 8px;
    }
    
    hr {
        border: 0;
        height: 1px;
        background: #e1e8ed;
        margin: 40px 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1 class='main-title'>Support My Father's Fight Against Cancer</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Medical Fundraiser for Samir Singha Mahapatra</p>", unsafe_allow_html=True)

# --- FATHER'S PHOTO (Optional - Will display if father.jpeg is uploaded) ---
father_img = get_image("father")
if father_img:
    col_img1, col_img2, col_img3 = st.columns([1, 2, 1])
    with col_img2:
        st.image(father_img, use_container_width=True)
        st.markdown("<p class='caption-text'>My Father, Samir Singha Mahapatra</p>", unsafe_allow_html=True)

# --- FUNDRAISING PROGRESS ---
target_amount = 1200000 # 12 Lakhs
raised_amount = 25000   # The amount already raised by the committee
progress_percent = min(int((raised_amount / target_amount) * 100), 100)

st.markdown(f"""
<div class='progress-box'>
    <div class='stats-text'>₹{raised_amount:,} raised of ₹{target_amount:,} goal</div>
    <p style='color: #7f8c8d; margin-top: 5px; font-weight: 600;'>{progress_percent}% funded</p>
</div>
""", unsafe_allow_html=True)

st.progress(progress_percent / 100.0)

# --- THE STORY ---
st.markdown("""
<div class='story-box'>
    <h3 style='color: #2c3e50; margin-bottom: 15px; font-weight: 700;'>Our Challenge</h3>
    <p>I am writing to share a personal challenge my family is currently facing. My father, <b>Samir Singha Mahapatra</b>, was recently diagnosed with Stage 1 cancer.</p>
    <p>We are entirely focused on his treatment and recovery, but the financial requirement for his comprehensive care is approximately 10–12 lakhs.</p>
    <p>I have always valued the strength of our community, and I am humbly asking for your support during this time. Any contribution toward his treatment fund would significantly ease the burden on my family as we navigate this journey together.</p>
    <p>Thank you for your thoughts, prayers, and generosity.</p>
    <p style='margin-top: 20px;'><b>— Gourab Singha Mahapatra</b></p>
</div>
""", unsafe_allow_html=True)

# --- HOW TO DONATE ---
st.markdown("<h2 class='section-header'>How to Contribute</h2>", unsafe_allow_html=True)

st.markdown("<div class='payment-container'>", unsafe_allow_html=True)
col_qr, col_bank = st.columns([1, 1.2])

with col_qr:
    st.markdown("<h4 style='text-align: center; color: #2c3e50;'>Scan to Pay (UPI)</h4>", unsafe_allow_html=True)
    qr_img = get_image("qr_code")
    if qr_img:
        st.image(qr_img, use_container_width=True)
    else:
        st.info("QR Code will appear here.")
    st.markdown("<p style='text-align: center; font-weight: 600; color: #34495e; font-size: 1.1em;'>UPI ID: gourabsmp-1@oksbi</p>", unsafe_allow_html=True)

with col_bank:
    st.markdown("<h4 style='color: #2c3e50; margin-bottom: 15px;'>Direct Bank Transfer</h4>", unsafe_allow_html=True)
    st.markdown("""
    <div class='bank-details'>
        <b>Account Name:</b> Gourab Singha Mahapatra<br>
        <b>Account No:</b> 34085907201<br>
        <b>IFSC Code:</b> SBINOO14054<br>
        <b>Bank Name:</b> State Bank of India<br><br>
        <b>Google Pay (GPay) No:</b> 9749168189
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- TRANSPARENCY & MEDICAL DOCUMENTS ---
st.markdown("<h2 class='section-header'>Medical Transparency</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #7f8c8d; margin-bottom: 30px;'>Official medical records from Disha Eye Hospitals.</p>", unsafe_allow_html=True)

col_rep1, col_rep2 = st.columns(2)
with col_rep1:
    prescription_img = get_image("prescription")
    if prescription_img:
        st.image(prescription_img, use_container_width=True)
        st.markdown("<p class='caption-text'>Medical Prescription & Plan</p>", unsafe_allow_html=True)
with col_rep2:
    scan_img = get_image("scan")
    if scan_img:
        st.image(scan_img, use_container_width=True)
        st.markdown("<p class='caption-text'>Initial Medical Scan</p>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #95a5a6;'>For any queries or updates, please reach out to me directly.</p>", unsafe_allow_html=True)
