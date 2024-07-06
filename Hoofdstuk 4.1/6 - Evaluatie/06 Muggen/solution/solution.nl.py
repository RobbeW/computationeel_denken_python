# Gegevens vragen
m = int(input("Geef het aantal muggen in: "))
l = int(input("Geef het aantal larven in: "))
p = int(input("Geef het aantal poppen in: "))

e = int(input("Geef het aantal eitjes in dat één mug legt: "))

n = int(input("Geef het aantal weken in: "))

for i in range(n):
    newl = m * e
    m = p // 2
    p = l // 3
    l = newl
    
if m == 0:
    print(f"Er zijn geen muggen na week {n}")
elif m == 1:
    print(f"Er is 1 mug na week {n}")
else:
    print(f"Er zijn {m} muggen na week {n}")
