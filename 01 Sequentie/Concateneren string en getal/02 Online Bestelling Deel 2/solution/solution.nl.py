# Vraag de gebruiker naar zijn/haar/hun voornaam, familienaam, straatnaam, huisnummer en postcode
voornaam = input("Voer je voornaam in: ")
familienaam = input("Voer je familienaam in: ")
straatnaam = input("Voer je straatnaam in: ")
huisnummer = input("Voer je huisnummer in: ")
postcode = input("Voer je postcode in: ")

# Print de ingevoerde gegevens
print("De bestelling wordt verzonden naar:", voornaam, familienaam+",", straatnaam, huisnummer+",", postcode+".")
