import streamlit as st
import time
from utils.auth import login_user, logout_user, supabase

# =========================================================
# 1. PAGE CONFIGURATION (MUST BE FIRST)
# =========================================================
st.set_page_config(
    page_title="StoneHaven Capital",
    page_icon="🦁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# 2. SESSION STATE & TIMEOUT LOGIC
# =========================================================
SESSION_TIMEOUT_MINUTES = 60 

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = "Unknown"
if "last_activity" not in st.session_state:
    st.session_state.last_activity = time.time()

if st.session_state.logged_in:
    # Check timeout
    if (time.time() - st.session_state.last_activity) > (SESSION_TIMEOUT_MINUTES * 60):
        logout_user()
        st.warning("⏳ Session timed out due to inactivity. Please log in again.")
        st.session_state.logged_in = False
        st.rerun()
    else:
        # Reset clock if active
        st.session_state.last_activity = time.time()

# =========================================================
# 3. LOGIN SCREEN (THE GATEKEEPER)
# =========================================================
if not st.session_state.logged_in:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.title("🦁 StoneHaven Capital Access")
        st.markdown("### Quantitative Research Group")
        st.info("Secure Login via Supabase")
        
        with st.form("login_form"):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Enter War Room")
            
            if submit:
                response = login_user(email, password)
                if response:
                    st.session_state.logged_in = True
                    st.session_state.user_email = getattr(response.user, 'email', 'Analyst')
                    st.session_state.last_activity = time.time()
                    st.success("Access Granted.")
                    st.rerun()
                else:
                    st.error("❌ Access Denied. Check credentials.")
    
    # STOP execution here if not logged in. 
    # The code below this line will NEVER run unless the user is logged in.
    st.stop() 

# =========================================================
# 4. AUTHENTICATED AREA (Only runs if logged in)
# =========================================================

# --- GLOBAL SIDEBAR ELEMENTS ---
user_display = st.session_state.get("user_email", "Analyst")
st.sidebar.success(f"Analyst: {user_display}")

if st.sidebar.button("Logout"):
    logout_user()
    st.rerun()
#=====================================================================================================================
# # --- DEFINE PAGES ---
# # Ensure these files exist in your folder structure!
# about_page = st.Page("pages/course/1_About.py", title="About the Course", icon="📚")
# de_zoocamp = st.Page("pages/course/DE_Zoomcamp.py", title="Zoomcamp course for Data science with python", icon="📚")
# faq = st.Page("pages/course/FAQ.py", title="FAQ", icon="❓")
# dashboard_page = st.Page("pages/2_📈_Dashboard.py", title="Dashboard", icon="📈")
# journal_page = st.Page("pages/3_📝_Journal.py", title="Journal", icon="📝")
# coach_page = st.Page("pages/4_🤖_AI_Coach.py", title="AI Coach", icon="🤖")
# analysis_page = st.Page("pages/5_stock_analysis.py", title="Stock Analysis", icon="📊")

# # --- NAVIGATION GROUPS ---
# pg = st.navigation({
#     "Course Materials": [about_page, de_zoocamp, faq],
#     "Hedge Fund Ops": [dashboard_page, analysis_page],
#     "Personal Growth": [journal_page, coach_page]
# })

# # --- RUN NAVIGATION ---
# pg.run()
#=====================================================================================================================
# ... (Previous authentication logic and sidebar code remains above) ...

# =========================================================
# 5. DEFINE PAGES
# =========================================================

# --- 1. Hedge Fund / Main Apps ---
dashboard_page = st.Page("pages/2_📈_Dashboard.py", title="Dashboard", icon="📈")
analysis_page = st.Page("pages/5_stock_analysis.py", title="Stock Analysis", icon="📊")
journal_page = st.Page("pages/3_📝_Journal.py", title="Journal", icon="📝")
coach_page = st.Page("pages/4_🤖_AI_Coach.py", title="AI Coach", icon="🤖")
extras = st.Page("pages/extras.py", title="Extras", icon="✨")
# --- 2. Course: General Info ---
# Note: Paths include 'pages/course/'
course_home = st.Page("pages/course/DE_Zoomcamp.py", title="DE Zoomcamp Home", icon="💻")
about_page = st.Page("pages/course/1_About.py", title="About", icon="ℹ️")
faq_page = st.Page("pages/course/FAQ.py", title="FAQ", icon="❓")

# --- 3. Course: 2024 Cohort ---
# Note: Paths include 'pages/course/2024_cohort/'
c24_overview = st.Page("pages/course/2024_cohort/Course_Overview.py", title="Course Overview", icon="📚")
c24_mod1 = st.Page("pages/course/2024_cohort/Module_1_Introduction_&_Prerequisites.py", title="Mod 1: Intro & Prereqs", icon="1️⃣")
c24_mod2 = st.Page("pages/course/2024_cohort/Module_2_Workflow_Orchestration.py", title="Mod 2: Orchestration", icon="2️⃣")
c24_wk1 = st.Page("pages/course/2024_cohort/Workshop_1_Data_Ingestion.py", title="Workshop 1: Ingestion", icon="🛠️")
c24_mod3 = st.Page("pages/course/2024_cohort/Module_3_Data_Warehouse.py", title="Mod 3: Warehouse", icon="3️⃣")
c24_mod4 = st.Page("pages/course/2024_cohort/Module_4_Analytics_Engineering.py", title="Mod 4: Analytics", icon="4️⃣")
c24_mod5 = st.Page("pages/course/2024_cohort/Module_5_Batch_Processing.py", title="Mod 5: Batch", icon="5️⃣")
c24_wk2 = st.Page("pages/course/2024_cohort/Workshop_2_Stream_Processing_with_SQL.py", title="Workshop 2: Stream SQL", icon="🛠️")
c24_mod6 = st.Page("pages/course/2024_cohort/Module_6_Stream_Processing.py", title="Mod 6: Stream", icon="6️⃣")
c24_project = st.Page("pages/course/2024_cohort/Course_Project.py", title="Final Project", icon="🏆")

# =========================================================
# 6. NAVIGATION STRUCTURE
# =========================================================
pg = st.navigation({
    "Hedge Fund Ops": [dashboard_page, analysis_page, extras],
    "Personal Growth": [journal_page, coach_page],
    "Course Info": [course_home, about_page, faq_page],
    "2024 Cohort Modules": [
        c24_overview,
        c24_mod1,
        c24_mod2,
        c24_wk1,
        c24_mod3,
        c24_mod4,
        c24_mod5,
        c24_wk2,
        c24_mod6,
        c24_project
    ]
})

pg.run()