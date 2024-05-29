import streamlit as st
import streamlit_pages.ekg.read_data as rd
from PIL import Image
from streamlit_pages.ekg.create_plot import make_plot

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
            options=rd.get_person_list(), key="sbVersuchsperson")

        if st.session_state.current_user != "None":
            st.session_state.user_ekgtest = st.selectbox(
                'Testauswahl',
                options=rd.get_ekgtest_names_person(st.session_state.current_user), key="sbTestauswahl")
            st.write(st.session_state.user_ekgtest)

            # Plot erstellen und anzeigen, wenn ein EKG-Test ausgewählt wurde
            if st.session_state.user_ekgtest != "None":
                plot = make_plot(st.session_state.user_ekgtest)
                if plot:
                    st.plotly_chart(plot)

    with col2:
        if st.session_state.current_user != "None":
            image = Image.open(rd.get_image_person(st.session_state.current_user))
            st.image(image, caption=st.session_state.current_user)

    return st.session_state.user_ekgtest, st.session_state.current_user

