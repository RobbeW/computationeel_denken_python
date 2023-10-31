# Vaste gebruikersnaam en wachtwoord
correcte_gebruikersnaam = "janedoe"
correct_wachtwoord_versleuteld = "f76bbb80bc624a43e8dbcb813b27c2d32d753ce1"

# Implementeer hier de login procedure









# Een eenvoudig versleutelingsalgoritme
# Een stuk tekst 'wachtwoord' wordt omgezet naar een versleutelde versie.
# Gebruik deze functie als volgt: variabele = versleutel( ingevoerd_wachtwoord )
def versleutel( wachtwoord : str ):
    from hashlib import sha1
    pw = wachtwoord.encode("utf-8")
    for _ in range( 100 ):
        wachtwoord = sha1(pw)
    return wachtwoord.hexdigest()