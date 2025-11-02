import streamlit as st

# ── Page Config ─────────────────────────────────────
st.set_page_config(
    page_title="Explore NeuroNexus",
    page_icon="assets/seed_1756515283.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS for Professional Look ─────────────────
st.markdown("""
<style>
    .project-card {
        padding: 1.5rem;
        border-radius: 12px;
        background: linear-gradient(135deg, #f5f7fa 0%, #e4edf5 100%);
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
        border-left: 5px solid #4361ee;
        margin-bottom: 1.2rem;
    }
    .project-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 20px rgba(67, 97, 238, 0.15);
        border-left-color: #7209b7;
    }
    .project-title {
        font-size: 1.4rem !important;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 0.5rem;
    }
    .project-desc {
        color: #475569;
        line-height: 1.6;
        margin-bottom: 0.8rem;
    }
    .badge {
        display: inline-block;
        padding: 0.35rem 0.75rem;
        border-radius: 50px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .badge-soon {
        background: #fef3c7;
        color: #d97706;
    }
    .header-gradient {
        background: linear-gradient(90deg, #4361ee 0%, #7209b7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

# ── Header ───────────────────────────────────────────
col1, col2 = st.columns([1, 6])
with col1:
    st.image("assets/seed_1756515283.png", width=80)
with col2:
    st.markdown("<h1 class='header-gradient'>Explore NeuroNexus</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b; font-size:1.1rem; margin-top:-10px;'>Discover cutting-edge AI & ML projects from GitHub, Hugging Face, and beyond.</p>", unsafe_allow_html=True)

st.divider()

# ── Search & Filters ────────────────────────────────
col1, col2 = st.columns([3, 1])
with col1:
    search = st.text_input(
        "Search for a project",
        placeholder="e.g., Stable Diffusion, BERT, RL Agent..."
    )
with col2:
    category = st.selectbox(
        "Category",
        ["All", "NLP", "Computer Vision", "Reinforcement Learning", "Tools / Frameworks"],
        index=0
    )

st.divider()

# ── Projects Data ───────────────────────────────────
projects = [
    {
        "name": "Munaf Studio",
        "desc": "AI-powered Streamlit app for hyper-realistic image generation with custom modes, aspect ratios, generative fill, and intelligent object erasure.",
        "category": "Computer Vision",
        "status": "Done",
        "link": None,
        "tech": ["Stable Diffusion", "Streamlit", "Python", "Gradio"]
    },
    {
        "name": "Movies Recommender",
        "desc": "Machine learning-powered movie recommendation engine achieving **87% accuracy** using collaborative filtering and content-based hybrid models.",
        "category": "NLP",
        "status": "In Development",
        "link": None,
        "tech": ["Scikit-learn", "Pandas", "Surprise", "Streamlit"]
    },
    {
        "name": "NeuroNexus Core",
        "desc": "The brain of this platform — an adaptive AI recommendation system that learns your coding style and suggests tools, models, and projects in real-time.",
        "category": "Tools / Frameworks",
        "status": "Active",
        "link": "https://github.com",
        "tech": ["Python", "FAISS", "LangChain", "Streamlit"]
    }
]

# ── Filter Logic ───────────────────────────────────
filtered_projects = [
    p for p in projects
    if (search.lower() in p["name"].lower() or search.lower() in p["desc"].lower())
    and (category == "All" or p["category"] == category)
]

# ── Display Projects ────────────────────────────────
st.subheader(f"Featured Projects ({len(filtered_projects)})")

if not filtered_projects:
    st.info("No projects match your search. Try adjusting filters.")
else:
    for p in filtered_projects:
        with st.container():
            st.markdown(f"""
            <div class="project-card">
                <div class="project-title">
                    {p['name']}
                    <span class="badge badge-soon" style="margin-left:10px; font-size:0.65rem;">{p['status']}</span>
                </div>
                <div class="project-desc">{p['desc']}</div>
                <div>
                    {''.join([f'<span style="background:#e0e7ff; color:#4338ca; padding:4px 10px; border-radius:12px; font-size:0.7rem; margin-right:6px; margin-bottom:4px; display:inline-block;">{t}</span>' for t in p['tech']])}
                </div>
            </div>
            """, unsafe_allow_html=True)

            col_link, col_space = st.columns([1, 4])
            with col_link:
                if p["link"]:
                    st.markdown(f"[View Project]({p['link']})")
                else:
                    st.caption("Coming soon to GitHub")

# ── Footer ──────────────────────────────────────────
st.markdown("---")
st.caption("© 2025 NeuroNexus by **Ali Munaf** • Built with ❤️ and AI")