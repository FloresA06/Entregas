
n=int(input("Ingrese el numero de filas de la matriz: "))
m=int(input("Ingrese el numero de columnas de la matriz: "))
matriz=list()

for x in range(n):
    filas=list()
    for y in range(m):
        val=(x+y)%2
        filas.append(val)
    matriz.append(filas)

print("Matriz alternada:")
for fila in matriz:
    print(fila)
