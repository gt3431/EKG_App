import streamlit as st
from streamlit_pages.ekg.person import Person
from streamlit_pages.ekg.ekg import EKGData
from streamlit_pages.interactive_plot.activity import Activity
from datetime import date
import os

def new_person():
    st.write("## Neue Person hinzufügen")
    # Create input fields for each required field
    firstname = st.text_input("Vorname")
    lastname = st.text_input("Nachname")
    dateofbirth = st.number_input("Geburtsjahr", min_value=1900, max_value=2024, value=None)
    sex = st.selectbox("Geschlecht", ["male", "female"], index=None)
    picture = st.file_uploader("Bild", type=["jpg", "jpeg", "png"])
    ekg_data = st.file_uploader("EKG Daten", type=["csv", "txt"])
    activity_data = st.file_uploader("Aktivität Dataen", type=["csv"])

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Speichern"):
            # Speichere das Bild mit dem Dateinamen als Vor- und Nachname
                if picture:
                    picture_filename = f"data/pictures/{firstname[0].lower()}{lastname[0].lower()}.{picture.name.split('.')[-1]}"
                    with open(picture_filename, "wb") as f:
                        f.write(picture.read())
                else:
                    picture_filename = 'data/pictures/none.jpg'
                
                # Erstelle ein neues Personenobjekt mit den Eingabewerten
                if firstname and lastname and sex and dateofbirth:
                    person = Person(firstname=firstname, lastname=lastname, date_of_birth=dateofbirth, sex=sex, picture_path=picture_filename)
                    person.save()
                    st.session_state.page = "main"

                    if ekg_data:
                        ekg_filename = f"data/ekg_data/{firstname.lower()}_{lastname.lower()}_{ekg_data.name}"
                        with open(ekg_filename, "wb") as f:
                            f.write(ekg_data.read())
                        
                        # Erstelle ein neues EKGData-Objekt
                        ekg_record = EKGData(date=date.today(), data=ekg_filename, subject=person)
                        ekg_record.save()
                    
                    if activity_data:
                        activity_filename = f"data/activities/{firstname.lower()}_{lastname.lower()}_{activity_data.name}"
                        with open(activity_filename, "wb") as f:
                            f.write(activity_data.read())
                        
                        # Erstelle ein neues Activity-Objekt
                        activity_record = Activity(data=activity_filename, subject=person)
                        activity_record.save()

                    st.success("Versuchsperson erfolgreich hinzugefügt!")
                    st.rerun()
                else:
                    st.warning("Bitte füllen Sie alle Felder aus.")
    with col2:
        if st.button("Abbrechen"):
            st.session_state.page = "main"
            st.rerun()

def edit_person():
    st.write("## Person bearbeiten")
    print("edit")
    # Erstelle Eingabefelder für jede erforderliche Angabe
    person = st.session_state.editing_person
    print("edit1")
    firstname = st.text_input("Vorname", value=person.firstname)
    lastname = st.text_input("Nachname", value=person.lastname)
    dateofbirth = st.number_input("Geburtsdatum", min_value=1900, max_value=2024, value=person.date_of_birth)
    sex = st.selectbox("Geschlecht", ['male', 'female'], index=["male", "female"].index(person.sex))
    picture = st.file_uploader("Picture", type=["jpg", "jpeg", "png"])
    print("edit2")
    if picture:
        # Speichere das Bild mit den ersten beiden Buchstaben des Vornamens und dem Nachnamen als Dateinamen
        filename = f"data/pictures/{firstname[0].lower()}{firstname[1].lower()}_{lastname.lower()}.{picture.name.split('.')[-1]}"
        with open(filename, "wb") as f:
            f.write(picture.read())
        person.picture_path = filename
    if st.button("Löschen"):
        #picture delete 
        print("deletee")
        if person.picture_path != 'data/pictures/none.jpg':
            os.remove(person.picture_path)
            person.picture_path = 'data/pictures/none.jpg'
        person.delete_instance()
        del st.session_state.editing_person
        st.success("Person erfolgreich gelöscht!")
        st.session_state.page = "main"
        print("deletee")
        st.rerun()
        

    # Hinzufügen einer Schaltfläche zum Anwenden der Änderungen
    if st.button("Aktualisieren"):
        print("edit3")
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
            st.session_state.page = "main"
            st.rerun()
        else:
            st.warning("Bitte füllen Sie alle Felder aus.")

def new_ekg_test():
    ekg_data = st.file_uploader("EKG Data", type=["csv", "txt"])
    person = st.session_state.person
    # Check if the upload button is clicked
    if st.button("Upload EKG Daten"):
        if ekg_data:
            # Save the EKG data with a unique filename
            ekg_filename = f"data/ekg_data/{person.firstname.lower()}_{person.lastname.lower()}_{ekg_data.name}"
            with open(ekg_filename, "wb") as f:
                f.write(ekg_data.read())
            
            # Create a new EKGData object
            ekg_record = EKGData(date=date.today(), data=ekg_filename, subject=person)
            # Save the EKGData object in the database
            ekg_record.save()

            st.success("EKG wurde gespeichert")
            st.rerun()
        else:
            st.warning("Bitte laden Sie eine Datei hoch")
            st.rerun()

def new_activity_test():
    activity_data = st.file_uploader("Aktivitätsdaten", type=["csv"])
    person = st.session_state.person
    # Check if the upload button is clicked
    if st.button("Upload Aktivitätsdaten"):
        if activity_data:
            # Save the EKG data with a unique filename
            activity_filename = f"data/activities/{person.firstname.lower()}_{person.lastname.lower()}_{activity_data.name}"
            with open(activity_filename, "wb") as f:
                f.write(activity_data.read())
            
            # Create a new EKGData object
            activity_record = Activity(data=activity_filename, subject=person)
            # Save the EKGData object in the database
            activity_record.save()

            st.success("Aktivitätsdaten gespeichert")
            st.rerun()
        else:
            st.warning("Bitte laden Sie eine Datei hoch")
            st.rerun()
