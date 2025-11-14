import streamlit as st

st.set_page_config(page_title="TimeLens", page_icon="⌛", layout="wide")

# ---------- CLEAN MINIMAL PORTFOLIO CSS ----------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Marcellus&family=Cinzel:wght@600;700&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background-color: #f5efe3; /* soft parchment color */
}

.big-title {
    font-family: 'Cinzel', serif;
    font-size: 3.2rem;
    text-align: center;
    font-weight: 700;
    background: linear-gradient(90deg, #a87b00, #e6c35a);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-top: 30px;
}

.subtitle {
    text-align: center;
    font-size: 1.2rem;
    color: #6e6137;
    font-style: italic;
    margin-top: -12px;
}

.description {
    text-align: center;
    font-size: 1.1rem;
    color: #4c3f2f;
    width: 70%;
    margin: 20px auto;
}

.card-container {
    display: flex;
    justify-content: center;
    gap: 40px;
    margin-top: 40px;
}

.card {
    background: #ffffff;
    border-radius: 16px;
    padding: 25px;
    width: 320px;
    text-align: center;
    border: 2px solid #e6d8b4;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    transition: 0.3s ease;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.25);
}

.card-title {
    font-family: 'Cinzel', serif;
    font-size: 1.5rem;
    font-weight: 600;
    color: #a87b00;
    margin-bottom: 10px;
}

.card-desc {
    font-size: 1rem;
    color: #5a4a32;
    margin-bottom: 20px;
}

.button-custom {
    background: linear-gradient(90deg, #a87b00, #e6c35a);
    color: white !important;
    padding: 10px 18px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
}

.button-custom:hover {
    background: linear-gradient(90deg, #e6c35a, #a87b00);
}

</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown('<div class="big-title">TimeLens: AI-Powered Manuscript, Stone Inscription Text Extraction & Monument Exploration</div>', unsafe_allow_html=True)

# ---------- SUBTITLE ----------
st.markdown('<div class="subtitle">“Where ancient worlds whisper, and AI listens.”</div>', unsafe_allow_html=True)

# ---------- DESCRIPTION ----------
st.markdown('<div class="description">TimeLens merges advanced AI with cultural heritage — identify monuments from images, explore history, clean Sanskrit manuscripts, extract inscriptions, and translate text across five languages.</div>', unsafe_allow_html=True)

# ---------- CARDS ----------
st.markdown('<div class="card-container">', unsafe_allow_html=True)

# Card 1
st.markdown("""
<div class="card">
    <div class="card-title">🏛️ Monument Recognition</div>
    <div class="card-desc">Upload a monument image, let TimeLens identify it, and explore its rich history.</div>
    <a class="button-custom" href="https://monument-recognition1.streamlit.app/" target="_self">
        Explore
    </a>
</div>
""", unsafe_allow_html=True)

# Card 2
st.markdown("""
<div class="card">
    <div class="card-title">📜 Sanskrit Manuscripts</div>
    <div class="card-desc">Clean manuscripts, extract text, refine with AI, and translate into five languages.</div>
    <a class="button-custom" href="https://huggingface.co/spaces/premjavali05/Sanskrit_Manuscripts" target="_self">
        Open Workspace
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
