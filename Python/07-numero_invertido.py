num = int(input("Escriba un numero de dos cifras: "))
cociente = num / 10
residuo = num % 10
invertido = (residuo * 10) + cociente
print("Su numero invertido es: ",invertido)