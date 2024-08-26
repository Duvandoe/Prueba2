nota1 = float(input("Escriba nota 1: "))
nota2 = float(input("Escriba nota 2: "))
nota3 = float(input("Escriba nota 3: "))
promedio = (nota1 + nota2 + nota3) / 3
if (promedio >= 3.0):
    print("Aprobó")
    print("Su promedio es: ",promedio)
else:
    print("Reprobó")
    print("Su promedio es: ",promedio)