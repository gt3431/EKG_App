import streamlit as st
from peewee import *
from datetime import date
from streamlit_pages.ekg.person import Person
from streamlit_pages.ekg.ekg import EKGData
from streamlit_pages.interactive_plot.activity import Activity



def init():
    # Initial setup of streamlit session states
    if 'person_name' not in st.session_state:
        st.session_state.person_name = 'None'
    
    if 'person' not in st.session_state:
        st.session_state.person = 'None'

    if 'ekgtest_name' not in st.session_state:
        st.session_state.ekgtest_name = 'None'

    if 'ekgtest' not in st.session_state:
        st.session_state.ekgtest = 'None'

    if 'aktivity_name' not in st.session_state:
        st.session_state.aktivity_name = 'None'   

    if 'page' not in st.session_state:
        st.session_state.page = "main"   

    "st.session_state object:" , st.session_state

    # Initial setup of the database
    db = SqliteDatabase('data/person.db')
    db.connect()
    if not db.get_tables():
        db.create_tables([Person, EKGData, Activity])
    if not Person.select():
        #Fill with example data
        julian = Person(firstname='Julian', lastname='Huber', sex='male', picture_path='data/pictures/tb.jpg', date_of_birth=1989)
        julian.save()
        EKGData(date=date(2023, 2, 10), data='data/ekg_data/01_Ruhe.txt', subject=julian).save()
        EKGData(date=date(2023, 3, 11), data='data/ekg_data/04_Belastung.txt', subject=julian).save()
        Activity(data='data/activities/activity.csv', subject=julian).save()
        yannic = Person(firstname='Yannic', lastname='Heyer', sex='male', picture_path='data/pictures/js.jpg', date_of_birth=1967)
        yannic.save()
        EKGData(date=date(2023, 2, 10), data='data/ekg_data/02_Ruhe.txt', subject=yannic).save()
        Activity(data='data/activities/activity2.csv', subject=yannic).save()
        yunus = Person(firstname='Yunus', lastname='Schmirander', sex='male', picture_path='data/pictures/bl.jpg', date_of_birth=1973)
        yunus.save()
        EKGData(date=date(2023, 2, 11), data='data/ekg_data/03_Ruhe.txt', subject=yunus).save()
        Activity(data='data/activities/activity3.csv', subject=yunus).save()
        tobias = Person(firstname='Tobias', lastname='Gasteiger', sex='male', picture_path='data/pictures/none.jpg', date_of_birth=1998)
        tobias.save()
    