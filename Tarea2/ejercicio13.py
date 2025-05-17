
cad=str(input("Ingrese una cadena de texto: "))
char=str(input("Indique el caracter a buscar: "))
cont=0

for l in cad:
    if l==char:
        cont+=1

print(f"El caracter {char} aparecio {cont} veces en la cadena")
