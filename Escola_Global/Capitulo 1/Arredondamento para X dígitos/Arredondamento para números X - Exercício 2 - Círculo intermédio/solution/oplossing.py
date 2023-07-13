# Definir pi
pi = 3.14

# Pedir o raio ao utilizador
raio = float(input("Introduza o raio: "))

# Calcular o perímetro e a área
perímetro = 2 * pi * raio
área = pi * raio ** 2

# Imprimir os resultados com 2 casas decimais
print("O perímetro é:", round(perímetro, 2), "metros.")
print("A área é:", round(área, 2), "metros quadrados.")
