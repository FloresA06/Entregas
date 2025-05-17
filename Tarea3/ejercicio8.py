
cad=str(input("Ingrese una cadena de texto: "))

def det_pal(cad):
    n_cad=cad.replace(" ","")
    cad_inv=n_cad[::-1]
    if cad_inv==n_cad:
        print("La cadena de texto es un palindromo")
    else:
        print("La cadena de texto no es un palindromo")

det_pal(cad)
