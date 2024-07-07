import streamlit as st
from streamlit_pages.ekg.person import Person

def new_person():
    st.write("## Neue Person hinzufügen")
    # Create input fields for each required field
    firstname = st.text_input("Firstname")
    lastname = st.text_input("Lastname")
    dateofbirth = st.number_input("Date of Birth", min_value=1900, max_value=2024, value=None)
    sex = st.selectbox("Gender", ["Männlich", "Weiblich", "Divers"], index=None)
    picture = st.file_uploader("Picture", type=["jpg", "jpeg", "png"])
    EKG_Data = st.file_uploader("EKG Data", type=["fit", "csv", "txt"])

    # Add a button to deploy the changes
    if st.button("Deploy Changes"):
        # Check if all fields are filled
        if firstname and lastname and sex and dateofbirth:
            # Create a new person object with the input values
            person = Person(firstname=firstname, lastname=lastname, date_of_birth=dateofbirth, sex=sex, picture_path='data/pictures/none.jpg')
            # Save the person object to the database
            person.save()
            
            st.success("Versuchsperson erfolgreich hinzugefügt!")
        else:
            st.warning("Bitte füllen Sie alle Felder aus.")

#TODO: drag and Drop verknüpfen 
#TODO: edit und löschen Button 