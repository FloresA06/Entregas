
def leer_empleados(nombre_archivo="empleados.txt"):
    empleados=list()
    with open(nombre_archivo,"r") as archivo:
        for linea in archivo:
            partes=linea.strip().split(",")
            nombre=partes[0].strip()
            edad=int(partes[1].strip())
            salario=float(partes[2].strip())
            empleado = {
                "nombre": nombre,
                "edad": edad,
                "salario": salario
            }
            empleados.append(empleado)
    return empleados

def salario_prom(empleados):
    if not empleados:
        return 0
    total_salarios=sum(emp['salario'] for emp in empleados)
    return total_salarios / len(empleados)

def empleados_prom(empleados):
    print("Datos empleados:")
    for emp in empleados:
        print(f"Nombre: {emp['nombre']}, Edad: {emp['edad']}, Salario: ${emp['salario']:.2f}")
    promedio=salario_prom(empleados)
    print(f"El salario promedio de los empleados es: ${promedio:.2f}")

empleados=leer_empleados()
empleados_prom(empleados)
