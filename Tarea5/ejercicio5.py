
def cons_cad(cadena):
    vocales={'a','e','i','o','u'}
    cad=cadena.lower()
    conj_cons=set()
    for caracter in cad:
        if caracter.isalpha() and caracter not in vocales:
            conj_cons.add(caracter)
    return conj_cons

cadena=str(input("Ingrese la cadena de texto: "))
conj=cons_cad(cadena)
print(f"Su conjunto sin vocales es: {conj}")
