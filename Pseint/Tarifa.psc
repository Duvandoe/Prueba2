Algoritmo Tarifa
	Definir tarifas, descuento, faltas, horas, total, totalnodescuento Como Real
	Definir nombre Como Caracter
	tarifas <- 75000
	Escribir "Nombre del trabajador: "
	Leer nombre
	Escribir "Ingrese el numero de horas trabajadas: "
	Leer horas
	Escribir "Numero de faltas: "
	Leer faltas
	totalnodescuento <- horas * tarifas
	descuento <- faltas * 5 * tarifas
	total <-  totalnodescuento - descuento
	Escribir "------------VOLANTE DE PAGO-------------"
	Escribir "El/La señor(a): ",nombre
	Escribir "Su sueldo sin descuento: $",totalnodescuento
	Escribir "El descuento que se hizo: $",descuento
	Escribir "Su sueldo es de: $",total
	Escribir "Faltas: ",faltas
	Escribir "Horas trabajadas: ",horas
	Escribir "-----------------------------------------"
FinAlgoritmo
