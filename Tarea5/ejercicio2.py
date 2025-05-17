
def c_set(nomb):
    n=int(input("Ingrese el numero de elementos del conjunto: "))
    conj=set()
    for i in range(n):
        num=int(input(f"Ingrese el contenido del conjunto {nomb}: "))
        conj.add(num)
    return conj

def es_subconjunto(conjunto1,conjunto2):
    if conjunto1.issubset(conjunto2):
        print("El primer conjunto es un subconjunto del segundo.")
    else:
        print("El primer conjunto no es un subconjunto del segundo.")

conjunt1=c_set("A")
conjunt2=c_set("B")
es_subconjunto(conjunt1,conjunt2)
