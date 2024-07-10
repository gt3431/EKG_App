import streamlit as st
from streamlit_pages.ekg.person import Person
from PIL import Image

def page():
    #
    #   Display the sidebar with the person selection
    #
    
    persons = Person.get_person_name_list()

    st.session_state.person_name = st.selectbox(
        'Versuchsperson',
        options=persons, format_func=lambda option: option[1], key="sbVersuchsperson")

    if st.session_state.person_name:
        st.session_state.person = Person.load_by_id(st.session_state.person_name[0])
     
    if st.session_state.person:
        image = Image.open(st.session_state.person.picture_path)
        st.image(image)
        st.write(f"Alter: {st.session_state.person.calc_age()}")
        st.write(f"Geburtsdatum: {st.session_state.person.date_of_birth}")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Edit"):
            st.session_state.page = "edit"
            st.session_state.editing_person = st.session_state.person
    with col2:
        if st.button("Add"):
            st.session_state.page = "add"


