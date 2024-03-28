import os

def write_to_file(afile, atext):
    # Controleer of de map al bestaat, zo niet, maak deze dan aan
    directory = os.path.dirname(afile)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Schrijf de tekst naar het bestand
    with open(afile, 'a') as file:
        file.write(atext)

# Definieer de tekst en het bestand
my_tekst = "Schrijf dit maar even in een bestandje\n"
my_file = "C:/Python_090_Functies/test.txt"

# Roep de functie aan om de tekst naar het bestand te schrijven
write_to_file(my_file, my_tekst)

# Print het pad waar het bestand is opgeslagen
print(f"Het bestand is opgeslagen in het volgende pad: {my_file}")
