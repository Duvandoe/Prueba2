#Definir variables para N numero de notas
x = int(input("Ingresar numero de notas: "))

#Definicion de arreglo (vector) con x dimensiones
notas = [0] * x

#Leer las notas
for i in range(x):
    notas[i] = float(input(f"Ingrese la nota {i+1}: "))
   
#Calcular promedio
promedio = sum(notas) / x

#Mostrar promedio
print(f"El promedio de las notas es: {promedio:.2f}")