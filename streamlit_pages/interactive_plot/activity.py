from streamlit_pages.ekg.person import Person
from peewee import *

class Activity(Model):
    data = CharField()
    subject = ForeignKeyField(Person, backref='activity_data')

    class Meta:
        database = SqliteDatabase('data/person.db')

    @staticmethod
    def load_by_id(id):
        return Activity.get(Activity.id == id)