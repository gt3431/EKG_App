import streamlit as st
from streamlit_pages.ekg.page import page as ekg_page
from streamlit_pages.interactive_plot.page import page as interactive_plot_page

if __name__ == "__main__":

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["EKG App", "Interaktiver Plot"])

    if page == "EKG App":
        ekg_page()
    else:
        interactive_plot_page()