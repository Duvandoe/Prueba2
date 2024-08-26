Algoritmo respuestas
	definir resp1,resp2,resp3 Como Entero
	definir puntaje_final Como Real
	Escribir "Escriba el numero de respuestas correctas: "
	Leer resp1
	Escribir "Escribir el numero de respuestas incorrectas: "
	Leer resp2
	Escribir "Escribir el numero de respuestas en blanco: "
	Leer resp3
	puntaje_final <- (resp1*5) + (resp2*(-1)) + (resp3*0)
	Escribir "El puntaje final es de: ",puntaje_final
FinAlgoritmo
