# Vraag de gebruiker naar het te betalen bedrag
bedrag = int(input("Voer het te betalen bedrag in euro's in: "))

# Bereken het aantal biljetten en munten
aantal_vijftig = bedrag // 50
bedrag %= 50

aantal_twintig = bedrag // 20
bedrag %= 20

aantal_tien = bedrag // 10
bedrag %= 10

aantal_vijf = bedrag // 5
bedrag %= 5

aantal_twee = bedrag // 2
bedrag %= 2

aantal_een = bedrag // 1
bedrag %= 1

# Print het aantal benodigde biljetten en munten
print("U hebt", aantal_vijftig, "biljetten van 50 euro,", aantal_twintig, "biljetten van 20 euro,", 
      aantal_tien, "biljetten van 10 euro,", aantal_vijf, "biljetten van 5 euro,", aantal_twee, 
      "munten van 2 euro en", aantal_een, "munten van 1 euro nodig om het bedrag van 2543 euro te betalen.")
