import streamlit as st
import read_data as rd
from PIL import Image

if 'current_user' not in st.session_state:
    st.session_state.current_user = 'None'

st.write("# EKG APP")
st.write("## Versuchsperson auswählen")

col1, col2 = st.columns(2)

with col1:
    st.session_state.current_user = st.selectbox(
        'Versuchsperson',
        options = rd.get_person_list(), key="sbVersuchsperson")

with col2:
    image = Image.open(rd.get_image_person(st.session_state.current_user))
    st.image(image, caption=st.session_state.current_user)







