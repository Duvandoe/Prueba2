#Entrada de datos
pg = int(input("Ingrese numero de partidos ganados: "))
pe = int(input("Ingrese numero de partidos empatados: "))
pp = int(input("Ingrese numero de partidos perdidos: "))

#Procedemos a realizar el calculo de cada grupo de partidos
ppg = pg * 3
ppe = pe * 1
ppp = pp * 0

#Calculos del puntaje total del equipo ABC club
pt = ppg + ppe + ppp

#Salida de datos
print(f"El puntaje final es de: ",pt)