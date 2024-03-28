# Opdracht 3 condities
# Naam student:
# Groep:

normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Vraag de leeftijd van de bezoeker
leeftijd_bezoeker = int(input("Geef uw leeftijd in aantal jaar: "))

# Zoek de leeftijdsgroep van de bezoeker
groep = ""
for key, value in leeftijd.items():
    if value[0] <= leeftijd_bezoeker <= value[1]:
        groep = key
        break

# Bepaal de korting
korting = kortings_percentages[groep]
korting_bedrag = (korting / 100) * normale_toegangsprijs
te_betalen = normale_toegangsprijs - korting_bedrag

# Print de output
print("U behoort tot de groep", groep)
print("U krijgt", korting, "% korting")
print("U betaalt daarom", te_betalen)
