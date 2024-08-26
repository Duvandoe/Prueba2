Algoritmo Notas
	Definir x, i Como Entero
	Definir suma, promedio, nota Como Real
	Escribir "Numero de notas a ingresar: "
	Leer x
	Dimension nota[x]
	suma <- 0
	Para i <- 1 Hasta x Hacer
		Escribir "Ingresa la nota ", i, ":"
		Leer nota[x]
		suma <- suma + nota[x]
	FinPara
	promedio <- suma / x
	Escribir "El promedio de las notas es: ", promedio
FinAlgoritmo
