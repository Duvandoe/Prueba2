#Funcion
def factorial(num):
    f=1
    for i in range (1,num):
        f = f*i
    return f

#Entrada de datos
n = int(input("Ingrese el valor de n: "))
m = int(input("Ingrese el tamaño del grupo factorial: "))

#Calculos
nf = factorial(n)
mf = factorial(m)
nmf = factorial(n-m)

#Calculo final
c = nf/(mf*nmf)

#Salida de datos
print(f"Cantidad de combinaciones es: ",c)