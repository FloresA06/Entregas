
import random

n=int(input("Indique el numero de numeros a generar: "))
lista=list()

for num in range(n):
    lista.append(random.randint(1,100))

print(f"La lista es: {lista}")
