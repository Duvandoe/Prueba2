suma = 0
contador = 0

while True:
    num = int(input("Ingrese numeros negativos (numeros positivos para terminar): "))
    if num < 0:
        suma += num
        contador += 1
    else:
        break

print(f"Suma de numeros negativos: {suma}")
print(f"cantidad de numeros negativos: {contador}")
