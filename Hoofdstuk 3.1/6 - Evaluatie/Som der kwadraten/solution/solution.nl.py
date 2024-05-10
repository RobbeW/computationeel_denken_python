# Vraag de gebruiker om de waarde N
n = int(input("Voer de waarde voor N in: "))
som_kwadraten = 0
# Bereken de som van de kwadraten van 1 tot en met N
for i in range (1, n+1): 
    som_kwadraten += i**2

# Print de som van de kwadraten op het scherm
print()
print("De som van de kwadraten van 1 tot en met", n, "is", som_kwadraten)
