
def cap_puntos():
    puntos=list()
    n=int(input("Numeros de puntos a ingresar: "))
    for i in range(n):
        x=float(input(f"Ingrese la coordenada x del {i + 1} punto: "))
        y=float(input(f"Ingrese la coordenada y del {i + 1} punto: "))
        puntos.append((x, y))
    return puntos

def puntos_distancia(puntos):
    return sorted(puntos, key=lambda punto: punto[0]**2 + punto[1]**2)

def mostrar_puntos(puntos):
    print("Los puntos ordenados por distancia al origen son:")
    for punto in puntos:
        print(punto)

p_usuario=cap_puntos()
puntos_ordenados=puntos_distancia(p_usuario)
mostrar_puntos(puntos_ordenados)
