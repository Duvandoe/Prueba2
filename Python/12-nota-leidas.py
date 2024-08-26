suma_notas = 0

for i in range(5):
  nota = float(input(f"Ingresa la nota {i+1}: "))
  suma_notas += nota

promedio = suma_notas / 5
print(f"El promedio de las notas es: {promedio:.2f}")