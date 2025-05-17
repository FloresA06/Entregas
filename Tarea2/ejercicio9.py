
cad=str(input("Ingrese la cadena de texto: "))
palabras=cad.split()
contador=0

for p in palabras:
    contador+=1

print(f"Hay {contador} palabras en la cadena")
