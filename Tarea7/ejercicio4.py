
def leer_estudiantes(nombre_archivo="estudiantes.txt"):
    estudiantes=list()
    with open(nombre_archivo,"r") as archivo:
        for linea in archivo:
            partes=linea.strip().split(",")
            nombre=partes[0]
            edad=int(partes[1])
            calificaciones=list(map(float, partes[2:]))
            estudiante={
                "nombre":nombre,
                "edad":edad,
                "calificaciones":calificaciones
                }
            estudiantes.append(estudiante)
    return estudiantes

def mostrar_estudiantes(estudiantes):
    print("Lista estudiantes:")
    for est in estudiantes:
        print(f"Nombre: {est['nombre']}, Edad: {est['edad']}, Calificaciones: {est['calificaciones']}")

estudiantes=leer_estudiantes()
mostrar_estudiantes(estudiantes)
