Algoritmo area_triangulo
	//formula S = (A+B+C) / 2, A = RC(S*(S-A)*(S-B)*(S-C))
	Definir a, b, c, s, area Como Real
	Escribir "Lado A (cm): "
	leer a
	Escribir "Lado B (cm): "
	leer b
	Escribir "Lado C (cm): "
	leer c
	s <- (a+b+c)/2
	area = raiz(s*(s-a)*(s-b)*(s-c))
	Escribir "Semiperimetro: ",s
	Escribir "Area: ",area, " cm"
FinAlgoritmo
