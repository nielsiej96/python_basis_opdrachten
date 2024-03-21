# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

pizza_lijst = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

# Sorteer de lijst op alfabet
pizza_lijst.sort()
print(pizza_lijst)

# Voeg een pizza toe
pizza_lijst.append('yo-favorito')
print(pizza_lijst)

# Verwijder de minst lekkere pizza
pizza_lijst.remove('olivio')
print(pizza_lijst)

# Print de eerste 3 pizza's
print(pizza_lijst[:3])

# Print de middelste pizza
print(pizza_lijst[len(pizza_lijst)//2])

# Print de laatste 3 pizza's
print(pizza_lijst[-3:])
