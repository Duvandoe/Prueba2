Algoritmo Porcentaje_inversion
	definir pinv1, pinv2, pinv3 Como entero
	definir inv1, inv2, inv3, total Como Real
	definir persona1, persona2, persona3 Como Caracter
	Escribir "Escriba el nombre de la persona 1: "
	leer persona1
	Escribir "Escriba la inversion de la persona 1: $"
	leer pinv1
	Escribir "Escriba el nombre de la persona 2: "
	leer persona2
	Escribir "Escriba la inversion de la persona 2: $"
	leer pinv2
	Escribir "Escriba el nombre de la persona 3: "
	leer persona3
	Escribir "Escriba la inversion de la persona 3: $"
	leer pinv3
	total <- pinv1 + pinv2 + pinv3
	Escribir "Total de inversiones: $",total
	inv1 <- (pinv1 / total) * 100
	inv2 <- (pinv2 / total) * 100
	inv3 <- (pinv3 / total) * 100
	Escribir "Porcentaje de inversion de ",persona1,"es de: ",inv1,"%"
	Escribir "Porcentaje de inversion de ",persona2,"es de: ",inv2,"%"
	Escribir "Porcentaje de inversion de ",persona3,"es de: ",inv3,"%"
FinAlgoritmo
