def calcular_nivel_aprobacion():
    def leer_notas():
        nota1 = float(input("Ingrese la primera nota: "))
        nota2 = float(input("Ingrese la segunda nota: "))
        return nota1, nota2

    def calcular_promedio(nota1, nota2):
        return (nota1 + nota2) / 2

    def determinar_nivel_aprobacion(promedio):
       if(opcion == 1):
        if(promedio >= 3.0):
         print("Aprobaste como tecnico")
        else:
          print("No aprobó") 
       elif(opcion == 2):
        if(promedio >= 3.5):
         print("Aprobaste como tecnologo")
        else:
         print("No aprobó") 
       elif(opcion == 3):
        if(promedio >= 4.0):
         print("Aprobaste como profesional")
        else:
         print("No aprobó") 
    def mostrar_menu():
        print("Seleccione el nivel de aprobación:")
        print("1. Técnico")
        print("2. Tecnólogo")
        print("3. Profesional")

    mostrar_menu()
    opcion = int(input("Ingrese su opción: "))
    nota1, nota2 = leer_notas()
    promedio = calcular_promedio(nota1, nota2)
    nivel_aprobacion = determinar_nivel_aprobacion(promedio)
    print("Promedio:", promedio)


calcular_nivel_aprobacion()