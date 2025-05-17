
t_lista=int(input("Ingrese el tamaño de la lista: "))
lista=list()

for d in range(t_lista):
    num=int(input("Ingrese un numero: "))
    lista.append(num)
print(f"La lista es: {lista}")

lista.sort()
print(f"El numero mayor es {lista[-1]} mientras que el menor es {lista[0]}")
