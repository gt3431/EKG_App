import streamlit as st
import streamlit_pages.ekg.read_data as rd
from PIL import Image

def page():
    if 'current_user' not in st.session_state:
        st.session_state.current_user = 'None'

    if 'user_ekgtest' not in st.session_state:
        st.session_state.user_ekgtest = 'None'


    col1, col2 = st.columns(2)

    with col1:
        st.write("## Versuchsperson auswählen")
        st.session_state.current_user = st.selectbox(
            'Versuchsperson',
            options = rd.get_person_list(), key="sbVersuchsperson")
        #st.write("Bildpfad: ", rd.get_image_person(st.session_state.current_user))

        if(st.session_state.current_user != "None"):       
            st.session_state.user_ekgtest = st.selectbox(
                'Testauswahl',
                options = rd.get_ekgtest_names_person(st.session_state.current_user), key="sbTestauswahl")

    with col2:
        image = Image.open(rd.get_image_person(st.session_state.current_user))
        st.image(image, caption=st.session_state.current_user)
