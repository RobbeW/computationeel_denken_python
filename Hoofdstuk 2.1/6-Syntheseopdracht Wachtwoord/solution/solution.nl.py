# Een eenvoudig versleutelingsalgoritme
# Een stuk tekst 'wachtwoord' wordt omgezet naar een versleutelde versie.
def versleutel( wachtwoord : str ):
    from hashlib import sha1
    pw = wachtwoord.encode("utf-8")
    for i in range(100):
        wachtwoord = sha1(pw)
    return wachtwoord.hexdigest()

# Vaste gebruikersnaam en wachtwoord
correcte_gebruikersnaam = "janedoe"
correct_wachtwoord_versleuteld = "f76bbb80bc624a43e8dbcb813b27c2d32d753ce1"

# Vraag de gebruiker om de gebruikersnaam en wachtwoord
ingevoerde_gebruikersnaam = input("Voer uw gebruikersnaam in: ")
ingevoerd_wachtwoord = input("Voer uw wachtwoord in: ")

# Controleer de invoer
if ingevoerde_gebruikersnaam != correcte_gebruikersnaam:
    print("Incorrecte gebruikersnaam")
else:
    if versleutel( ingevoerd_wachtwoord ) == correct_wachtwoord_versleuteld:
        print("Toegang verleend")
    else:
        print("Incorrect wachtwoord")