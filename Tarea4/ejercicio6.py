
def cap_matriz():
    matriz=list()
    for i in range(5):
        fila=list()
        for j in range(5):
            valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def sum_diag(matriz):
    sum_prin=0
    sum_sec=0
    for i in range(5):
        sum_prin+=matriz[i][i]
        sum_sec+=matriz[i][4-i]
    return sum_prin,sum_sec

matriz=cap_matriz()
suma_p,suma_s=sum_diag(matriz)

print("Su matriz es:")
for fila in matriz:
    print(fila)

print(f"La suma de la diagonal principal es: {suma_p}")
print(f"La suma de la diagonal secundaria es: {suma_s}")
