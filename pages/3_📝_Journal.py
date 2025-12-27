import streamlit as st
import pandas as pd
from datetime import datetime

# Security Check
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("⛔ Access Restricted.")
    st.stop()

st.set_page_config(page_title="Alpha Journal", page_icon="📝", layout="wide")

st.title("📝 Alpha Journal")
st.caption("Document every insight. This is your Intellectual Property.")

# Initialize Session State for journal (Temporary storage)
if "journal" not in st.session_state:
    st.session_state.journal = pd.DataFrame(columns=["Date", "Member", "Topic", "Insight"])

# --- ENTRY FORM ---
with st.expander("✍️ New Log Entry", expanded=True):
    with st.form("entry_form"):
        c1, c2 = st.columns(2)
        date = c1.date_input("Date", datetime.now())
        # Auto-fill member name from login if available
        member = c2.text_input("Member Name", value="Analyst")
        
        topic = st.selectbox("Topic", ["Python/Code", "Math/Stats", "Strategy Research", "Market Structure"])
        insight = st.text_area("Key Insight / Code Snippet")
        
        if st.form_submit_button("Save Entry"):
            new_row = pd.DataFrame({
                "Date": [date], 
                "Member": [member], 
                "Topic": [topic], 
                "Insight": [insight]
            })
            st.session_state.journal = pd.concat([st.session_state.journal, new_row], ignore_index=True)
            st.success("Entry logged successfully!")

# --- DISPLAY LOGS ---
st.divider()
st.subheader("📚 Knowledge Base")

if not st.session_state.journal.empty:
    st.dataframe(st.session_state.journal, use_container_width=True)
    
    # CSV Download Button
    csv = st.session_state.journal.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Journal (CSV)",
        data=csv,
        file_name="primemark_journal.csv",
        mime="text/csv",
    )
else:
    st.info("No entries yet. Start researching!")