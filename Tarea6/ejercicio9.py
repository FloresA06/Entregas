
def mostrar_menu():
    print("\nAGENDA DE CONTACTOS")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Ver todos los contactos")
    print("5. Salir")

def agregar_contacto(agenda):
    nombre=input("Nombre: ").strip()
    telefono=input("Numero de telefono: ").strip()
    correos=list()
    n=int(input("Indique el numero de correos a registrar: "))
    for i in range(n):
        correo=input(f"Correo #{i + 1}: ").strip()
        correos.append(correo)
    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "correos": correos
    }
    agenda.append(contacto)

def buscar_contacto(agenda):
    nombre_buscar=input("Ingrese el nombre del contacto a buscar: ").strip().lower()
    encontrados=[c for c in agenda if c["nombre"].lower()==nombre_buscar]
    if encontrados:
        for c in encontrados:
            print(f"\nNombre: {c['nombre']}")
            print(f"Telefono: {c['telefono']}")
            print("Correos:",", ".join(c['correos']) if c['correos'] else "Sin correos registrados")
    else:
        print(f"No se encontró el contacto con nombre")

def eliminar_contacto(agenda):
    nombre_eliminar=input("Ingrese el nombre del contacto a eliminar: ").strip().lower()
    for i, c in enumerate(agenda):
        if c["nombre"].lower()==nombre_eliminar:
            del agenda[i]
            print(f"Contacto eliminado")
            return
    print(f"No se encontro el contacto")

def mostrar_todos(agenda):
    if not agenda:
        print("La agenda esta vacia")
    else:
        print("\nLista de contactos:")
        for c in agenda:
            print(f"\nNombre: {c['nombre']}")
            print(f"Telefono: {c['telefono']}")
            print("Correos:",", ".join(c['correos']) if c['correos'] else "Sin correos registrados")

def agenda():
    agenda=list()
    while True:
        mostrar_menu()
        op=input("Seleccione una opcion(1-5): ").strip()
        if op=="1":
            agregar_contacto(agenda)
        elif op=="2":
            buscar_contacto(agenda)
        elif op=="3":
            eliminar_contacto(agenda)
        elif op=="4":
            mostrar_todos(agenda)
        elif op=="5":
            print("Saliendo de la agenda")
            break
        else:
            print("Opcion no válida. Intente nuevamente.")

agenda()