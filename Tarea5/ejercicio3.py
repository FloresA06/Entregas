
import random

def crear_lista():
    lista_r=list()
    n=int(input("Ingrese el tamaño de la lista: "))
    for i in range(n):
        num=random.randint(1,50)
        lista_r.append(num)
    return lista_r

"""                     #Para input del usuario
def crear_lista():
    lista_r=list()
    n=int(input("Ingrese el tamaño de la lista: "))
    for i in range(n):
        num=input("Ingrese el elemento de la lista: ")
        lista_r.append(num)
    return lista_r
"""

lista=crear_lista()

print(f"Su lista es: {lista}")
conjunto=set(lista)
print(f"Su conjunto sin duplicados es: {conjunto}")
