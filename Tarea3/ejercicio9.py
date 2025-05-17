
lista=list()
t_lista=int(input("Indique el tamaño de la lista: "))
for x in range(t_lista):
    num=float(input("Ingrese el numero: "))
    lista.append(num)

print(f"Su lista es: {lista}")

def seg_may(lista):
    lista.sort(reverse=True)
    mayor2=min(lista[0],lista[1]) #Por que el mayor seria: mayor=max(lista[0],lista[1])
    print(f"El segundo numero mayor en la lista es: {mayor2}")

seg_may(lista)
