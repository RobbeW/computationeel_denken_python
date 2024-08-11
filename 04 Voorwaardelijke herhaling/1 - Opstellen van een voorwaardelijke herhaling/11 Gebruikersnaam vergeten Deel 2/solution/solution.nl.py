# Vaste emailadres en gebruikersnaam
correct_emailadres = "janedoe@sintlievenscollege.be"
correcte_gebruikersnaam = "janedoe"


poging = 0
correct = False
while poging < 3 and not correct:
    # Vraag de gebruiker om de gebruikersnaam en wachtwoord
    ingevoerd_emailadres = input("Voer uw emailadres in: ")
    ingevoerde_gebruikersnaam = input("Voer uw gebruikersnaam in: ")

    # Controleer de invoer
    if correct_emailadres != ingevoerd_emailadres:
        print("Emailadres niet gekend.")
        poging += 1
    else:
        if correcte_gebruikersnaam == ingevoerde_gebruikersnaam:
            print("Resetlink verstuurd.")
            correct = True
        else:
            print("Gebruiker en email komen niet overeen.")
            poging += 1
    
    if poging < 3 and not correct:
        print("Probeer opnieuw.")
