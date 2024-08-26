Algoritmo Donaciones_instituto
	Definir telecomunicacion, sistemas, administracion, contabilidad, donaciones, donacion, pcont Como Real
	Escribir "Da la donacion especial para ser repartida: "
	Leer donacion 
	administracion <- (donacion * 0.3)
	sistemas <- (administracion * 0.15)
	telecomunicacion <- (sistemas * 0.20)
	contabilidad <- donacion - (administracion+sistemas+telecomunicacion)
	pcont <- (contabilidad / donacion) * 100 
	Escribir "Telecomunicaciones recibió: $",telecomunicacion
	Escribir "Sistemas recibió: $",sistemas
	Escribir "Administracion recibió: $",administracion
	Escribir "Contabilidad recibió: $",contabilidad
	Escribir "Porcentaje de contabilidad: ",pcont,"%"
FinAlgoritmo
