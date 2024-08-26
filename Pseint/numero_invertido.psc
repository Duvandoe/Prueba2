Algoritmo numero_invertido
	Definir num, cociente, residuo, invertido Como Entero
	Escribir "Escriba un numero de dos cifras: "
	Leer num
	cociente <- trunc(num / 10)
	residuo <- num MOD 10
	invertido <- (residuo * 10) + cociente
	Escribir "Su numero invertido es: ",invertido
FinAlgoritmo