# Vaste gebruikersnaam en wachtwoord
correcte_gebruikersnaam = "janedoe"
correct_wachtwoord = "wachtwoord123"

# Vraag de gebruiker om de gebruikersnaam en wachtwoord
ingevoerde_gebruikersnaam = input("Voer uw gebruikersnaam in: ")
ingevoerde_wachtwoord = input("Voer uw wachtwoord in: ")

# Controleer de invoer
print()
if ingevoerde_gebruikersnaam == correcte_gebruikersnaam and ingevoerde_wachtwoord == correct_wachtwoord:
    print("Toegang verleend")
elif ingevoerde_gebruikersnaam == correcte_gebruikersnaam and ingevoerde_wachtwoord != correct_wachtwoord:
    print("Incorrect wachtwoord")
elif ingevoerde_gebruikersnaam != correcte_gebruikersnaam and ingevoerde_wachtwoord == correct_wachtwoord:
    print("Incorrecte gebruikersnaam")
else:
    print("Incorrecte gebruikersnaam en wachtwoord")
