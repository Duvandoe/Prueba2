inv1 = float(input("Escriba la inversion de la persona 1: $"))
inv2 = float(input("Escriba la inversion de la persona 2: $"))
inv3 = float(input("Escriba la inversion de la persona 3: $"))
total = inv1 + inv2 + inv3
print("Total de inversion: $",total)
p_inv1 = (inv1 / total) * 100
p_inv2 = (inv2 / total) * 100
p_inv3 = (inv3 / total) * 100
print("Porcentaje de inversion de la persona 1: ",inv1,"%")
print("Porcentaje de inversion de la persona 2: ",inv2,"%")
print("Porcentaje de inversion de la persona 3: ",inv3,"%")