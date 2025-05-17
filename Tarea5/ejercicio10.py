
def mostrar_menu():
    print("\n*--AGENDA DE CONTACTOS--*")
    print("1.Agregar contacto")
    print("2.Buscar contacto")
    print("3.Eliminar contacto")
    print("4.Salir")

def agregar_cont(agenda):
    nom=input("Ingrese el nombre del contacto: ").strip()
    tel=input("Ingrese el número de teléfono: ").strip()
    agenda[nom]=tel
    print(f"Contacto '{nom}' agregado")

def buscar_cont(agenda):
    nom=input("Ingrese el nombre a buscar: ").strip()
    if nom in agenda:
        print(f"{nom}:{agenda[nom]}")
    else:
        print(f"Contacto '{nom}' no encontrado")

def eliminar_cont(agenda):
    nom=input("Ingrese el contacto a eliminar: ").strip()
    if nom in agenda:
        del agenda[nom]
        print(f"Contacto eliminado")
    else:
        print(f"Contacto no encontrado")


def ejecutar_a():
    agenda=list()
    while True:
        mostrar_menu()
        opcion=input("Seleccione una opcion(1-4): ")
        if opcion=="1":
            agregar_cont(agenda)
        elif opcion=="2":
            buscar_cont(agenda)
        elif opcion=="3":
            eliminar_cont(agenda)
        elif opcion=="4":
            print("Saliendo de la agenda.")
            break
        else:
            print("Opcion invalida. Intente nuevamente.")


ejecutar_a()
