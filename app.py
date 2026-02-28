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

# --- PREMIUM CROWDFUNDING CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');

    .stApp {
        background-color: #f4f7f9;
        color: #2b3a42;
        font-family: 'Inter', sans-serif;
    }
    
    /* Headers */
    .hero-title {
        color: #1a252f;
        text-align: center;
        font-size: 3em;
        font-weight: 800;
        margin-bottom: 5px;
        line-height: 1.2;
        letter-spacing: -0.5px;
    }
    .hero-subtitle {
        text-align: center;
        color: #7f8c8d;
        font-size: 1.3em;
        margin-bottom: 35px;
        font-weight: 400;
    }

    /* Target & Progress Section */
    .campaign-stats-container {
        background-color: #ffffff;
        padding: 35px;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.06);
        margin-bottom: 40px;
        border-top: 6px solid #10b981; /* Trustworthy Green */
    }
    .stats-flex {
        display: flex;
        justify-content: space-between;
        margin-bottom: 15px;
    }
    .stat-box {
        text-align: left;
    }
    .stat-label {
        font-size: 1em;
        color: #7f8c8d;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .stat-value {
        font-size: 2.2em;
        font-weight: 800;
        color: #1a252f;
        margin-top: 5px;
    }
    .stat-value.target {
        color: #95a5a6;
        font-size: 1.6em;
        margin-top: 12px;
    }
    
    /* Custom Thick Progress Bar */
    .custom-progress-bg {
        background-color: #e2e8f0;
        border-radius: 20px;
        height: 24px;
        width: 100%;
        overflow: hidden;
        margin-bottom: 10px;
    }
    .custom-progress-fill {
        background: linear-gradient(90deg, #10b981, #34d399);
        height: 100%;
        border-radius: 20px;
        transition: width 1s ease-in-out;
    }
    
    /* The Story Box */
    .story-card {
        background-color: #ffffff;
        padding: 45px;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.04);
        line-height: 1.8;
        font-size: 1.15em;
        margin-bottom: 40px;
        color: #34495e;
    }
    .story-card h3 {
        color: #1a252f;
        font-weight: 700;
        font-size: 1.6em;
        margin-bottom: 20px;
        border-bottom: 2px solid #f0f2f5;
        padding-bottom: 10px;
    }
    
    /* Donation Cards */
    .donate-grid {
        display: flex;
        gap: 20px;
        margin-bottom: 40px;
    }
    .donate-card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.05);
        border: 1px solid #e2e8f0;
        flex: 1;
        transition: transform 0.2s ease;
    }
    .donate-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.08);
        border-color: #3b82f6; /* Highlight Blue */
    }
    .card-header {
        font-weight: 700;
        font-size: 1.3em;
        color: #1a252f;
        margin-bottom: 20px;
        text-align: center;
        padding-bottom: 15px;
        border-bottom: 1px solid #e2e8f0;
    }
    .bank-details-list {
        list-style: none;
        padding: 0;
        margin: 0;
        color: #34495e;
        font-size: 1.1em;
        line-height: 1.9;
    }
    .bank-details-list li span {
        font-weight: 700;
        color: #1a252f;
        display: inline-block;
        width: 140px;
    }
    .upi-highlight {
        background-color: #eff6ff;
        color: #1e3a8a;
        padding: 10px 15px;
        border-radius: 8px;
        font-weight: 700;
        text-align: center;
        font-size: 1.2em;
        margin-top: 15px;
        border: 1px dashed #93c5fd;
    }

    .section-header {
        text-align: center; 
        color: #1a252f; 
        font-size: 2.2em;
        font-weight: 800;
        margin-bottom: 30px;
    }
    
    .caption-text {
        text-align: center; 
        color: #7f8c8d; 
        font-size: 0.9em;
        font-style: italic;
        margin-top: 10px;
    }
    
    hr { border: 0; height: 1px; background: #cbd5e1; margin: 50px 0; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1 class='hero-title'>Support My Father's Treatment</h1>", unsafe_allow_html=True)
st.markdown("<p class='hero-subtitle'>Medical Fundraiser for Samir Singha Mahapatra</p>", unsafe_allow_html=True)

# --- FATHER'S PHOTO ---
father_img = get_image("father")
if father_img:
    col_img1, col_img2, col_img3 = st.columns([1, 2, 1])
    with col_img2:
        st.image(father_img, use_container_width=True)
        st.markdown("<p class='caption-text'>My Father, Samir Singha Mahapatra</p>", unsafe_allow_html=True)

# --- NEW: HIGH-IMPACT FUNDRAISING PROGRESS ---
target_amount = 1200000 # 12 Lakhs
raised_amount = 25000   # Amount currently raised
progress_percent = min((raised_amount / target_amount) * 100, 100)
display_percent = max(progress_percent, 2) # Ensures the green bar is at least slightly visible even at 1%

st.markdown(f"""
<div class='campaign-stats-container'>
    <div class='stats-flex'>
        <div class='stat-box'>
            <div class='stat-label'>Amount Raised</div>
            <div class='stat-value'>₹{raised_amount:,}</div>
        </div>
        <div class='stat-box' style='text-align: right;'>
            <div class='stat-label'>Target Goal</div>
            <div class='stat-value target'>₹{target_amount:,}</div>
        </div>
    </div>
    <div class='custom-progress-bg'>
        <div class='custom-progress-fill' style='width: {display_percent}%;'></div>
    </div>
    <div style='text-align: right; color: #7f8c8d; font-size: 0.9em; margin-top: 8px; font-weight: 600;'>
        {progress_percent:.1f}% Funded
    </div>
</div>
""", unsafe_allow_html=True)


# --- THE STORY ---
st.markdown("""
<div class='story-card'>
    <h3>Our Challenge</h3>
    <p>I am writing to share a personal challenge my family is currently facing. My father, <b>Samir Singha Mahapatra</b>, was recently diagnosed with Stage 1 cancer.</p>
    <p>We are entirely focused on his treatment and recovery, but the financial requirement for his comprehensive care is approximately <b>10–12 lakhs</b>.</p>
    <p>I have always valued the strength of our community, and I am humbly asking for your support during this time. Any contribution toward his treatment fund would significantly ease the burden on my family as we navigate this journey together.</p>
    <p>Thank you for your thoughts, prayers, and generosity.</p>
    <p style='margin-top: 25px; font-size: 1.1em;'><b>— Gourab Singha Mahapatra</b></p>
</div>
""", unsafe_allow_html=True)


# --- HOW TO DONATE (PREMIUM CARDS) ---
st.markdown("<h2 class='section-header'>How to Contribute</h2>", unsafe_allow_html=True)

col_qr, col_bank = st.columns([1, 1.3])

with col_qr:
    st.markdown("""
    <div class='donate-card'>
        <div class='card-header'>📲 Scan & Pay (UPI)</div>
    """, unsafe_allow_html=True)
    
    qr_img = get_image("qr_code")
    if qr_img:
        st.image(qr_img, use_container_width=True)
    else:
        st.info("QR Code will appear here.")
        
    st.markdown("""
        <div class='upi-highlight'>ID: gourabsmp-1@oksbi</div>
        <p style='text-align: center; color: #7f8c8d; margin-top: 10px; font-size: 0.9em;'>GPay / PhonePe / Paytm</p>
    </div>
    """, unsafe_allow_html=True)

with col_bank:
    st.markdown("""
    <div class='donate-card' style='height: 100%;'>
        <div class='card-header'>🏦 Direct Bank Transfer</div>
        <ul class='bank-details-list'>
            <li><span>Account Name:</span> Gourab Singha Mahapatra</li>
            <li><span>Account No:</span> 34085907201</li>
            <li><span>IFSC Code:</span> SBIN0014054</li>
            <li><span>Bank Name:</span> State Bank of India</li>
        </ul>
        <div style='margin-top: 30px; padding-top: 20px; border-top: 1px dashed #e2e8f0;'>
            <ul class='bank-details-list'>
                <li><span>Google Pay (No):</span> 9749168189</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)


# --- TRANSPARENCY & MEDICAL DOCUMENTS ---
st.markdown("<h2 class='section-header'>Medical Transparency</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #7f8c8d; margin-bottom: 35px; font-size: 1.1em;'>Official medical records from Disha Eye Hospitals.</p>", unsafe_allow_html=True)

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
st.markdown("<p style='text-align: center; color: #95a5a6; font-size: 1.1em;'>For any queries or updates, please reach out to me directly.</p>", unsafe_allow_html=True)
