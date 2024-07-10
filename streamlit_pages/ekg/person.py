from peewee import *
from datetime import datetime

class Person(Model):
    lastname = CharField()
    firstname = CharField()
    date_of_birth = IntegerField()
    sex = CharField()
    picture_path = CharField()

    class Meta:
        database = db = SqliteDatabase('data/person.db')
    
    @staticmethod
    def get_person_name_list() -> list[tuple]:
        '''Return a list of all persons as a tuple with the id and the name. '''
        persons = []
        for person in Person.select():
            persons.append((person.id, f"{person.firstname} {person.lastname}"))
        return persons

    @staticmethod
    def load_by_id(id):
        '''Return the person with the given id.
        If the person does not exist, returns None.'''
        return Person.get(Person.id == id)
 
    def calc_age(self):
        '''Calculate the age of the person based on the date of birth.'''
        birthyear = int(self.date_of_birth)
        current_year = datetime.now().year
        age = current_year - birthyear
        return age
    
    def calc_max_heart_rate(self):
        '''Calculate the maximum heart rate of the person based'''
        if self.sex == "male":
            max_hr_bpm =  223 - 0.9 * self.calc_age()
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 *  self.calc_age()
        else:
            max_hr_bpm = 224 - 0.88 * self.calc_age()
        return int(max_hr_bpm)

    def get_ekgtest_names(self) -> list[tuple]:
        '''Return a list of all EKG test names of the person. '''
        from streamlit_pages.ekg.ekg import EKGData #Fixes circular import
        
        ekg_names = []
        ekgs = EKGData.select().where(EKGData.subject == self)

        if len(ekgs) == 0:
            return [(-1, "Kein Test vorhanden")]
        
        for ekg in ekgs:
            name = ekg.data.split("/")[-1]
            name = name.split(".")[0]
            ekg_names.append((ekg.id, name))
            
        return ekg_names
    
    def get_activity_names(self) -> list[tuple]:
        '''Return a list of all activity test names of the person. '''
        from streamlit_pages.interactive_plot.activity import Activity #Fixes circular import
        
        activity_names = []
        ativities = Activity.select().where(Activity.subject == self)

        if len(ativities) == 0:
            return [(-1, "Kein Test vorhanden")]
        # Get the name of the activity test
        for act in ativities:
            name = act.data.split("/")[-1]
            name = name.split(".")[0]
            activity_names.append((act.id, name))
            
        return activity_names