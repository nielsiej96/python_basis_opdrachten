# Vragen voor de enquête
vragen = [
    "Wat vind je van de huidige regering?",
    "Wat vind je van de Python-lessen tot nu toe?",
    "Wat vind jij de mooiste stad van Nederland?"
]

# Prompt om te vragen om invoer en instructies
prompt = "Beantwoord de volgende vragen:\n" \
         "Vul 'q' in om de enquête te beëindigen.\n"

# Open een tekstbestand om de resultaten op te slaan
bestandsnaam = "enquete_resultaten.txt"
fo = open(bestandsnaam, 'wt')

# Loop door de vragen en vraag om invoer
for vraag in vragen:
    antwoord = input(vraag + "\n")
    if antwoord.lower() == 'q':
        break  # Stop de lus als 'q' wordt ingevoerd om de enquête te beëindigen
    else:
        fo.write(vraag + ": " + antwoord + "\n")  # Schrijf het antwoord naar het tekstbestand

# Sluit het tekstbestand
fo.close()

print("Bedankt voor het invullen van de enquête. De resultaten zijn opgeslagen in", bestandsnaam)
