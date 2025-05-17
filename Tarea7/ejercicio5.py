
def ingresar_empleados():
    empleados=list()
    n=int(input("Indique el numero de empleados a ingresar: "))
    for x in range(n):
        nombre=input("Ingrese el nombre del empleado: ").strip()
        edad=int(input("Ingrese la edad del empleado: "))
        salario=float(input("Ingrese el salario del empleado: "))
        empleado = {
            "nombre": nombre,
            "edad": edad,
            "salario": salario
        }
        empleados.append(empleado)
    return empleados

def empleados_archivo(empleados,nombre_archivo="empleados.txt"):
    with open(nombre_archivo,"w") as archivo:
        for emp in empleados:
            linea=f"Nombre: {emp['nombre']}, Edad: {emp['edad']}, Salario: ${emp['salario']:.2f}"
            archivo.write(linea + "\n")

empleados = ingresar_empleados()
empleados_archivo(empleados)
