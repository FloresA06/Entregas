
def dict_traduccion():
    traducciones=dict()
    n=int(input("Ingrese el numero de palabras a agregar al diccionario: "))
    for i in range(n):
        palabra_og=str(input(f"Ingrese la #{i + 1} palabra en el idioma original: ")).strip().lower()
        palabra_trad=input(f"Ingrese su traducción: ").strip().lower()
        traducciones[palabra_og]=palabra_trad
    return traducciones

def buscar_trad(diccionario):
    pal=input("\nIngrese una palabra para traducir: ").strip().lower()
    if pal in diccionario:
        print(f"La traducción es: '{diccionario[pal]}'")
    else:
        print(f"No se encontró la traducción")

diccionario=dict_traduccion()
buscar_trad(diccionario)
