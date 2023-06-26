# Vraag de gebruiker naar het aantal kilometers
km = float(input("Voer het aantal kilometers in: "))

# Bereken de kosten voor beide opties
bxl_tax_kosten = 150 + 0.5 * km
tax_b_kosten = 6.50 * km

# Controleer welke optie goedkoper is
if bxl_tax_kosten < tax_b_kosten:
    print("De voordeligste formule is: BXL-TAX")
else:
    print("De voordeligste formule is: TAX-B")
