# Opdracht 1 functies
# Naam student:
# Groep:

import math

def kubus_vol(m):
    volume = m ** 3
    return volume

def bol_vol(r):
    volume = (4/3) * math.pi * (r ** 3)
    return volume

zijde = 5
radius = 4

print(f"De inhoud van deze kubus is: {kubus_vol(zijde)}")
print(f"De inhoud van deze bol is: {bol_vol(radius)}")
