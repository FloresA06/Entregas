
suma=0
lista=list()
t_lista=int(input("Ingrese el tamaño de la lista: "))

for x in range(t_lista):
    num=int(input("Ingrese un numero: "))
    lista.append(num)

for n in lista:
    suma+=n

print(f"La suma de los digitos en {lista} es: {suma}")
