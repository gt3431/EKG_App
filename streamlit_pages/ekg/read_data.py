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

def get_person(person_name):
    person_data = load_person_data()
    for person in person_data:
        if f"{person["firstname"]} {person["lastname"]}" == person_name:
            return person
    return None

def get_image_person(person_name):
    if(get_person(person_name)):
        path = get_person(person_name)["picture_path"]
        if path:
            return path
        else:
            return "data/pictures/none.jpg"
    else :
        return "data/pictures/none.jpg"
    

def get_ekgtest_names_person(person_name):
    if(get_person(person_name)):
        ekg_names = []
        print("EKG-Tests: ")
        print(get_person(person_name)["ekg_tests"])
        ekgs = get_person(person_name)["ekg_tests"]
        for ekg in ekgs:
            if not ekg:
                return ["Kein Test vorhanden"]
            name = ekg["result_link"].split("/")[-1]
            name = name.split(".")[0]
            ekg_names.append(name)
        return ekg_names
    else :
        return ["Kein Test vorhanden"]