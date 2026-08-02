import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.database.db import check_teacher_exists, create_teacher, teacher_login

def teacher_screen():
    
    style_background_dashboard()
    style_base_layout()
    
    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == "login":
        teacher_screen_login()
    
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()


def teacher_dashboard():
    teacher_data = st.session_state.teacher_data
    
    st.subheader(f"""Welcome, {teacher_data['name']}""")
    

def login_teacher(username, password):
    if not username or not password:
        return False
    
    teacher = teacher_login(username,password)
    if teacher:
        st.session_state.user_role = 'teacher'
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True
        

def teacher_screen_login():
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    
    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state["login_type"] = None
            st.rerun()

    st.header('Login using password', text_alignment='center')
    st.space()
    
    teacher_username = st.text_input("Enter Username", placeholder='John Write')
    teacher_password = st.text_input("Enter Password", type='password', placeholder="Enter Password")
    st.divider()
    
    btnc1, btnc2 = st.columns(2)
    
    with btnc1:
        if st.button("Login", icon=':material/passkey:', shortcut="control+enter", width='stretch'):
            if login_teacher(teacher_username, teacher_password):
                st.toast("Welcome Back!")
                import time
                time.sleep(2)
                st.rerun()
            else:
                st.error("Invalid username snf password combo")
    
    with btnc2:
        if st.button("Register Instead", type='primary', icon=':material/passkey:', width='stretch'):
           st.session_state.teacher_login_type = 'register' 
        
    footer_dashboard()
    
    
def register_teacher(teacher_username,teacher_name,teacher_password,teach_pass_confirm):
    
    if not teacher_username or not teacher_name or not teacher_password:
        return False, "All Fields are required"
    
    if check_teacher_exists(teacher_username):
        return False, "Username already exists."
    
    if teacher_password != teach_pass_confirm:
        return False, "Password doesnt match"
    
    try:
        create_teacher(teacher_username, teacher_password, teacher_username)
    except Exception as e:
        return False, "Unexpected Error!"
    return True, "Successfully Created! Please proceed with Login"


def teacher_screen_register():
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    
    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state["login_type"] = None
            st.rerun()
        
    st.header('Register your teacher profile')
    
    st.space()
    
    teacher_name = st.text_input("Enter Name", placeholder='Enter Name')    
    teacher_username = st.text_input("Enter Username", placeholder='Enter Username')
    teacher_password = st.text_input("Enter Password", type='password', placeholder="Enter Password")
    teach_pass_confirm = st.text_input("Confirm your Password", type='password', placeholder="Confirm Password")
    
    
    st.divider()
    
    btnc1, btnc2 = st.columns(2)
    
    with btnc1:
        if st.button("Register Now", icon=':material/passkey:', shortcut="control+enter", width='stretch'):
            success , message = register_teacher(teacher_username,teacher_name,teacher_password,teach_pass_confirm)
            if success:
                st.success(message)
                import time
                time.sleep(2)
                st.session_state.teacher_login_key = "login"
                st.rerun()
            else:
                st.error(message)
            
    with btnc2:
        if st.button("Login Instead", type='primary', icon=':material/passkey:', width='stretch'):
            st.session_state.teacher_login_type = 'login'    
    footer_dashboard()
    
    