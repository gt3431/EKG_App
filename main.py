import streamlit as st
from streamlit_pages.ekg.page import page as ekg_page
from streamlit_pages.interactive_plot.page import page as interactive_plot_page
from peewee import *
from streamlit_pages.ekg.person import Person
from streamlit_pages.ekg.ekg import EKGData
from datetime import date


if __name__ == "__main__":
    
    #TODO: Make this ist own file and import it
    # Initial setup of the database
    db = SqliteDatabase('data/person.db')
    db.connect()
    if not db.get_tables():
        db.create_tables([Person, EKGData])
    if not Person.select():
        #Fill with example data
        julian = Person(firstname='Julian', lastname='Huber', sex='male', picture_path='data/pictures/tb.jpg', date_of_birth=1989)
        julian.save()
        EKGData(date=date(2023, 2, 10), data='data/ekg_data/01_Ruhe.txt', subject=julian).save()
        EKGData(date=date(2023, 3, 11), data='data/ekg_data/04_Belastung.txt', subject=julian).save()
        yannic = Person(firstname='Yannic', lastname='Heyer', sex='male', picture_path='data/pictures/js.jpg', date_of_birth=1967)
        yannic.save()
        EKGData(date=date(2023, 2, 10), data='data/ekg_data/02_Ruhe.txt', subject=yannic).save()
        yunus = Person(firstname='Yunus', lastname='Schmirander', sex='male', picture_path='data/pictures/bl.jpg', date_of_birth=1973)
        yunus.save()
        EKGData(date=date(2023, 2, 11), data='data/ekg_data/03_Ruhe.txt', subject=yunus).save()
        tobias = Person(firstname='Tobias', lastname='Gasteiger', sex='male', picture_path='data/pictures/none.jpg', date_of_birth=1998)
        tobias.save()

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["EKG App", "Interaktiver Plot"])

    if page == "EKG App":
        ekg_page()
    else:
        interactive_plot_page()