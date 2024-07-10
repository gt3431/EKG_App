from peewee import *
from init import init
import streamlit as st
from streamlit_pages.ekg.page import page as ekg_page
from streamlit_pages.interactive_plot.page import page as interactive_plot_page
from streamlit_pages.sidebar import page as sidebar_page
from streamlit_pages.ekg.edit_masks import new_person , edit_person


if __name__ == "__main__":
    #Initializes the database if empty
    init()

    #Sidebar
    with st.sidebar:
        st.sidebar.title("StreamBoard")
        sidebar_page()

    #Pages
    if st.session_state.page == "main":
        tab_ekg, tab_activity = st.tabs(["EKG", "Aktivitätsdaten"])
        with tab_ekg:
            ekg_page()
        with tab_activity:
            interactive_plot_page()
    elif st.session_state.page == "add":
        new_person()
    elif st.session_state.page == "edit":
        edit_person()
