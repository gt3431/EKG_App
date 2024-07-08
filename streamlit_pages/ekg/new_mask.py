import streamlit as st
from streamlit_pages.ekg.person import Person
from streamlit_pages.ekg.ekg import EKGData
from datetime import date
import os
def new_person():
    st.write("## Neue Person hinzufügen")
    # Create input fields for each required field
    firstname = st.text_input("Firstname")
    lastname = st.text_input("Lastname")
    dateofbirth = st.number_input("Date of Birth", min_value=1900, max_value=2024, value=None)
    sex = st.selectbox("Gender", ["male", "female", "other"], index=None)
    picture = st.file_uploader("Picture", type=["jpg", "jpeg", "png"])
    ekg_data = st.file_uploader("EKG Data", type=["fit", "csv", "txt"])

    # Add a button to deploy the changes
    if st.button("Deploy Changes"):
        # Speichere das Bild mit dem Dateinamen als Vor- und Nachname
            if picture:
                picture_filename = f"data/pictures/{firstname[0].lower()}{lastname[0].lower()}.{picture.name.split('.')[-1]}"
                with open(picture_filename, "wb") as f:
                    f.write(picture.read())
            else:
                picture_filename = 'data/pictures/none.jpg'
            
            # Erstelle ein neues Personenobjekt mit den Eingabewerten
            person = Person(firstname=firstname, lastname=lastname, date_of_birth=dateofbirth, sex=sex, picture_path=picture_filename)
            # Speichere das Personenobjekt in der Datenbank
            person.save()

            if ekg_data:
                ekg_filename = f"data/ekg_data/{firstname.lower()}_{lastname.lower()}_{ekg_data.name}"
                with open(ekg_filename, "wb") as f:
                    f.write(ekg_data.read())
                
                # Erstelle ein neues EKGData-Objekt
                ekg_record = EKGData(date=date.today(), data=ekg_filename, subject=person)
                # Speichere das EKGData-Objekt in der Datenbank
                ekg_record.save()

                st.success("Versuchsperson und EKG-Daten erfolgreich hinzugefügt!")
            else:
                st.warning("Bitte füllen Sie alle Felder aus.")


def edit_person(person):
    st.write("## Person bearbeiten")
    # Erstelle Eingabefelder für jede erforderliche Angabe
    firstname = st.text_input("Firstname", value=person.firstname)
    lastname = st.text_input("Lastname", value=person.lastname)
    dateofbirth = st.number_input("Date of Birth", min_value=1900, max_value=2024, value=person.date_of_birth)
    sex = st.selectbox("Gender", ['male', 'female', 'other'], index=["male", "female", "other"].index(person.sex))
    picture = st.file_uploader("Picture", type=["jpg", "jpeg", "png"])
    if picture:
        # Speichere das Bild mit den ersten beiden Buchstaben des Vornamens und dem Nachnamen als Dateinamen
        filename = f"data/pictures/{firstname[0].lower()}{firstname[1].lower()}_{lastname.lower()}.{picture.name.split('.')[-1]}"
        with open(filename, "wb") as f:
            f.write(picture.read())
        person.picture_path = filename
    if st.button("Delete Person"):
        person.delete_instance()
        st.success("Person erfolgreich gelöscht!")
        del st.session_state.editing_person
        st.session_state.page = 'Main'
        #picture delete 
        if person.picture_path != 'data/pictures/none.jpg':
            os.remove(person.picture_path)
            person.picture_path = 'data/pictures/none.jpg'
        

    # Hinzufügen einer Schaltfläche zum Anwenden der Änderungen
    if st.button("Apply Changes"):
        # Überprüfen, ob alle Felder ausgefüllt sind
        if firstname and lastname and sex and dateofbirth:
            # Aktualisiere die Personendetails
            person.firstname = firstname
            person.lastname = lastname
            person.date_of_birth = dateofbirth
            person.sex = sex
            # Speichere die Änderungen in der Datenbank
            person.save()
            st.success("Person erfolgreich aktualisiert!")
            # Entferne den editing_person Zustand und kehre zur Hauptseite zurück
            del st.session_state.editing_person
            st.session_state.page = 'Main'
            st.experimental_rerun()
        else:
            st.warning("Bitte füllen Sie alle Felder aus.")

def new_ekg_test(person):
    ekg_data = st.file_uploader("EKG Data", type=["fit", "csv", "txt"])
    
    # Check if the upload button is clicked
    if st.button("Upload EKG Data"):
        if ekg_data:
            # Save the EKG data with a unique filename
            ekg_filename = f"data/ekg_data/{person.firstname.lower()}_{person.lastname.lower()}_{ekg_data.name}"
            with open(ekg_filename, "wb") as f:
                f.write(ekg_data.read())
            
            # Create a new EKGData object
            ekg_record = EKGData(date=date.today(), data=ekg_filename, subject=person)
            # Save the EKGData object in the database
            ekg_record.save()

            st.success("EKG data successfully uploaded and added to the database!")
