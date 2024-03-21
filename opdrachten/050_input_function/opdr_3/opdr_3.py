# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...
# Initialiseer een lege lijst voor de programmeertalen
programmeertalen = []

# Blijf invoer vragen totdat er minimaal 5 programmeertalen zijn ingevoerd
while len(programmeertalen) < 5:
    taal = input("Voer een programmeertaal in (druk op Enter om door te gaan): ")
    if taal.strip():  # Controleer of de invoer niet leeg is
        programmeertalen.append(taal.strip())
    else:
        print("Je moet een programmeertaal invoeren.")

# Filter de programmeertalen die beginnen met "z" en sorteer ze in omgekeerde volgorde
gesorteerde_programmeertalen = sorted(filter(lambda taal: taal.lower().startswith("z"), programmeertalen), reverse=True)

# Sorteer de overige programmeertalen in omgekeerde volgorde
overige_programmeertalen = sorted(filter(lambda taal: not taal.lower().startswith("z"), programmeertalen), reverse=True)

# Voeg de gesorteerde programmeertalen samen
gesorteerde_programmeertalen.extend(overige_programmeertalen)

# Print de gesorteerde lijst met programmeertalen
print("Gesorteerde lijst met programmeertalen:")
print(gesorteerde_programmeertalen)
