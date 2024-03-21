# Opdracht 2 lists
# Naam student:
# Groep:


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# Hier jouw code.....

# Print de naam van de 1e rivier met een hoofdletter
print("Naam van de 1e rivier:", rivieren[0].capitalize())

# Print het 2e land waar de 1e rivier doorheen stroomt met een hoofdletter
landen_van_1e_rivier = rivier_info[rivieren[0]]  # Haal de lijst met landen op
print("2e land waar de 1e rivier doorheen stroomt:", landen_van_1e_rivier[1].capitalize())

# Print de naam van de 1e rivier met een hoofdletter
print("De rivier", rivieren[0].capitalize(), "stroomt onder andere door", rivier_info[rivieren[0]][1].capitalize())

# Print de naam van de 2e rivier met een hoofdletter
print("De rivier", rivieren[1].capitalize())

# Print het 1e land waar de 1e rivier doorheen stroomt met een hoofdletter
landen_van_1e_rivier = rivier_info[rivieren[0]]  # Haal de lijst met landen op
print("Het 1e land waar de 1e rivier doorheen stroomt:", landen_van_1e_rivier[0].capitalize())

# Print de naam van de 2e rivier met een hoofdletter
print("De rivier", rivieren[1].capitalize(), "stroomt onder andere door", rivier_info[rivieren[1]][0].capitalize())

# Print de naam van de 3e rivier met een hoofdletter
print("De rivier", rivieren[2].capitalize())

# Print het 3e land waar de 3e rivier doorheen stroomt met een hoofdletter
landen_van_3e_rivier = rivier_info[rivieren[2]]  # Haal de lijst met landen op
print("Het 3e land waar de 3e rivier doorheen stroomt:", landen_van_3e_rivier[2].capitalize())

