
lista=list()
t_lista=int(input("Indique el tamaño de la lista: "))

for n in range(t_lista):
    num=int(input("Ingrese un numero: "))
    lista.append(num)
print(f"Su lista es: {lista}")

for x in range(t_lista-1):
	menor=x
	for y in range(x+1,t_lista):
		if lista[y]<lista[menor]:
			menor=y
	lista[x], lista[menor]=lista[menor], lista[x]

print(f"Su lista ordenada de menor a mayor: {lista}")
