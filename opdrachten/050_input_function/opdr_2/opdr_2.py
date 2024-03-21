# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

#Mooi spul

def print_gasten(gasten):
    print("Gasten:")
    for i, gast in enumerate(gasten, start=1):
        print(f"{i}. {gast}")
    print()

def bepaal_volgorde(gasten):
    print("Bepaal de volgorde van de gasten:")
    volgorde = []

    for gast in gasten:
        print(f"Wie zit er naast {gast}? (Voer de naam in of druk op Enter als er niemand naast zit)")
        buurman = input()
        volgorde.append((gast, buurman))

    print("\nDit is de volgorde:")
    for koppel in volgorde:
        print(f"{koppel[0]} zit naast {koppel[1]}")
    print()

def toon_overzicht(gasten, volgorde):
    print("Overzicht:")
    print_gasten(gasten)
    bepaal_volgorde(gasten)

def main():
    gasten = []

    while True:
        print("Wat wil je doen?")
        print("1. Voeg een gast toe")
        print("2. Verwijder een gast")
        print("3. Bepaal de volgorde")
        print("4. Toon overzicht")
        print("5. Stop het programma")

        keuze = input("Voer het nummer van je keuze in: ")

        if keuze == "1":
            naam = input("Voer de naam van de gast in: ")
            gasten.append(naam)
            print(f"{naam} is toegevoegd aan de lijst.\n")
            print_gasten(gasten)
        elif keuze == "2":
            naam = input("Voer de naam van de gast in die wil afzeggen: ")
            if naam in gasten:
                gasten.remove(naam)
                print(f"{naam} is verwijderd uit de lijst.\n")
            else:
                print(f"{naam} staat niet op de lijst.\n")
            print_gasten(gasten)
        elif keuze == "3":
            bepaal_volgorde(gasten)
        elif keuze == "4":
            toon_overzicht(gasten, [])
        elif keuze == "5":
            print("Het programma wordt gestopt.")
            break
        else:
            print("Ongeldige keuze. Probeer het opnieuw.\n")

if __name__ == "__main__":
    main()
