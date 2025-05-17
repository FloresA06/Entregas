
def c_set(nomb):
    n=int(input("Ingrese el numero de elementos del conjunto: "))
    conj=set()
    for i in range(n):
        num=int(input(f"Ingrese el contenido del conjunto {nomb}: "))
        conj.add(num)
    return conj

conjunt1=c_set("A")
conjunt2=c_set("B")

print(f"\nSus conjuntos son:\n A= {conjunt1}\n B= {conjunt2}")
dif=conjunt1-conjunt2
print(f"La diferencia entre los conjuntos es: {dif}")
