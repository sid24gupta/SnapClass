import streamlit as st

def footer_home():
    
    logo_url = ""
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-alignment:center">
        <p style="font-weight:bold; color:white;">Created by Siddharth</p>
        <img src='{logo_url}' style='max-height:25px'/>
        </div>
                """,unsafe_allow_html=True)