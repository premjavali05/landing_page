import streamlit as st

st.set_page_config(page_title="TimeLens", page_icon="⌛", layout="wide")

# ---------- CSS SECTION ----------
page_bg = """
<style>

@import url('https://fonts.googleapis.com/css2?family=Marcellus&family=Cinzel:wght@600;700&display=swap');

body {
    font-family: 'Marcellus', serif;
}

[data-testid="stAppViewContainer"] {
    background-image: url("https://i.ibb.co/5x1nMdc/parchment-bg.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    color: #fff;
}

.big-title {
    font-family: 'Cinzel', serif;
    font-size: 3.5rem;
    text-align: center;
    font-weight: 700;
    background: linear-gradient(90deg, #d4af37, #f6e27f, #c9a340);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-top: 20px;
    text-shadow: 0px 0px 8px rgba(255,255,255,0.4);
}

.subtitle {
    text-align: center;
    font-size: 1.3rem;
    color: #f0e6c8;
    margin-top: -10px;
    font-style: italic;
}

.description {
    text-align: center;
    font-size: 1.15rem;
    width: 70%;
    margin: 15px auto;
    color: #f9f4df;
}

.card-wrapper {
    display: flex;
    justify-content: center;
    gap: 50px;
    margin-top: 50px;
}

.card {
    background: rgba(0,0,0,0.45);
    padding: 30px 25px;
    border-radius: 18px;
    width: 330px;
    text-align: center;
    border: 2px solid rgba(212,175,55,0.7);
    box-shadow: 0px 0px 15px rgba(212,175,55,0.4);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 0px 22px rgba(255,215,0,0.7);
}

.card-title {
    font-family: 'Cinzel', serif;
    font-size: 1.6rem;
    color: #ffd76a;
    font-weight: 600;
    margin-bottom: 12px;
}

.card-desc {
    font-size: 1rem;
    color: #f2e9d8;
    margin-bottom: 20px;
}

.stButton>button {
    background: linear-gradient(90deg, #d4af37, #f6e27f);
    color: black !important;
    font-weight: 600;
    border: none;
    border-radius: 10px;
    padding: 10px 18px;
    cursor: pointer;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #f6e27f, #d4af37);
    transform: scale(1.05);
}

</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown('<div class="big-title">TimeLens: AI-Powered Manuscript, Stone Inscription Text Extraction & Monument Exploration</div>', unsafe_allow_html=True)

# ---------- SUBTITLE ----------
st.markdown('<div class="subtitle">“Where ancient worlds whisper, and AI listens.”</div>', unsafe_allow_html=True)

# ---------- DESCRIPTION ----------
st.markdown('<div class="description">TimeLens merges advanced AI with cultural heritage — identify monuments using images, explore history, clean Sanskrit manuscripts, extract inscriptions, and translate text across five languages.</div>', unsafe_allow_html=True)


# ---------- CARD SECTION ----------
st.markdown('<div class="card-wrapper">', unsafe_allow_html=True)

# Use Streamlit columns for PERFECT centered alignment
col1, col2 = st.columns([1,1], gap="large")

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">🏛️ Monument Recognition</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-desc">Upload a monument image → TimeLens identifies it → Learn its story instantly.</div>', unsafe_allow_html=True)

    if st.button("Explore"):
        st.switch_page("https://monument-recognition1.streamlit.app/")

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">📜 Sanskrit Manuscripts</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-desc">Restore manuscripts, extract text, refine with AI, and translate into 5 languages.</div>', unsafe_allow_html=True)

    if st.button("Open Workspace"):
        st.switch_page("https://huggingface.co/spaces/premjavali05/Sanskrit_Manuscripts")

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
