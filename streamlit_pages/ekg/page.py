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

    "st.session_state object:" , st.session_state

    def update_slider():
        print(st.session_state.slider)
        st.session_state.slider = (st.session_state.lower_range, st.session_state.upper_range)

    def update_numin():
        print(st.session_state.slider[0], st.session_state.lower_range)
        st.session_state.lower_range = st.session_state.slider[0]
        st.session_state.upper_range = st.session_state.slider[1]

    col1, col2 = st.columns(2)

    with col1:
        ## Person auswählen
        st.write("## Versuchsperson auswählen")
        Person.get_person_name_list()
        st.session_state.person_name = st.selectbox(
            'Versuchsperson',
            options=Person.get_person_name_list(), format_func=lambda option: option[1], key="sbVersuchsperson")

        if st.session_state.person_name:
            st.session_state.person = Person.load_by_id(st.session_state.person_name[0])
        
        ## EKG Test auswählen
        if st.session_state.person:       
            st.session_state.ekgtest_name = st.selectbox(
                'Testauswahl',
                options=st.session_state.person.get_ekgtest_names(), format_func=lambda option: option[1], key="sbTestauswahl")
        
        ## EKG Objekt erstellen
        if st.session_state.ekgtest_name and st.session_state.ekgtest_name[1] != "Kein Test vorhanden":
            st.session_state.ekgtest = EKGData.load_by_id(st.session_state.ekgtest_name[0])
            st.session_state.ekgtest.load_data()
            lower = st.session_state.ekgtest.df["Zeit in ms"].min() / 1000
            upper = int((st.session_state.ekgtest.df["Zeit in ms"].max() / 1000 - lower))
            range_ekg = (300, 310)
            st.write("#### Messwertbereich auswählen")
            low, upp = st.columns(2)
            with low:
                lower_range = st.number_input("Lower", value=295, key="lower_range", on_change = update_slider)
            with upp:
                upper_range = st.number_input("Upper", value=305, key="upper_range", on_change = update_slider)
            range_ekg = st.slider("_", 0, upper, (lower_range, upper_range), key="slider", on_change= update_numin, label_visibility="hidden")
            st.session_state.ekgtest.find_peaks()

        ## Ekg Plot mit Messwerten anzeigen
        if st.session_state.ekgtest and st.session_state.ekgtest_name[1] != "Kein Test vorhanden":
            st.plotly_chart(st.session_state.ekgtest.plot_time_series(range_ekg[0] + lower, range_ekg[1] + lower))
            st.write(f"Maximale Herzfrequenz: {st.session_state.person.calc_max_heart_rate()} bpm")
            st.write(f"Durchschnittliche Herzfrequenz: {st.session_state.ekgtest.estimate_hr()} bpm")

    with col2:
        if st.session_state.person:
            image = Image.open(st.session_state.person.picture_path)
            st.image(image)
            st.write(f"Name: {st.session_state.person.firstname} {st.session_state.person.lastname}")
            st.write(f"Alter: {st.session_state.person.calc_age()}")
            st.write(f"Geburtsdatum: {st.session_state.person.date_of_birth}")

    