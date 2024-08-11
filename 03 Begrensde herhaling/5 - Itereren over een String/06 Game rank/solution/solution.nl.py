# Vraag de spelgeschiedenis
history = input("Geef de spelgeschiedenis in: ")

# Bepaal de ranking
rank = 0
aantal_W = 0
aantal_L = 0
for char in history:
    if char == "W":
        aantal_W += 1
    else:
        aantal_L += 1
    
    if aantal_W == 3:
        aantal_W = 0
        rank += 1
    if aantal_L == 3:
        aantal_L = 0
        if rank > 0:
            rank -= 1
print()
# Geef de ranking weer
print(f"rank: {rank}")
