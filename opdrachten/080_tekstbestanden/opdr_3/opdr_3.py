# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:



def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

# Invoer van de gebruiker
plaintext = input("Geef de tekst die wilt encrypten: ")
shift = 5  # Verplaatsingsaantal, bijvoorbeeld 5 posities naar rechts

# Versleutelen van de tekst
encrypted_text = encrypt(plaintext, shift)

# Uitvoer van de versleutelde tekst
print("Versleutelde tekst:")
print(encrypted_text)
