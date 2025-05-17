
suma=0
import random
lista_r=list()

for n in range(0,10):
    lista_r.append(random.randint(0,10))

with open("num_enteros.txt","w") as archivo:
    for item in lista_r:
        archivo.write(f"{item}\n")

with open("num_enteros.txt", "r") as archivo:
    lista_ent=[int(linea) for linea in archivo]

for num in lista_ent: 
    suma += num

print(f"Los elementos de la lista son: {lista_ent}")
print(f"La suma de sus elementos es: {suma}")
