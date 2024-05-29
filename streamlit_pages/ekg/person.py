import json

class Person:

    def __init__(self, person_dict):
        self.date_of_birth = person_dict["date_of_birth"]
        self.firstname = person_dict["firstname"]
        self.lastname = person_dict["lastname"]
        self.picture_path = person_dict["picture_path"]
        self.id = person_dict["id"]


    @staticmethod
    def load_person_data():
        '''Load the whole data from the person_db.json file and return it as a list of dictionaries.'''
        file = open("data/person_db.json")
        person_data = json.load(file)
        return person_data

    @staticmethod
    def get_person_list():
        '''Return a list of all person names in the database.'''
        persons = []
        person_data = Person.load_person_data()
        for person in person_data:
            persons.append(f"{person["firstname"]} {person["lastname"]}")
        return persons

    @staticmethod
    def get_person_dict(id):
        '''Return the person with the given name as a dictionary, which contains all its information from the person_db.json file.
        If the person does not exist, return None.'''
        person_data = Person.load_person_data()
        for person in person_data:
            if id == person["id"]:
                return person
        return None
        

    def get_ekgtest_names(self):
        ekg_names = []
        ekgs = Person.get_person_dict(self.id)["ekg_tests"]
        for ekg in ekgs:
            if not ekg:
                return ["Kein Test vorhanden"]
            name = ekg["result_link"].split("/")[-1]
            name = name.split(".")[0]
            ekg_names.append(name)
            return ekg_names