
lista=list()
t_lista=int(input("Indique el tamaño de la lista: "))

for x in range(t_lista):
    num=int(input("Ingrese un numero: "))
    lista.append(num)

print(f"Su lista es: {lista}")

def calc_med(lista,t_lista):
    lista.sort()
    if t_lista%2!=0:
        indice=int(t_lista/2)
        print(f"La mediana de la lista es: {lista[indice]}")
    elif t_lista%2==0:
        indice=int(t_lista/2)
        med=(lista[indice-1]+lista[indice])/2
        print(f"La mediana de la lista es: {med}")

calc_med(lista,t_lista)    
