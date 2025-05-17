
matriz=list()

fila1=list()
for x in range(3):
    num=int(input("Ingrese los elementos para la primera fila: "))
    fila1.append(num)
matriz.append(fila1)

fila2=list()
for x in range(3):
    num=int(input("Ingrese los elementos para la segunda fila: "))
    fila2.append(num)
matriz.append(fila2)

fila3=list()
for x in range(3):
    num=int(input("Ingrese los elementos para la tercera fila: "))
    fila3.append(num)
matriz.append(fila3)

print("Su matriz es:")
for fila in matriz:
    print(fila)

def det_matriz(matriz):
    det_pos=(fila1[0]*fila2[1]*fila3[2])+(fila2[0]*fila3[1]*fila1[2])+(fila3[0]*fila1[1]*fila2[2])
    det_neg=-(fila1[2]*fila2[1]*fila3[0])-(fila2[2]*fila3[1]*fila1[0])-(fila3[2]*fila1[1]*fila2[0])
    determinante=det_pos+det_neg
    print(f"La determinante de la matriz es: {determinante}")

det_matriz(matriz)    
