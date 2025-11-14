import streamlit as st

st.set_page_config(page_title="TimeLens", page_icon="⌛", layout="wide")

# ---- Custom CSS ----
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #0e0f31 0%, #1c1f4a 100%);
    color: white;
}

.main-title {
    font-size: 3.2rem;
    text-align: center;
    font-weight: 800;
    background: linear-gradient(90deg, #ff8c00, #ffd700, #ff4500);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-top: 30px;
    animation: fadeIn 1.5s ease-in-out;
}

.subtitle {
    text-align: center;
    font-size: 1.2rem;
    margin-top: -10px;
    color: #dcdcdc;
    font-style: italic;
}

.description {
    text-align: center;
    font-size: 1.1rem;
    margin: 20px auto;
    color: #e8e8e8;
    width: 70%;
}

.card-container {
    display: flex;
    justify-content: center;
    gap: 40px;
    margin-top: 40px;
}

.card {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    width: 330px;
    padding: 30px;
    text-align: center;
    color: white;
    border: 1px solid rgba(255,255,255,0.2);
    transition: 0.3s ease;
    cursor: pointer;
}

.card:hover {
    transform: scale(1.05);
    box-shadow: 0px 0px 25px rgba(255, 215, 0, 0.4);
    border: 1px solid rgba(255,255,255,0.4);
}

.card-title {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 15px;
    color: #ffd700;
}

.card-desc {
    font-size: 1rem;
    color: #e0e0e0;
}

.button-link {
    margin-top: 15px;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-10px); }
    to { opacity: 1; transform: translateY(0); }
}

</style>
""", unsafe_allow_html=True)

# ---- Hero Section ----
st.markdown('<div class="main-title">TimeLens: AI-Powered Manuscript, Stone Inscription Text Extraction and Monument Exploration</div>', unsafe_allow_html=True)

st.markdown('<div class="subtitle">"Bridging centuries with a single lens — where ancient stories meet modern intelligence."</div>', unsafe_allow_html=True)

st.markdown('<div class="description">TimeLens unifies deep-learning magic with cultural heritage — enabling monument recognition, historical narration, manuscript cleaning, precision OCR, and multilingual translations. Explore the past, effortlessly.</div>', unsafe_allow_html=True)

# ---- Cards Section ----
st.markdown('<div class="card-container">', unsafe_allow_html=True)

# Card 1
card1 = f"""
<div class="card" onclick="window.location.href='https://monument-recognition1.streamlit.app/';">
    <div class="card-title">🏛️ Monument Recognition</div>
    <div class="card-desc">Upload a monument image → AI identifies it → History revealed instantly.</div>
</div>
"""

# Card 2
card2 = f"""
<div class="card" onclick="window.location.href='https://huggingface.co/spaces/premjavali05/Sanskrit_Manuscripts';">
    <div class="card-title">📜 Sanskrit Manuscripts</div>
    <div class="card-desc">Clean manuscripts, extract text, refine with Mistral, and translate into 5 languages.</div>
</div>
"""

st.markdown(card1 + card2, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
