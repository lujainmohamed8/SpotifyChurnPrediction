import streamlit as st
import joblib
import pandas as pd
import time
import base64

# ================= LOAD MODEL =================
try:
    model = joblib.load("spotify_churn_random_forest.pkl")
except:
    st.error("Model file not found.")

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Spotify Analytics",
    page_icon="🎵",
    layout="wide"
)

# ================= AUDIO HELPER =================
def play_sound():
    # Using a clean, short notification sound
    sound_url = "https://www.soundjay.com/buttons/sounds/button-37a.mp3"
    html_string = f"""
        <audio autoplay style="display:none;">
            <source src="{sound_url}" type="audio/mp3">
        </audio>
    """
    st.components.v1.html(html_string, height=0)

# ================= CSS =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;800;900&display=swap');

html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
    background: linear-gradient(180deg, #1e1e1e 0%, #121212 40%, #121212 100%) !important;
    color: #FFFFFF;
    font-family: 'Montserrat', sans-serif;
    overflow: hidden !important; 
    height: 100vh !important;
}

.block-container {
    padding: 2rem 5rem !important;
    max-width: 1300px !important;
}

.header-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 15px;
    margin-bottom: 2.5rem;
}

.spotify-title {
    color: #FFFFFF;
    font-size: 40px;
    font-weight: 800;
    letter-spacing: -1.5px;
    margin: 0;
}

h3 {
    font-size: 0.85rem !important;
    color: #FFFFFF !important;
    margin-bottom: 1.5rem !important;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 2px;
    border-left: 4px solid #1DB954; 
    padding-left: 35px !important; 
    line-height: 1;
}

/* SCANNING ANIMATION */
.scan-container {
    width: 100%;
    height: 180px;
    background: #181818;
    border-radius: 12px;
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
}

.scan-bar {
    width: 100%;
    height: 4px;
    background: #1DB954;
    position: absolute;
    top: 0;
    left: 0;
    box-shadow: 0 0 15px #1DB954;
    animation: scan 1.5s linear infinite;
}

.scan-text {
    color: #1DB954;
    font-weight: 700;
    font-size: 0.8rem;
    letter-spacing: 2px;
    animation: pulse 1s ease-in-out infinite;
}

@keyframes scan {
    0% { top: 0; }
    100% { top: 100%; }
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
}

.stSelectbox > div > div {
    background: #282828 !important;
    border: none !important;
    border-radius: 4px !important;
    color: white !important;
}

.stButton>button#calc_btn {
    background-color: #1DB954 !important;
    color: white !important;
    font-weight: 700;
    border-radius: 500px;
    padding: 12px 30px;
    width: 100%;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: 0.8rem;
    border: none;
    transition: 0.2s ease-in-out;
}

.stButton>button#calc_btn:hover {
    background-color: #1ed760 !important;
    transform: scale(1.03);
}

.result-container {
    background: #181818;
    border-radius: 12px;
    padding: 2rem;
    text-align: center;
    border: 1px solid #282828;
    margin-top: 15px;
    height: 180px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.probability-number {
    font-size: 3.5rem;
    font-weight: 800;
    letter-spacing: -3px;
    line-height: 1;
}

#MainMenu, footer, header {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("""
<div class="header-wrapper">
    <img src="https://upload.wikimedia.org/wikipedia/commons/1/19/Spotify_logo_without_text.svg" width="48">
    <h1 class="spotify-title">Churn Predictor</h1>
</div>
""", unsafe_allow_html=True)

# ================= 3-COLUMN LAYOUT =================
col1, col2, col3 = st.columns([1, 1, 1], gap="large")

with col1:
    st.markdown("### Engagement")
    listening_time = st.slider("Listening Time (min/day)", 0, 500, 150, key="listen")
    songs_played = st.slider("Songs Played (daily)", 0, 100, 30, key="songs")
    skip_rate = st.slider("Skip Rate", 0.0, 1.0, 0.35, key="skip")
    ads = st.slider("Ads per Week", 0, 100, 20, key="ads")

with col2:
    st.markdown("### User Profile")
    subscription = st.selectbox("Subscription Plan", ["Free", "Premium", "Student", "Family"], key="sub")
    device = st.selectbox("Primary Device", ["Mobile", "Desktop", "Web"], key="device")
    offline = st.selectbox("Offline Listening", [0,1], format_func=lambda x: "Enabled" if x==1 else "Disabled", key="offline")
    st.markdown("<div style='height:45px'></div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;font-size:0.6rem;color:#444;letter-spacing:1px;opacity:0.5;'>AI MODEL: RANDOM FOREST v2.0</p>", unsafe_allow_html=True)

with col3:
    st.markdown("### Prediction")
    
    input_data = pd.DataFrame([{
        "listening_time": listening_time, "songs_played_per_day": songs_played,
        "skip_rate": skip_rate, "ads_listened_per_week": ads,
        "offline_listening": offline, "subscription_type": subscription,
        "device_type": device, "EngagementScore": listening_time + songs_played,
        "AdsEngagement": ads / (listening_time + 1), "PremiumMobile": int(subscription == "Premium" and device=="Mobile")
    }])

    run_btn = st.button("Calculate", key="calc_btn")
    placeholder = st.empty()

    if run_btn:
        # Show Animation
        placeholder.markdown("""
            <div class="scan-container">
                <div class="scan-bar"></div>
                <div class="scan-text">SCANNING USER BEHAVIOR...</div>
            </div>
        """, unsafe_allow_html=True)
        
        time.sleep(1.8) # Delay for the animation
        
        # Result Reveal
        try:
            prob = model.predict_proba(input_data)[0][1]
            color = "#1DB954" if prob < 0.4 else "#fbbf24" if prob < 0.7 else "#f87171"
            status = "STABLE" if prob < 0.4 else "MODERATE" if prob < 0.7 else "AT RISK"

            # PLAY SOUND HERE
            play_sound()

            placeholder.markdown(f"""
            <div class="result-container">
                <p style="color:#B3B3B3; font-size:0.65rem; font-weight:700; letter-spacing:2px; margin-bottom:5px;">PROBABILITY</p>
                <div class="probability-number" style="color:{color}">{prob:.1%}</div>
                <p style="color:{color}; font-weight:700; margin-top:10px; font-size:1.1rem; letter-spacing:2px;">{status}</p>
            </div>
            """, unsafe_allow_html=True)
        except:
            st.error("Error")
    else:
        placeholder.markdown("""
        <div class="result-container" style="opacity:0.2;">
            <p style="font-size:0.8rem;">Adjust parameters and calculate</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<p style='position: fixed; bottom: 15px; width: 100%; text-align: center; color: #444; font-size: 0.65rem; font-weight:700; letter-spacing:1px; opacity:0.6;'>SPOTIFY DATA SCIENCE • INTERNAL DASHBOARD</p>", unsafe_allow_html=True)