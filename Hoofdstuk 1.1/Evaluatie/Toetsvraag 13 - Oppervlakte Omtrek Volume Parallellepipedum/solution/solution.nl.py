import math

# Gegeven: 
zijde_a = float(input('Voer de lengte in van A (in cm): '))
zijde_b = float(input('Voer de lengte in van B (in cm): '))
zijde_c = float(input('Voer de lengte in van C (in cm): '))

# Eenzelfde formule als bij een balk:
opp = zijde_b * (zijde_a+zijde_c)

# Om de omtrek te berekenen hebben we de lengte van de schuine zijde nodig:
# Stelling van Pythagoras: 
schuine_zijde = math.sqrt(zijde_b**2 + zijde_c**2)
omtrek = (schuine_zijde + (zijde_c+zijde_a))*2

# We berekenen het volume: 
volume = zijde_b * (zijde_c+zijde_a) * (zijde_a+zijde_c)

# Output: 
print(round(opp,2))
print(round(omtrek,2))
print(round(volume,2))
