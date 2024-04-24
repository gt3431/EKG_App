import json


def load_person_data():
    file = open("data/person_db.json")
    person_data = json.load(file)
    return person_data

def get_person_list():
    persons = []
    person_data = load_person_data()
    for person in person_data:
        persons.append(f"{person["firstname"]} {person["lastname"]}")
    return persons

def get_image_person(person_name):
    person_data = load_person_data()
    for person in person_data:
        if f"{person["firstname"]} {person["lastname"]}" == person_name:
            return person["picture_path"]
    return None



print(load_person_data())
print(get_person_list())