import streamlit as st
from streamlit_pages.ekg.person import Person
from streamlit_pages.ekg.ekg import EKGData
from PIL import Image

def page():
    if 'person_name' not in st.session_state:
        st.session_state.person_name = 'None'
    
    if 'person' not in st.session_state:
        st.session_state.person = 'None'

    if 'ekgtest_name' not in st.session_state:
        st.session_state.ekgtest_name = 'None'

    if 'ekgtest' not in st.session_state:
        st.session_state.ekgtest = 'None'

    col1, col2 = st.columns(2)

    with col1:
        ##Person auswählen
        st.write("## Versuchsperson auswählen")
        st.session_state.person_name = st.selectbox(
            'Versuchsperson',
            options = Person.get_person_name_list(), format_func=lambda option: option[1] ,  key="sbVersuchsperson")

        if st.session_state.person_name:
            st.session_state.person = Person(Person.load_by_id(st.session_state.person_name[0]))
        
        ##EKG Test auswählen
        if st.session_state.person:       
            st.session_state.ekgtest_name = st.selectbox(
                'Testauswahl',
                options = st.session_state.person.get_ekgtest_names(), format_func=lambda option: option[1], key="sbTestauswahl")
        
        if st.session_state.ekgtest_name:
            st.session_state.ekgtest = EKGData(EKGData.load_by_id(st.session_state.person.id, st.session_state.ekgtest_name[0]))

        ##Plot anzeigen
        st.session_state.ekgtest.find_peaks()
        st.plotly_chart(st.session_state.ekgtest.make_plot())


        st.write(st.session_state.ekgtest_name)
        st.write(f"Alter: {st.session_state.person.calc_age()}")
        st.write(f"Maximale Herzfrequenz: {st.session_state.person.estimate_max_hr()} bpm")
    with col2:
        image = Image.open(st.session_state.person.picture_path)
        st.image(image)

    # Plot erstellen und anzeigen, wenn ein EKG-Test ausgewählt wurde
    '''if st.session_state.user_ekgtest != "None":
        plot = make_plot(st.session_state.user_ekgtest)
        if plot:
            st.plotly_chart(plot)'''
