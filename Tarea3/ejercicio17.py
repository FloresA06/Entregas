
def es_palindromo(cadena):
    cadena=cadena.replace(" ","")
    cadena=cadena.lower()
    cadena2=""
    n=len(cadena)

    for i in range(n-1,-1,-1):
        cadena2+=cadena[i]
    return cadena==cadena2

resultado=es_palindromo("Dabale arroz a la zorra el abad")
print("Es palindromo?", resultado)
