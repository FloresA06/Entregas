
def cap_conjunto(nombre):
    entrada=input(f"Ingrese los elementos del conjunto {nombre}, separados por comas: ")
    elementos=entrada.strip().split(',')
    conjunto=set([e.strip() for e in elementos])
    return conjunto

def inter_conj(c1, c2):
    return c1.intersection(c2) 

c1=cap_conjunto("A")
c2=cap_conjunto("B")
res=inter_conj(c1,c2)

print(f"El conjunto 'A': {c1}")
print(f"El conjunto 'B': {c2}")
print(f"Su unterseccion es: {res}")
