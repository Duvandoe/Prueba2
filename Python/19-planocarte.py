import math
#Entrada
xA = float(input("Coordenada x de A: "))
xB = float(input("Coordenada x de B: "))
yA = float(input("Coordenada y de A: "))
yB = float(input("Coordenada y de B: "))

#Operaciones
dx = xB - xA
dy = yB - yA
dxx = dx * dx
dyy = dy * dy
suma = dxx + dyy
distancia = math.sqrt(suma)

#Salida
print(f"La distancia entre el punto A y B es: {distancia:.2f}")
