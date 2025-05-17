
def cont_pal(texto):
    for caracter in ",.;:!?¿¡()[]\"'":
        texto=texto.replace(caracter,"")
    texto=texto.lower()
    palabras=texto.split()
    frecuencias={}
    for pal in palabras:
        if pal in frecuencias:
            frecuencias[pal]+=1
        else:
            frecuencias[pal]=1
    return frecuencias

parrafo=input("Ingrese un párrafo o texto largo:\n")
frecuencias=cont_pal(parrafo)

print("\nFrecuencia de palabras: ")
for palabra,cantidad in frecuencias.items():
    print(f"{palabra}:{cantidad}")
