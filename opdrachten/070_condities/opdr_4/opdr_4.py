# Opdracht 4 condities
# Naam student:
# Groep:

toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]

beschikbare_toppings = [topping[0] for topping in toppings]

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings}\n")

gekozen_topping = None
for topping in toppings:
    if keuze.lower() == topping[0]:
        gekozen_topping = topping
        break

if gekozen_topping:
    print(f"U heeft {gekozen_topping[0]} besteld. Dat kost {gekozen_topping[1]}")
else:
    print("Uw keuze zit niet in ons assortiment.")
