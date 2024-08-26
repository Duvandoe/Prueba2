tarifa = 75000
nombre = input("Escriba nombre del trabajador(a): ")
horas = int(input("Ingrese el numero de horas trabajadas: "))
faltas = int(input("Numero de faltas: "))
totalnodescuento = horas * tarifa
descuento = faltas * 5 * tarifa
total =  totalnodescuento - descuento
print("------------VOLANTE DE PAGO-------------")
print("El/La senor(a): ",nombre)
print("Su sueldo sin descuento: $",totalnodescuento)
print("El descuento que se hizo: $",descuento)
print("Su sueldo es de: $",total)
print("Faltas: ",faltas)
print("Horas trabajadas: ",horas)
print("-----------------------------------------")