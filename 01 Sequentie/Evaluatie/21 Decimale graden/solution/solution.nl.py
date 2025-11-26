# Decimale graad vragen
graad = int(input("Geef het gehele deel in: "))
decimaal = int(input("Geef de eerste 3 cijfers na de komma: "))

# Omzetten
minuten = decimaal * 60 // 1000
resterend = decimaal * 60 % 1000

seconden = resterend * 60 // 1000

# Weergeven op het scherm
print( "Dit komt overeen met", graad, "graden", minuten, "minuten en", seconden, "seconden.")
