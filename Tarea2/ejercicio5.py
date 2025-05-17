
cad=str(input("Ingrese una cadena de texto: "))
voc=0

for l in cad:
    if l=="a" or l=="e" or l=="i" or l=="o" or l=="u" or l=="A" or l=="E" or l=="I" or l=="O" or l=="U":
        voc+=1

print(f"Hay {voc} vocales en el texto")
