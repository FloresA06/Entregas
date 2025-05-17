
def matriz_t(matriz):
    transpuesta=list()
    for i in range(3):
        fila=list()
        for j in range(3):
            fila.append(matriz[j][i])
        transpuesta.append(fila)
    return transpuesta

def matriz():
    matriz=list()
    for x in range(3):
        fila=list()
        for y in range(3):
            valor=int(input(f"Ingrese los valores: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

matriz1=matriz()
matriz1_t=matriz_t(matriz1)

for fila in matriz1_t:
    print(fila)
