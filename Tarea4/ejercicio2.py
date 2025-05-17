
def matriz():
    matriz=list()
    for x in range(3):
        fila=list()
        for y in range(3):
            valor=int(input(f"Ingrese los valores: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

print("Primera matriz")
matriz1=matriz()
print("Segunda matriz")
matriz2=matriz()

def suma_matrices(matriz1, matriz2):
    m_suma=list()
    for i in range(3):
        sum_filas=list()
        for j in range(3):
            suma=matriz1[i][j]+matriz2[i][j]
            sum_filas.append(suma)
        m_suma.append(sum_filas)
    return m_suma

m_s=suma_matrices(matriz1,matriz2)
for fila in m_s:
    print(fila)
