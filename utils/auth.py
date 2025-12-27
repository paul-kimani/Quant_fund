import streamlit as st
from supabase import create_client, Client
import os
from dotenv import load_dotenv

# Load secrets from .env file
load_dotenv()

# Initialize connection
@st.cache_resource
def init_supabase():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    
    # Debugging: Print to terminal (hidden from user) to see what is loading
    if not url:
        print("DEBUG: SUPABASE_URL is Missing")
        return None
    if not key:
        print("DEBUG: SUPABASE_KEY is Missing")
        return None
    
    try:
        return create_client(url, key)
    except Exception as e:
        print(f"DEBUG: Connection failed. URL used: {url}")
        return None

supabase = init_supabase()

def login_user(email, password):
    """Attempts to log in with Supabase Auth"""
    if not supabase:
        st.error("❌ Database Connection Failed. Please check your .env file.")
        st.info("Ensure SUPABASE_URL starts with 'https://' and keys are correct.")
        return None
    
    try:
        # Sign in
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        return response
    except Exception as e:
        # Return None if login fails so the app doesn't crash
        return None 

def logout_user():
    """Clears session"""
    if supabase:
        supabase.auth.sign_out()
    st.session_state.logged_in = False
    st.session_state.user_email = None