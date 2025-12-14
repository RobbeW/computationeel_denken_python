# Invoer: 
per_dag = int(input("Hoeveel snoepjes per dag? "))
totaal = int(input("Hoeveel snoepjes in totaal? "))

# Berekeningen:
dagen = totaal // per_dag
overschot = totaal % per_dag

# Uitvoer:
print("Het kind kan", dagen, "dag(en) snoep eten.")
print("Er blijven", overschot, "snoepjes over.")
