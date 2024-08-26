def burblesort(arr):
    n = len(arr)
    for i in range(n):
        # Bandera para detectar si hubo intercambio
        swapped = False
        #Ultimos i elementos ya estan en su lugar
        for j in range(0, n-i-1):
        #Comparar elemento actual con el siguiente
            if arr[j] > arr[j+1]:
                #interacambiar si estan en orden incorrecto
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

#Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
print("Arreglo inicial\n", arr)
burblesort(arr)
print("Arreglo final\n", arr)        