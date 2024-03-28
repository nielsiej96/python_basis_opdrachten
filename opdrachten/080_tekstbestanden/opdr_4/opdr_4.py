def ask_questions(question_list, existing_answers=None):
    answers = existing_answers if existing_answers else {}
    for i, question in enumerate(question_list, start=1):
        if question not in answers:
            while True:
                answer = input(f"{i}. {question}\n")
                if answer:
                    answers[question] = answer
                    break
                else:
                    print("Ongeldige invoer. Vul alstublieft iets in.")
        else:
            print(f"{i}. {question}: {answers[question]} (druk op 'c' om te corrigeren)")
            while True:
                answer = input()
                if answer.lower() == 'c':
                    del answers[question]
                    break
                else:
                    print("Ongeldige invoer. Druk op 'c' om te corrigeren.")
    return answers

def save_answers(answers, filename):
    with open(filename, 'w') as file:
        file.write("----\n")
        for question, answer in answers.items():
            file.write(f"{question}: {answer}\n")
        file.write("----\n\n")

def print_summary(answers):
    print("\nHier is een overzicht van je antwoorden:")
    for i, (question, answer) in enumerate(answers.items(), start=1):
        print(f"{i}. {question}: {answer}")

def main():
    # Vragenlijst
    questions = [
        "Wat is je voornaam?",
        "Wat is je achternaam?",
        "Wat neem je mee aan drank?",
        "Wat neem je mee om te eten?"
    ]

    # Welkomstboodschap en menu
    print("Welkom bij het invullen van de vragenlijst voor de party!")
    print("------------------------------")
    print("Om een antwoord te corrigeren, druk op 'c'.")
    print("------------------------------")

    # Vraag de vragen en sla de antwoorden op
    answers = ask_questions(questions)
    save_answers(answers, "feestgangers.txt")

    # Overzicht van antwoorden
    print_summary(answers)

    # Menu voor het aanpassen van antwoorden
    while True:
        print("\nWil je een antwoord aanpassen?")
        print("1. Ja")
        print("2. Nee (stuur antwoorden op)")

        choice = input("Maak een keuze: ")

        if choice == "1":
            # Laat het menu zien voor het aanpassen van antwoorden
            print("Welk antwoord wil je aanpassen?")
            for i, question in enumerate(questions, start=1):
                print(f"{i}. {question}")
            print("0. Terug")

            # Keuze van de gebruiker voor het aanpassen van het antwoord
            answer_choice = input("Maak een keuze: ")

            if answer_choice == "0":
                continue  # Ga terug naar het vorige menu

            try:
                question_to_edit = questions[int(answer_choice) - 1]
                if question_to_edit in answers:
                    del answers[question_to_edit]  # Verwijder het antwoord om opnieuw te vragen
                    answers = ask_questions([question_to_edit], existing_answers=answers)
                    print_summary(answers)  # Toon overzicht van nieuwe antwoorden na wijziging
                else:
                    print("Ongeldige keuze. Probeer het opnieuw.")
            except ValueError:
                print("Ongeldige keuze. Probeer het opnieuw.")
        elif choice == "2":
            # Antwoorden opslaan en programma beëindigen
            save_answers(answers, "feestgangers.txt")
            print("\nBedankt voor het invullen!")
            print("See you at the party.")
            break
        else:
            print("Ongeldige keuze. Probeer het opnieuw.")

if __name__ == "__main__":
    main()

