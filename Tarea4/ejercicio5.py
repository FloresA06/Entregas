
n=int(input("Ingrese el numero de filas de la matriz: "))
m=int(input("Ingrese el numero de columnas de la matriz: "))
elemento=int(input("Ingrese el elemento a buscar: "))
matriz=list()

for x in range(n):
    filas=list()
    for y in range(m):
        val=int(input("Ingrese un valor para la matriz"))
        filas.append(val)
    matriz.append(filas)

def m_elem(matriz,elemento):
    for i in range(len(matriz)):            
        for j in range(len(matriz[i])):     
            if matriz[i][j]==elemento:
                return (i, j)  
    return None

resultado=m_elem(matriz,elemento)
if resultado:
    print(f"Elemento encontrado en la posición: fila {resultado[0]}, columna {resultado[1]}")
else:
    print("Elemento no encontrado en la matriz.")
