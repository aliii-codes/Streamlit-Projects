import streamlit as st

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="Ali Munaf | NeuroNexus Portfolio",
    page_icon="assets/IMG-20250406-WA0043.jpg",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------------------------------------
# Custom CSS
# -------------------------------------------------
st.markdown("""
<style>
    .hero-section {
        background: linear-gradient(135deg, #1e1b4b 0%, #312e81 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 15px 35px rgba(30, 27, 75, 0.3);
    }
    .hero-name {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #c084fc, #ec4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .hero-title {
        font-size: 1.5rem;
        color: #ddd6fe;
        margin-bottom: 1rem;
    }
    .skill-badge {
        background: #6b21a8;
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 50px;
        font-size: 0.8rem;
        font-weight: 600;
        margin: 0.3rem;
        display: inline-block;
        box-shadow: 0 2px 8px rgba(107, 33, 168, 0.3);
    }
    .project-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 1.5rem;
        margin-top: 2rem;
    }
    .project-card {
        background: white;
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        border: 1px solid #e5e7eb;
    }
    .project-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 16px 40px rgba(139, 92, 246, 0.2);
    }
    .project-img {
        height: 160px;
        background: #e0e7ff;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 3rem;
    }
    .project-body {
        padding: 1.2rem;
    }
    .project-title {
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 0.5rem;
    }
    .project-desc {
        color: #64748b;
        font-size: 0.9rem;
        line-height: 1.5;
    }
    .connect-btn {
        background: linear-gradient(45deg, #7c3aed, #ec4899) !important;
        color: white !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        padding: 0.8rem 2rem !important;
        font-size: 1.1rem !important;
        box-shadow: 0 6px 15px rgba(139, 92, 246, 0.3) !important;
    }
    .connect-btn:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 10px 25px rgba(139, 92, 246, 0.4) !important;
    }
    .contact-card {
        background: #f8f9fa;
        padding: 2.5rem;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        margin: 2rem 0;
    }
    .contact-link {
        font-size: 1.3rem;
        font-weight: 600;
        margin: 1rem 0;
        display: block;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Initialize Page
# -------------------------------------------------
if "current_page" not in st.session_state:
    st.session_state.current_page = "Profile"

# -------------------------------------------------
# Sidebar Navigation
# -------------------------------------------------
st.sidebar.image("assets/seed_1756515283.png", width=120)
st.sidebar.title("NeuroNexus")
page_options = ["Profile", "Explore", "Recommendations", "Connect"]
page = st.sidebar.radio(
    "Navigate",
    page_options,
    index=page_options.index(st.session_state.current_page),
    key="nav"
)
st.session_state.current_page = page

# -------------------------------------------------
# PAGE: Profile
# -------------------------------------------------
if st.session_state.current_page == "Profile":
    # Hero
    st.markdown(f"""
    <div class="hero-section">
        <div class="hero-name">Ali Munaf</div>
        <div class="hero-title">AI Engineer • ML Enthusiast</div>
        <p>Building the future with code, vision, and a little bit of magic.</p>
        <div>
            <span class="skill-badge">Python</span>
            <span class="skill-badge">Streamlit</span>
            <span class="skill-badge">Stable Diffusion</span>
            <span class="skill-badge">OCR + Vision</span>
            <span class="skill-badge">ML @ 87% Acc</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### My Projects")
    st.markdown("<div class='project-grid'>", unsafe_allow_html=True)

    projects = [
        {"name": "Munaf Studio", "emoji": "Art", "desc": "AI image generator with generative fill & object removal", "status": "Live"},
        {"name": "Movies Recommender", "emoji": "Movie", "desc": "87% accurate hybrid ML recommender system", "status": "Live"},
        {"name": "CodeSnap", "emoji": "Camera", "desc": "Hand-drawn flowcharts → Python/JS code in one snap", "status": "In Dev"},
        {"name": "NeuroNexus", "emoji": "Brain", "desc": "This platform — your AI-powered portfolio hub", "status": "Active"},
    ]

    for p in projects:
        st.markdown(f"""
        <div class="project-card">
            <div class="project-img">{p['emoji']}</div>
            <div class="project-body">
                <div class="project-title">{p['name']}</div>
                <div class="project-desc">{p['desc']}</div>
                <br>
                <span style="background:#f0fdf4;color:#166534;padding:4px 10px;border-radius:12px;font-size:0.7rem;">{p['status']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Connect Button
    st.divider()
    col_btn = st.columns([1, 2, 1])[1]
    # with col_btn:
    #     if st.button("Connect with Me", type="primary", key="connect_btn"):
    #         st.session_state.current_page = "Connect"
    #         st.rerun()

# -------------------------------------------------
# PAGE: Connect
# -------------------------------------------------
elif st.session_state.current_page == "Connect":
    st.markdown("<h1 style='text-align:center; color:#7c3aed; margin-top:2rem;'>Let's Connect</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748b; font-size:1.1rem;'>Reach out — I'm always open to ideas, collabs, or just a chat!</p>", unsafe_allow_html=True)

    st.markdown("""
    <div class="contact-card">
        <p class="contact-link">
            <strong>Email:</strong><br>
            <a href="mailto:alikhan4566544@gmail.com" style="color:#dc2626; text-decoration:none;">alikhan4566544@gmail.com</a>
        </p>
        <p class="contact-link">
            <strong>GitHub:</strong><br>
            <a href="https://github.com/khan4566544" target="_blank" style="color:#333; text-decoration:none;">@khan4566544</a>
        </p>
        <p class="contact-link">
            <strong>LinkedIn:</strong><br>
            <a href="https://www.linkedin.com/in/ali-munaf-25557838b/" target="_blank" style="color:#0a66c2; text-decoration:none;">Ali Munaf</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.caption("© 2025 Ali Munaf • Built with curiosity")

# -------------------------------------------------
# PAGE: Explore
# -------------------------------------------------
elif st.session_state.current_page == "Explore":
    st.markdown("## Explore Projects")
    st.write("Discover your projects and trending AI tools.")

# -------------------------------------------------
# PAGE: Recommendations
# -------------------------------------------------
elif st.session_state.current_page == "Recommendations":
    st.markdown("## AI Recommendations")
    st.write("Projects you might love, curated by AI.")

# -------------------------------------------------
# Footer
# -------------------------------------------------
st.markdown("---")
st.caption("© 2025 **Ali Munaf** • NeuroNexus — *Your Portfolio, Amplified by AI*")