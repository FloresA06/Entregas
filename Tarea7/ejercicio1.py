
l_nombres=list()
n=int(input("Numero de nombres a ingresar: "))

for num in range(n): 
    nombre=input("Nombre: ").strip
    l_nombres.append(nombre)

with open("nombres.txt", "w") as file: 
    file.write("\n".join(l_nombres))
