# Opdracht 1 condities
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

# Hier start de for-loop....

# Lijst initialiseren
getallen = []

# Loop om getallen van 1 t/m 10 toe te voegen aan de lijst
for i in range(1, 11):
    getallen.append(i)

# Print alleen getallen groter dan 4
for num in getallen:
    if num > 4:
        print(num)
