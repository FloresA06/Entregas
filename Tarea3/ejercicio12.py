
t_lista=int(input("Indique el tamaño de la lista: "))
lista=list()

for x in range(t_lista):
    num=int(input("Ingrese un numero: "))
    lista.append(num)
print(f"Su lista es: {lista}")

def moda(lista):
    l1=list()
    x=0
    lista.sort()
    while x<len(lista):
        l1.append(lista.count(lista[x]))
        x+=1
    d1=dict(zip(lista, l1)) 
    d2={k for (k,v) in d1.items() if v==max(l1)} 
    print(F"La moda es: {str(d2)}")

moda(lista)