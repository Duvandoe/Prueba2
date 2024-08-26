import math #Operaciones matematicas math.ceil es redondear la cifra

print("-------------------------------------------")
print(" Numero de micro discos 3.5 necesarios")
print("-------------------------------------------")

#Entrada
GB = float(input("Ingrese el numero GB: "))

#Proceso
MB = GB * 1024
MD = MB / 1.44

#Salida
print("-------------------------------------------")
print("\nSalida:")
print(MD)

#Usa la funcion decimal aproxima math.cel
print("Numero de discos necesarios: ", math.ceil(MD))