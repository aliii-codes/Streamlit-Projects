import streamlit as st


st.set_page_config(
    page_title="Recommendations - NeuroNexus",
    page_icon="assets/seed_1756515283.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS (consistent with Explore page)
st.markdown("""
<style>
    .rec-card {
        padding: 1.5rem;
        border-radius: 12px;
        background: linear-gradient(135deg, #fdf4ff 0%, #e0e7ff 100%);
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
        border-left: 5px solid #a855f7;
        margin-bottom: 1.2rem;
    }
    .rec-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 20px rgba(168, 85, 247, 0.15);
        border-left-color: #ec4899;
    }
    .rec-title {
        font-size: 1.35rem !important;
        font-weight: 600;
        color: #1e1b4b;
        margin-bottom: 0.4rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .rec-desc {
        color: #5b21b6;
        line-height: 1.6;
        margin-bottom: 0.8rem;
    }
    .stButton > button {
        border-radius: 8px !important;
    }
    .interest saved {
        background: #f0fdf4 !important;
        color: #166534 !important;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Header
# -------------------------------------------------
col1, col2 = st.columns([1, 6])
with col1:
    st.image("assets/seed_1756515283.png", width=80)
with col2:
    st.markdown("<h1 style='background: linear-gradient(90deg, #a855f7, #ec4899); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight:700;'>Your AI Recommendations</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b; font-size:1.1rem; margin-top:-10px;'>Tailored project suggestions based on your interests and activity.</p>", unsafe_allow_html=True)

st.divider()

# -------------------------------------------------
# Initialize interest tracking in session_state
# -------------------------------------------------
if "interests" not in st.session_state:
    st.session_state.interests = []

# -------------------------------------------------
# Recommended Projects
# -------------------------------------------------
recommendations = [
    {
        "name": "AI Chatbot",
        "emoji": "Chatbot",
        "desc": "A powerful chatbot powered by Transformers and fine-tuned on real conversations.",
        "link": "https://github.com/ai-collection/chatbot",
        "tags": ["NLP", "Transformers", "Gradio"]
    },
    {
        "name": "Image Classifier",
        "emoji": "Image",
        "desc": "Train and deploy CNNs to classify images with PyTorch — includes transfer learning.",
        "link": "https://github.com/pytorch/examples",
        "tags": ["Computer Vision", "PyTorch", "CNN"]
    },
    {
        "name": "Music Generator",
        "emoji": "Music",
        "desc": "Generate original music using Magenta’s RNN models — AI creativity unleashed.",
        "link": "https://github.com/magenta/magenta",
        "tags": ["Audio", "RNN", "Creative AI"]
    },
    {
        "name": "CodeSnap",
        "emoji": "Camera",
        "desc": "Snap a photo of a hand-drawn flowchart → get clean, executable Python/JS code instantly.",
        "link": None,
        "tags": ["Vision", "OCR", "Automation"]
    }
]

# -------------------------------------------------
# Display Recommendations
# -------------------------------------------------
st.subheader(f"Top Picks for You ({len(recommendations)})")

for rec in recommendations:
    with st.container():
        st.markdown(f"""
        <div class="rec-card">
            <div class="rec-title">
                {rec['emoji']} {rec['name']}
            </div>
            <div class="rec-desc">{rec['desc']}</div>
            <div>
                {''.join(f'<span style="background:#e9d5ff; color:#7c3aed; padding:3px 9px; border-radius:12px; font-size:0.7rem; margin-right:5px; display:inline-block;">{t}</span>' for t in rec['tags'])}
            </div>
        </div>
        """, unsafe_allow_html=True)

        col_btn, col_check = st.columns([1, 1.2])

        with col_btn:
            if rec["link"]:
                st.markdown(f"[View on GitHub]({rec['link']})")
            else:
                st.caption("Coming soon")

        with col_check:
            key = f"interest_{rec['name']}"
            interested = st.checkbox(
                "I'm Interested!",
                value=(rec["name"] in st.session_state.interests),
                key=key
            )
            if interested and rec["name"] not in st.session_state.interests:
                st.session_state.interests.append(rec["name"])
                st.success(f"Added **{rec['name']}** to your interests!")
            elif not interested and rec["name"] in st.session_state.interests:
                st.session_state.interests.remove(rec["name"])

        st.markdown("---")

# -------------------------------------------------
# Show User's Interest Summary
# -------------------------------------------------
if st.session_state.interests:
    st.divider()
    st.subheader("Your Interests")
    for interest in st.session_state.interests:
        st.markdown(f"- **{interest}**")

# -------------------------------------------------
# Footer
# -------------------------------------------------
st.markdown("---")
st.caption("© 2025 NeuroNexus by **Ali Munaf** • Powered by curiosity and code")