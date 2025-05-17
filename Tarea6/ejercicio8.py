
def reg_estudiantes():
    estudiantes=list()
    n=int(input("Indique el numero de estudiantes a registrar: "))
    for i in range(n):
        nombre=input(f"Nombre del estudiante #{i + 1}: ").strip()
        asignaturas=dict()
        num_asignaturas=int(input("Numero de asignaturas a registrar: "))
        for j in range(num_asignaturas):
            asignatura=input(f"Nombre de la asignatura #{j + 1}: ").strip()
            cal=float(input(f"Calificación en la asignatura {asignatura}: "))
            asignaturas[asignatura]=cal
        amigos=list()
        num_amigos=int(input("Indique el numero de amigos a regustrar: "))
        for k in range(num_amigos):
            amigo=input(f"Nombre del amigo #{k + 1}: ").strip()
            amigos.append(amigo)
        estudiante = {
            "nombre": nombre,
            "asignaturas": asignaturas,
            "amigos": amigos
        }
        estudiantes.append(estudiante)
    return estudiantes

def print_estudiantes(estudiantes):
    print("\nEstudiantes registrados: ")
    for est in estudiantes:
        print(f"\nNombre: {est['nombre']}")
        print("Asignaturas y calificaciones:")
        for materia,nota in est['asignaturas'].items():
            print(f" - {materia}: {nota}")
        print("Amigos:",", ".join(est['amigos']) if est['amigos'] else "Sin amigos registrados")

estudiantes = reg_estudiantes()
print_estudiantes(estudiantes)
