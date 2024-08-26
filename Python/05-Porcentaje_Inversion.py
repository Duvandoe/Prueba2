persona1 = input("Escriba nombre de la persona 1: $")
pinv1 = int(input("Escriba la inversion de la persona 1: "))
persona2 = input("Escriba nombre de la persona 2: $")
pinv2 = int(input("Escriba la inversion de la persona 2: "))
persona3 = input("Escriba nombre de la persona 3: $")
pinv3 = int(input("Escriba la inversion de la persona 3: "))
total = pinv1 + pinv2 + pinv3
print("Total de inversion: $",total)
inv1 = (pinv1 / total) * 100
inv2 = (pinv2 / total) * 100
inv3 = (pinv3 / total) * 100
print("Porcentaje de inversion de ",persona1,"es de: ",inv1,"%")
print("Porcentaje de inversion de ",persona2,"es de: ",inv2,"%")
print("Porcentaje de inversion de ",persona3,"es de: ",inv3,"%")

