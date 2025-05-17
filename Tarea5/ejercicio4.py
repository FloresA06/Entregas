
def crear_set():
    n=int(input("Ingrese el numero de elementos del conjunto: "))
    conj=set()
    for i in range(n):
        num=int(input(f"Ingrese el contenido del conjunto: "))
        conj.add(num)
    return conj

conjunto=crear_set()
if not conjunto:
    print("El conjunto esta vacio")
else:
    print("El conjunto no esta vacio")
