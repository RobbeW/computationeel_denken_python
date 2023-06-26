# correcte gebruikersnaam en wachtwoord
juiste_gebruikersnaam = "janedoe"
juiste_wachtwoord = "wachtwoord123"

# We stellen de toegang in op False
Toegang = False

# vraag de gebruiker om gebruikersnaam en wachtwoord
gebruikersnaam = input("Voer uw gebruikersnaam in: ")
wachtwoord = input("Voer uw wachtwoord in: ")

while Toegang == False: 
    if gebruikersnaam == juiste_gebruikersnaam and wachtwoord == juiste_wachtwoord:
        print("Toegang verleend")
        Toegang = True
    elif gebruikersnaam != juiste_gebruikersnaam and wachtwoord == juiste_wachtwoord:
        print("Incorrecte gebruikersnaam")
        gebruikersnaam = input("Voer uw gebruikersnaam opnieuw in: ")
        wachtwoord = input("Voer uw wachtwoord opnieuw in: ")
    elif gebruikersnaam == juiste_gebruikersnaam and wachtwoord != juiste_wachtwoord:
        print("Incorrect wachtwoord")
        gebruikersnaam = input("Voer uw gebruikersnaam opnieuw in: ")
        wachtwoord = input("Voer uw wachtwoord opnieuw in: ")
    else:
        print("Incorrecte gebruikersnaam en wachtwoord")
        gebruikersnaam = input("Voer uw gebruikersnaam opnieuw in: ")
        wachtwoord = input("Voer uw wachtwoord opnieuw in: ")
        
    
