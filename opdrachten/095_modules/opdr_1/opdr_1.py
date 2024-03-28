# Opdracht 1 functies
# Naam student:
# Groep:

# importeer de module csv...

from My_Modules import csv

# Lijst met gegevens van personen
namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"}
]

# Test de functie om de lijst met personen weer te geven
csv.print_persons(namen)
