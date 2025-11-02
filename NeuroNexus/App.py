import streamlit as st

# -------------------------------------------------
# Page configuration
# -------------------------------------------------
st.set_page_config(
    page_title="NeuroNexus",
    page_icon="assets/seed_1756515283.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------------------------------------
# Custom CSS (professional look for the Explore cards)
# -------------------------------------------------
st.markdown(
    """
<style>
    .project-card{
        padding:1.5rem;
        border-radius:12px;
        background:linear-gradient(135deg,#f5f7fa 0%,#e4edf5 100%);
        box-shadow:0 4px 12px rgba(0,0,0,.05);
        transition:all .3s ease;
        border-left:5px solid #4361ee;
        margin-bottom:1.2rem;
    }
    .project-card:hover{
        transform:translateY(-4px);
        box-shadow:0 8px 20px rgba(67,97,238,.15);
        border-left-color:#7209b7;
    }
    .project-title{font-size:1.4rem;font-weight:600;color:#1e293b;margin-bottom:.5rem}
    .project-desc{color:#475569;line-height:1.6;margin-bottom:.8rem}
    .badge{
        display:inline-block;padding:.35rem .75rem;border-radius:50px;
        font-size:.75rem;font-weight:600;text-transform:uppercase;letter-spacing:.5px;
    }
    .badge-soon{background:#fef3c7;color:#d97706}
    .header-gradient{
        background:linear-gradient(90deg,#4361ee 0%,#7209b7 100%);
        -webkit-background-clip:text;-webkit-text-fill-color:transparent;
        background-clip:text;font-weight:700;
    }
</style>
""",
    unsafe_allow_html=True,
)

# -------------------------------------------------
# Header (top of every page)
# -------------------------------------------------
col_logo, col_title = st.columns([1, 6])
with col_logo:
    st.image("assets/seed_1756515283.png", width=80)
with col_title:
    st.markdown(
        "<h1 class='header-gradient'>NeuroNexus</h1>", unsafe_allow_html=True
    )
    st.markdown(
        "<p style='color:#64748b;font-size:1.1rem;margin-top:-10px;'>Your AI-powered project discovery hub</p>",
        unsafe_allow_html=True,
    )

# -------------------------------------------------
# Sidebar (logo + navigation)
# -------------------------------------------------
st.sidebar.image("assets/seed_1756515283.png", width=150)
st.sidebar.title("NeuroNexus")

# -------------------------------------------------
# Session-state page handling
# -------------------------------------------------
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# -------------------------------------------------
# Home page content (with button)
# -------------------------------------------------
if st.session_state.current_page == "Home":
    # st.markdown("## Hi!")
    st.write(
        "NeuroNexus is your **personal AI-powered recommendation hub**.\n"
        "It learns your interests and suggests projects, tools, and ideas you’ll actually love."
    )
    st.subheader("Features")
    st.write("- **AI-Powered Recommendations** – Personalized ML suggestions.")
    st.write("- **Explore Projects** – Discover trending GitHub & Hugging Face tools.")
    st.write("- **Smart Tracking** – Learns what you like over time.")
    st.divider()
    st.write("Ready to explore the world of AI?")

    if st.button("Start Exploring", type="primary"):
        st.session_state.current_page = "Explore"
        st.rerun()

# -------------------------------------------------
# Sidebar navigation (AFTER Home button logic)
# -------------------------------------------------
page_options = ["Home", "Explore", "Recommendations", "Profile"]
page = st.sidebar.radio(
    "Navigate",
    page_options,
    index=page_options.index(st.session_state.current_page),
    key="nav_radio",
)

# Keep session_state in sync with the radio
st.session_state.current_page = page

# -------------------------------------------------
# Page routing
# -------------------------------------------------
if st.session_state.current_page == "Home":
    # Home already rendered above – nothing more to do
    pass

elif st.session_state.current_page == "Explore":
    # ---- Professional Explore page (your code, polished) ----
    st.markdown("## Explore Projects By Ali")
    st.write(
        "Discover cutting-edge AI & ML projects from GitHub, Hugging Face, and beyond."
    )
    st.divider()

    # Search + filter
    col1, col2 = st.columns([3, 1])
    with col1:
        search = st.text_input(
            "Search for a project",
            placeholder="e.g., Stable Diffusion, BERT, RL Agent...",
        )
    with col2:
        category = st.selectbox(
            "Category",
            ["All", "NLP", "Computer Vision", "Reinforcement Learning", "Tools / Frameworks"],
        )

    st.divider()

    # ---- Project data -------------------------------------------------
    projects = [
        {
            "name": "Munaf Studio",
            "desc": "AI-powered Streamlit app for hyper-realistic image generation with custom modes, aspect ratios, generative fill, and intelligent object erasure.",
            "category": "Computer Vision",
            "status": "In Development",
            "link": None,
            "tech": ["Stable Diffusion", "Streamlit", "Python", "Gradio"],
        },
        {
            "name": "Movies Recommender",
            "desc": "Machine learning-powered movie recommendation engine achieving **87% accuracy** using collaborative filtering and content-based hybrid models.",
            "category": "NLP",
            "status": "In Development",
            "link": None,
            "tech": ["Scikit-learn", "Pandas", "Surprise", "Streamlit"],
        },
        {
            "name": "NeuroNexus Core",
            "desc": "Adaptive AI recommendation engine that learns your coding style and suggests tools, models, and projects in real-time.",
            "category": "Tools / Frameworks",
            "status": "Active",
            "link": "https://github.com",
            "tech": ["Python", "FAISS", "LangChain", "Streamlit"],
        },
    ]

    # ---- Filtering ----------------------------------------------------
    filtered = [
        p
        for p in projects
        if (search.lower() in p["name"].lower() or search.lower() in p["desc"].lower())
        and (category == "All" or p["category"] == category)
    ]

    st.subheader(f"Featured Projects ({len(filtered)})")

    if not filtered:
        st.info("No projects match your search. Try adjusting the filters.")
    else:
        for p in filtered:
            st.markdown(
                f"""
                <div class="project-card">
                    <div class="project-title">
                        {p['name']}
                        <span class="badge badge-soon" style="margin-left:10px;font-size:0.65rem;">{p['status']}</span>
                    </div>
                    <div class="project-desc">{p['desc']}</div>
                    <div>
                        {''.join(
                            f'<span style="background:#e0e7ff;color:#4338ca;padding:4px 10px;border-radius:12px;font-size:0.7rem;margin-right:6px;margin-bottom:4px;display:inline-block;">{t}</span>'
                            for t in p['tech']
                        )}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            col_link, _ = st.columns([1, 4])
            with col_link:
                if p["link"]:
                    st.markdown(f"[View Project]({p['link']})")
                else:
                    st.caption("Coming soon to GitHub")

elif st.session_state.current_page == "Recommendations":
    st.write("**Recommendations page** – AI-curated suggestions just for you!")

elif st.session_state.current_page == "Profile":
    st.write("**Profile page** – your preferences, history, and stats.")

# -------------------------------------------------
# Footer
# -------------------------------------------------
st.markdown("---")
st.caption("© 2025 NeuroNexus by **Ali Munaf** • Built with love and AI")