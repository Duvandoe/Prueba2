Algoritmo Notas
	Definir nota1,nota2,nota3, promedio Como Real
	Escribir "Escriba la nota 1: "
	Leer nota1
	Escribir "Escriba la nota 2: "
	Leer nota2
	Escribir "Escriba la nota 3: "
	Leer nota3
	promedio <- (nota1 + nota2 + nota3) / 3
	Si promedio >= 3.0 Entonces
		Escribir "Aprob�"
		Escribir "Su promedio fue: ",promedio
	Sino 
		Escribir "Reprob�"
		Escribir "Su promedio fue: ",promedio
	FinSi
FinAlgoritmo
