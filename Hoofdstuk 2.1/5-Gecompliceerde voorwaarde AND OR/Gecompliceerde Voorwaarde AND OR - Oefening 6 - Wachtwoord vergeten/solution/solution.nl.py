# Vaste emailadres en gebruikersnaam
correct_emailadres = "janedoe@sintlievenscollege.be"
correcte_gebruikersnaam = "janedoe"

# Vraag de gebruiker om de gebruikersnaam en wachtwoord
ingevoerd_emailadres = input("Voer uw emailadres in: ")
ingevoerde_gebruikersnaam = input("Voer uw gebruikersnaam in: ")

# Controleer de invoer
if correct_emailadres != ingevoerd_emailadres:
    print("Emailadres niet gekend.")
else:
    if correcte_gebruikersnaam == ingevoerde_gebruikersnaam:
        print("Resetlink verstuurd.")
    else:
        print("Gebruiker en email komen niet overeen.")
