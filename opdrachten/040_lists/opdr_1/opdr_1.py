# Opdracht 1 lists
# Naam student:
# Groep:

mylist = []
dict_1 = { "id": 0, "voornaam": "Henk", "achternaam": "Tank" }
dict_2 = { "id": 1, "voornaam": "Jan", "achternaam": "Pan" }
dict_3 = { "id": 2, "voornaam": "Piet", "achternaam": "Kiet" }
dict_4 = { "id": 3, "voornaam": "Klaas", "achternaam": "Blaas" }

#Voeg de 4 dictionaries toe aan de list. Maak hierbij gebruik van een list-methode

mylist.append(dict_1)
mylist.append(dict_2)
mylist.append(dict_3)
mylist.append(dict_4)

#Print de volledige naam van de 2e persoon op het scherm door de juiste gegevens op de plek van de vraagtekens te zetten.

print(mylist[1]["voornaam"], mylist[1]["achternaam"])