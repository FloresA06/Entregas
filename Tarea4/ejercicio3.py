
def capturar_vector():
    entrada = input("Ingrese los elementos del vector separados por espacios: ")
    vector = [int(x) for x in entrada.strip().split()]
    return vector

def producto_escalar(v1,v2):
    if len(v1)!=len(v2):
        print("Los vectores deben tener la misma longitud.")
    else:
        return sum(a*b for a,b in zip(v1,v2))

vector1=capturar_vector()
vector2=capturar_vector()

res=producto_escalar(vector1, vector2)
print(f"El producto escalar de los vectores es: {res}")
