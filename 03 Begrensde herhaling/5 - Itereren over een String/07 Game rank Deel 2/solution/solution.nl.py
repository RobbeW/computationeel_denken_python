# Vraag de spelgeschiedenis
history = input("Geef de spelgeschiedenis in: ")

# Bepaal de ranking
rank = 0
wp = 0
for char in history:
    if char == "W":
        wp += 1
    else:
        wp -= 1
    
    if wp == 3:
        rank += 1
        wp = 0
    elif wp == -1:
        rank -= 1
        wp = 0
    
    if rank < 0:
        rank = 0

# Geef de ranking weer
print(f"rank: {rank}")
