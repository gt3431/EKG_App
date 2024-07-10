import streamlit as st
from streamlit_pages.ekg.ekg import EKGData
from streamlit_pages.ekg.edit_masks import new_ekg_test
import os

def page():
    #Funktionen für die verbindung von Slider und NumInput
    def update_slider():
        st.session_state.slider = (st.session_state.lower_range, st.session_state.upper_range)

    def update_numin():
        st.session_state.lower_range = st.session_state.slider[0]
        st.session_state.upper_range = st.session_state.slider[1]

    col1, col2 = st.columns(2)

    with col1:        
        ## EKG Test auswählen
        if st.session_state.person:       
            ekgs = st.session_state.person.get_ekgtest_names()
            ekgs.append((-1, 'Neuen Test hinzufügen'))
            st.write("## EKG Test")
            st.session_state.ekgtest_name = st.selectbox(
                'Testauswahl',
                options=ekgs,
                format_func=lambda option: option[1],
                key="sbTestauswahl"
            )
            
            # Überprüfen, ob ein neuer Test hinzugefügt werden soll
            if st.session_state.ekgtest_name and st.session_state.ekgtest_name[0] == -1:
                new_ekg_test()
            
            if st.session_state.ekgtest_name and st.session_state.ekgtest_name[0] != -1:
                st.session_state.ekgtest = EKGData.load_by_id(st.session_state.ekgtest_name[0])
                st.session_state.ekgtest.load_data()
                lower = st.session_state.ekgtest.df["Zeit in ms"].min() / 1000
                upper = int((st.session_state.ekgtest.df["Zeit in ms"].max() / 1000 - lower))
                range_ekg = (300, 310)
                st.session_state.ekgtest.find_peaks()
        
        if st.session_state.ekgtest and st.session_state.ekgtest_name[0] != -1:
            if st.button("Lösche EKG"):
                # Lade den EKG Test
                ekg_test = EKGData.get_by_id(st.session_state.ekgtest_name[0])
                # Lösche den EKG Test
                ekg_test.delete_instance()
                #lösche den EKG Test aus data/ekg_data
                os.remove(ekg_test.data)
                # Aktualisiere die Sitzung
                st.session_state.ekgtest_name = None
                st.session_state.ekgtest = None
                st.success("EKG Test erfolgreich gelöscht!")
                st.rerun()

    with col2:
        if st.session_state.ekgtest and st.session_state.ekgtest_name[0] != -1:
            st.write("#### Messergebnisse")
            st.write(f"Maximale Herzfrequenz: {st.session_state.person.calc_max_heart_rate()} bpm")
            st.write(f"Durchschnittliche Herzfrequenz: {st.session_state.ekgtest.estimate_hr()} bpm")
            st.write(f"Herzratenvariabilität: {st.session_state.ekgtest.hrv()} ms")



    ## EKG Objekt erstellen
    if st.session_state.ekgtest_name and st.session_state.ekgtest_name[0] != -1:
        st.write("#### Analysezeit auswählen [s]")
        ## Slider und NumInput für die Analysezeit
        low, upp = st.columns(2)
        with low:
            lower_range = st.number_input("Lower", value=295, key="lower_range", on_change = update_slider)
        with upp:
            upper_range = st.number_input("Upper", value=305, key="upper_range", on_change = update_slider)
        range_ekg = st.slider("_", 0, upper, (lower_range, upper_range), key="slider", on_change= update_numin, label_visibility="hidden")

    ## Ekg Plot anzeigen
    if st.session_state.ekgtest and st.session_state.ekgtest_name[0] != -1:
        st.plotly_chart(st.session_state.ekgtest.plot_time_series(range_ekg[0] + lower, range_ekg[1] + lower))

