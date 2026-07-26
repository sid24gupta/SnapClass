import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home

def home_screen():
    
    header_home()
    style_background_home()
    style_base_layout()
    
    col1, col2 = st.columns(2, gap='large')
    
    with col1:
        st.markdown("<h2 style='text-align: center;'>I'm Student</h2>", unsafe_allow_html=True)
        # Center image container using flexbox wrapper
        st.markdown("""
            <div style="display: flex; justify-content: center; align-items: center; height: 130px;">
                <img src="https://i.ibb.co/844D9Lrt/mascot-student.png" style="max-width: 115px; max-height: 100%; object-fit: contain;">
            </div>
        """, unsafe_allow_html=True)
        st.write("")
        if st.button("Student Portal", type='primary', icon=':material/arrow_outward:', icon_position='right', use_container_width=True):
            st.session_state['login_type'] = 'student'
            st.rerun()
            
    with col2:
        st.markdown("<h2 style='text-align: center;'>I'm Teacher</h2>", unsafe_allow_html=True)
        # Center image container using flexbox wrapper
        st.markdown("""
            <div style="display: flex; justify-content: center; align-items: center; height: 130px;">
                <img src="https://i.ibb.co/CsmQQV6X/mascot-prof.png" style="max-width: 140px; max-height: 100%; object-fit: contain;">
            </div>
        """, unsafe_allow_html=True)
        st.write("")
        if st.button("Teacher Portal", type='primary', icon=':material/arrow_outward:', icon_position='right', use_container_width=True):
            st.session_state['login_type'] = 'teacher'
            st.rerun()
   

    footer_home()