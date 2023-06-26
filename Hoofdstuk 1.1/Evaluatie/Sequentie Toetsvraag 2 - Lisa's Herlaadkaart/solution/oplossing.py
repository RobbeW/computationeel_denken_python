import math

# Vraag de gebruiker hoeveel Lisa over heeft op haar herlaadkaart
saldo = float(input("Hoeveel heeft Lisa over op haar herlaadkaart?"))

# Bereken hoeveel minuten Lisa nog kan bellen
min_bellen = saldo / 0.20

# Bereken hoeveel sms'en Lisa nog kan versturen
aantal_sms = saldo / 0.10

# Bereken hoeveel MB internet Lisa nog kan gebruiken
mb_internet = saldo / 0.15

# Rond de berekende waarden af naar beneden met de math.floor()-functie
min_bellen_afgerond = math.floor(min_bellen)
aantal_sms_afgerond = math.floor(aantal_sms)
mb_internet_afgerond = math.floor(mb_internet)

# Print de berekende waarden op het scherm in volzinnen
print("Met het overgebleven bedrag kan Lisa nog", min_bellen_afgerond, "minuten bellen.")
print("Met het overgebleven bedrag kan Lisa nog", aantal_sms_afgerond, "sms'en versturen.")
print("Met het overgebleven bedrag kan Lisa nog", mb_internet_afgerond, "MB internet gebruiken.")
