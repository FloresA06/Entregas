
def cap_conjunto(nombre):
    entrada=input(f"Ingrese los elementos del conjunto {nombre}, separados por comas: ")
    elementos=entrada.strip().split(',')
    conjunto=set([e.strip() for e in elementos])
    return conjunto

def union_conjuntos(c1, c2):
    return c1.union(c2)  

conj1=cap_conjunto("A")
conj2=cap_conjunto("B")
res_union=union_conjuntos(conj1,conj2)

print(f"nConjunto A: {conj1}")
print(f"Conjunto B: {conj2}")
print(f"Unión de A y B: {res_union}")
