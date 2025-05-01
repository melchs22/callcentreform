import streamlit as st
import time

# Set page config
st.set_page_config(page_title="Call Centre Daily Report", page_icon="📋", layout="centered")

# Custom CSS to make form look stylish
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
        padding: 2rem;
        border-radius: 10px;
    }
    h1 {
        color: #1f77b4;
        text-align: center;
    }
    iframe {
        border: 2px solid #1f77b4;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Page title
st.title("📋 Call Centre Daily Report")

# Intro
st.markdown("""
Welcome to the **Call Centre Daily Reporting Tool**.  
Please take a moment to complete your daily update. Your input drives our growth! 🚀
""")

# Loading spinner
with st.spinner('Loading the reporting form...'):
    time.sleep(2)  # Simulate loading time

# Embed Google Form
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfWt6PzEoYv2lSL8H6WGZaL0IsDmq3I79aMWt5VOseL6CN7_Q/viewform?embedded=true"

st.markdown(
    f"""
    <iframe src="{form_url}" width="720" height="1600" frameborder="0" marginheight="0" marginwidth="0" style="background: white;">
        Loading…
    </iframe>
    """,
    unsafe_allow_html=True
)

# Divider
st.markdown("---")

# Confirm submission message
st.success("✅ After submitting your form, thank you for your dedication today!")

# Footer
st.caption("© 2025 BodaBoda Union | Powered by Love and Togetherness 💚")
