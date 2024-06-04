import json
from datetime import datetime 

class Person:

    def __init__(self, person_dict):
        self.id = person_dict["id"]
        self.lastname = person_dict["lastname"]
        self.firstname = person_dict["firstname"]
        self.date_of_birth = person_dict["date_of_birth"]
        self.sex = person_dict["sex"]
        if person_dict["picture_path"]:
            self.picture_path = person_dict["picture_path"]
        else:
            self.picture_path = "data/pictures/none.jpg"

    @staticmethod
    def load_person_data():
        '''Load the whole data from the person_db.json file and return it as a list of dictionaries.'''
        file = open("data/person_db.json")
        person_data = json.load(file)
        return person_data
    
    @staticmethod
    def get_person_name_list() -> list[tuple]:
        '''Return a list of all persons as a tuple with the id and the name. '''
        persons = []
        person_data = Person.load_person_data()
        for person in person_data:
            persons.append((person["id"], f"{person["firstname"]} {person["lastname"]}"))
        return persons

    @staticmethod
    def load_by_id(id):
        '''Return the person with the given name as a dictionary, which contains all its information from the person_db.json file.
        If the person does not exist, return None.'''
        person_data = Person.load_person_data()
        for person in person_data:
            if id == person["id"]:
                return person
        return None
        
    def calc_age(self):
        '''Calculate the age of the person based on the date of birth.'''
        birthyear = int(self.date_of_birth)
        current_year = datetime.now().year
        age = current_year - birthyear
        return age
    
    def calc_max_heart_rate(self):
        if self.sex == "male":
            max_hr_bpm =  223 - 0.9 * self.calc_age()
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 *  self.calc_age()
        else:
            # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)

    def get_ekgtest_names(self) -> list[tuple]:
        '''Return a list of all EKG test names of the person. '''
        ekg_names = []
        ekgs = Person.load_by_id(self.id)["ekg_tests"]

        if len(ekgs[0].keys()) == 0:
            return [(-1, "Kein Test vorhanden")]
        
        for ekg in ekgs:
            name = ekg["result_link"].split("/")[-1]
            name = name.split(".")[0]
            ekg_names.append((ekg["id"], name))
            
        return ekg_names