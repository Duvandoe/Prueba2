#Funcion
def contador():
    #Determinar filas y columnas
    n = int(input("Ingrese el número de filas: "))
    m = int(input("Ingrese el número de columnas: "))
    
    #Matriz y ingreso de numeros
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            num = int(input(f"Ingrese el número en la posición ({i+1},{j+1}): "))
            fila.append(num)
        matriz.append(fila)
    #Declarar
    positivos = 0
    negativos = 0
    neutral = 0
    #Condiciones para determinar
    for fila in matriz:
        for num in fila:
            if num > 0:
                positivos += 1
            elif num < 0:
                negativos += 1
            else:
                neutral += 1
    print(f"Positivos: ", positivos)
    print(f"Negativos: ", negativos)
    print(f"Neutros: ", neutral)

# Llamada a la función
contador()
