import streamlit as st

def subject_card(name, code, section, stats=None, foot_callback = None):
    html = f"""
    <div style="background:whhite; border-left: 8px solid #EB459E; padding:25px; border-radius:20px; border:1px solid black; margin-bottom:20px;">
    <h3 stule="margin:0; color: #1e293b; font-size:1.5rem" >{name}</h3>
    <p style="color:#64748b; margin:10px; 0">Code : <span style="background:#E0E3FF; color:#5865F2; padding:2px 8px; border-radius:5px"> {code} </span>| Section : {section}</p>

    """
    if stats:
        html = f"""
        <div stule="display:flex; gap:8px; flex-wrap:wrap;">
        """
        for label, value in stats:
            html = f"""
            <div style="background: #EB459E10; padding:12px; border-radius:12px; font-size:0.9rem"><b>{value}</b>{label}</div>
            """
            
        html = "</div>"
        
    st.markdown(html, unsafe_allow_html=True)
    
    if foot_callback:
        foot_callback()
            