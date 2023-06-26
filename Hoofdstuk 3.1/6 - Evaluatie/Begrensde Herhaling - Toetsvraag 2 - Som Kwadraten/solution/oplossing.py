# Vraag de gebruiker om de waarde N
N = int(input("Voer de waarde voor N in: "))
som_kwadraten = 0
# Bereken de som van de kwadraten van 1 tot en met N
for i in range (1, N+1): 
    som_kwadraten += i**2

# Print de som van de kwadraten op het scherm
print("De som van de kwadraten van 1 tot", N, "is", som_kwadraten)
