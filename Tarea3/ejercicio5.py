
lista_cals=list()
n_cal=int(input("Indique el numero de calificaciones a ingresar: "))

for x in range(n_cal):
    cal=float(input("Ingrese la calificacion: "))
    lista_cals.append(cal)

def prom(lista_cals):
    suma=0
    for cal in lista_cals:
        suma+=cal
    prom=suma/n_cal
    r_prom=round(prom,2)
    print(f"Su promedio es: {r_prom}")

prom(lista_cals)
