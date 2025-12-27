import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Security Check
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("⛔ Access Restricted.")
    st.stop()

load_dotenv() # Load API Key from .env

st.set_page_config(page_title="AI Coach", page_icon="🤖")

st.title("🤖 Quant Coach AI")
st.caption("Powered by Gemini 2.0 Flash")

# --- API CONFIG ---
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("⚠️ GEMINI_API_KEY not found in .env file.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.0-flash-exp')

# --- CHAT INTERFACE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input
if prompt := st.chat_input("Ask about Python, Math, or Trading Strategy..."):
    # User message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # AI Response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # System prompt injection for context
                system_context = "You are a senior quantitative researcher at PrimeMark Kapital. Be strict, mathematical, and prefer Python code examples."
                full_prompt = f"{system_context}\n\nUser: {prompt}"
                
                response = model.generate_content(full_prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Error connecting to AI: {e}")