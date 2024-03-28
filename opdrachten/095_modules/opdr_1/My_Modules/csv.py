# csv.py

def sanitize(line):
    """
    Haal alle dubbele spaties en hoofdletters eruit.
    """
    new_lst = []
    lst = line.split(',')
    for item in lst:
        new_lst.append(item.lower().rstrip().strip())
    return new_lst

def create_person(lst):
    """
    Zet de gegevens om in een dictionary.
    """
    person = {"voornaam": "", "tussenvoegsel": "", "achternaam": ""}
    person["voornaam"] = lst[0]
    person["tussenvoegsel"] = lst[1]
    person["achternaam"] = lst[2]
    return person

def add_fullname(person):
    """
    Voeg de volledige naam toe aan de persoon dictionary.
    """
    if person["tussenvoegsel"] == "":
        person['full_name'] = f"{person['voornaam'].title()} {person['achternaam'].title()}"
    else:
        person['full_name'] = f"{person['voornaam'].title()} {person['tussenvoegsel']} {person['achternaam'].title()}"
    return person

def print_persons(persons, filter=["full_name"]):
    """
    Print de volledige naam van alle personen op het scherm.
    """
    counter = 0
    for person in persons:
        counter += 1
        output = ""
        for attr in filter:
            if attr in person:
                output += person[attr].title() + " "
        print(output)
    print(f"Er zijn in totaal {counter} personen")

def do_filter(persons, key, value):
    """
    Filter de personen op basis van een bepaalde sleutel en waarde.
    """
    filtered_persons = []
    for person in persons:
        if key in person and person[key].lower().startswith(value.lower()):
            filtered_persons.append(person)
    return filtered_persons
