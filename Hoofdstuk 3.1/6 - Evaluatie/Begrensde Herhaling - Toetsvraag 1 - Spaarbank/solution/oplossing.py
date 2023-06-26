# Vraag de gebruiker om het startbedrag, aantal jaar, en de jaarlijkse interest
startbedrag = float(input("Voer het startbedrag in (tussen 500 en 1000): "))
jaren = int(input("Voer het aantal jaar in dat je wil sparen: "))
interest = float(input("Voer de jaarlijkse interest in (als een percentage): "))

# Bereken het bedrag op de rekening na elk jaar
for jaar in range(1, jaren + 1):
    startbedrag = startbedrag + (startbedrag * (interest / 100))
    print("Na", jaar, "jaar staat er", round(startbedrag,2), "euro op de rekening.")

# Print het eindbedrag na het opgegeven aantal jaren
print("Het eindbedrag na", jaren, "jaar is", round(startbedrag,2), "euro.")
