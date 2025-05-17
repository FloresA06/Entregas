
def reg_alumnos():
    alumnos=list()
    n=int(input("Numero de alumnos a registrar: "))
    for i in range(n):
        print(f"Alumno #{i + 1}\n")
        nombre=input("Nombre: ").strip()
        edad=int(input("Edad: "))
        num_cals=int(input("Indique el numero de calificaciones a registrar: "))
        cals=list()
        for j in range(num_cals):
            calificacion=float(input(f"Ingrese la calificacion #{j + 1}: "))
            cals.append(calificacion)
        alumno=(nombre, edad, cals)
        alumnos.append(alumno)
    return alumnos

def print_alumnos(lista_alumnos):
    print("\nLista de alumnos registrados:")
    for alumno in lista_alumnos:
        nombre, edad, calificaciones=alumno
        promedio=sum(calificaciones) / len(calificaciones) if calificaciones else 0
        print(f"Nombre: {nombre}\nEdad: {edad}\nCalificaciones: {calificaciones}\nPromedio: {promedio:.2f}")

alumnos=reg_alumnos()
print_alumnos(alumnos)
