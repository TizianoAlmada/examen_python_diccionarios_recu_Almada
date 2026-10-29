notas={
    "Perez":[],
    "Salatic":[],
    "Almada":[],
    "Loberza":[],
    "Moyano":[]
}
continuar=True
while continuar:
    print("1. Ver notas de todos los alumnos")
    print("2. Ver notas de un alumno")
    print("3. Cargar 5 notas a un alumno")
    print("4. Promedio de un alumno")
    print("5. Salir del sistema")
    opcion=int(input("Ingrese la opcion: "))
    if opcion==1:
        for key in notas.keys():
            print(f"{key}: {notas[key]}")
    elif opcion==2:
        alumno=input("Ingrese el apellido del alumno\n")
        encontrado=False
        for key in notas.keys():
            if alumno==key:
                print(f"El alumno {alumno} tiene las notas: {notas[alumno]}")
                encontrado=True  
        if encontrado==False:
            print("No se encontro al alumno")
            break
        else:
            print("Se enconto al alumno")
    elif opcion==3:
        alumno=input("Ingrese el apellido del alumno que desea cargar 5 notas\n")
        for key in notas.keys():
            if alumno==key:
                for value in notas[alumno]:
                    if len(notas[alumno])==0:
                        for value in range(5):
                            nota=int(input("Ingrese la nota: "))
                            notas[key]=nota
                    elif len(notas[alumno])==5:
                        print("El alumno ya tiene 5 notas")
    elif opcion==4:
        alumno=input("Ingrese el alumno que desea ver el promedio\n")
        for key in notas.keys():
            if alumno==key:
                suma=nota+nota
                promedio=nota/len(notas[alumno])
                print(f"El alumno {alumno} tiene de promedio: {promedio}")
    elif opcion==5:
        print("Saliendo del sistema")
        continuar=False
    else:
        print("ingrese una opcion valida")
                    
