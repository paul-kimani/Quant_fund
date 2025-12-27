import streamlit as st
import pandas as pd
import plotly.express as px
from utils.auth import supabase # Import the client we already created

# 1. Security Check
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("⛔ Access Restricted. Please login from the main page.")
    st.stop()

st.set_page_config(page_title="Dashboard", page_icon="📈", layout="wide")

st.title("📈 Strategic Dashboard")
st.markdown("---")

# 2. Key Metrics Row
c1, c2, c3, c4 = st.columns(4)
c1.metric("Fund Status", "Incubator", "Phase 1")
c2.metric("Strategies", "1 Active", "Momentum")
c3.metric("Data Pipeline", "Yahoo Finance", "Stable")
c4.metric("Risk Limits", "2.0%", "Strict")

# 3. Roadmap Visualization (Cloud-Sync)
st.subheader("📍 Execution Roadmap (Live DB)")

# --- DATABASE FUNCTIONS ---
def fetch_roadmap():
    """Get data from Supabase"""
    try:
        response = supabase.table("roadmap").select("*").order("id", desc=False).execute()
        df = pd.DataFrame(response.data)
        return df
    except Exception as e:
        # Fallback if DB is empty or connection fails
        return pd.DataFrame([
            {"id": 1, "phase": "1. Foundation", "status": "In Progress", "progress": 60, "focus": "Python"},
            {"id": 2, "phase": "2. Portfolio Theory", "status": "Pending", "progress": 0, "focus": "Math"},
        ])

def update_roadmap(edited_df):
    """Sync changes back to Supabase"""
    # 1. SMART LOGIC: Auto-update progress based on status changes
    # If Status is 'Done', force Progress to 100. If 'Pending', force 0.
    edited_df.loc[edited_df["status"] == "Done", "progress"] = 100
    edited_df.loc[edited_df["status"] == "Pending", "progress"] = 0
    
    # Convert DataFrame back to list of dicts for Supabase
    records = edited_df.to_dict('records')
    
    try:
        supabase.table("roadmap").upsert(records).execute()
        st.toast("✅ Database Synced & Progress Updated!", icon="☁️")
    except Exception as e:
        st.error(f"Sync Failed: {e}")

# Load Data from Cloud
if "roadmap_df" not in st.session_state:
    st.session_state.roadmap_df = fetch_roadmap()

# Interactive Editor
edited_df = st.data_editor(
    st.session_state.roadmap_df,
    column_config={
        "id": st.column_config.NumberColumn("ID", disabled=True, width="small"), 
        "phase": st.column_config.TextColumn("Phase", width="medium", disabled=True),
        "status": st.column_config.SelectboxColumn(
            "Status",
            options=["Pending", "In Progress", "Done", "On Hold"],
            required=True,
            width="small"
        ),
        "progress": st.column_config.ProgressColumn(
            "Completion",
            format="%d%%",
            min_value=0,
            max_value=100,
            help="Set Status to 'Done' to auto-complete this.",
        ),
        "focus": st.column_config.TextColumn("Focus Area", width="large"),
    },
    use_container_width=True,
    num_rows="dynamic",
    key="roadmap_editor"
)


# SAVE BUTTON
if st.button("💾 Save & Update Progress"):
    update_roadmap(edited_df)
    # Reload data to confirm visual updates
    st.session_state.roadmap_df = fetch_roadmap()
    st.rerun()

# 4. Market Regime
st.subheader("🌍 Market Context")
st.info("Market data connection is currently: **OFFLINE** (Connect APIs in Phase 2)")

