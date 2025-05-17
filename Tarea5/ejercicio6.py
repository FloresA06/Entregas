
def crear_set():
    n=int(input("Ingrese el numero de elementos del conjunto: "))
    conj=set()
    for i in range(n):
        num=int(input(f"Ingrese el contenido del conjunto: "))
        conj.add(num)
    return conj

conjunto=crear_set()
elem_e=input("\nIngrese el elemento a buscar: ")

if elem_e in conjunto:
    print(f"{elem_e} se encuentra en el conjunto")
else:
    print(f"{elem_e} no se encuentra en el conjunto")
