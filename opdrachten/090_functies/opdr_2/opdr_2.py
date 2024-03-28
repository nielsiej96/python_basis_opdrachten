# Opdracht 1 functies
# Naam student:
# Groep:


def kilometers_naar_miles(km):
    miles = km / 1.609344
    return miles

def miles_naar_kilometers(miles):
    kilometers = miles * 1.609344
    return kilometers

kilometers = 1223
miles = 867

print(f"{kilometers} kilometers = {kilometers_naar_miles(kilometers)} miles")
print(f"{miles} miles = {miles_naar_kilometers(miles)} kilometers")
