
def dic_sinonimos():
    sinonimos=dict()
    n=int(input("Numero de sinonimos a registrar: "))
    for i in range(n):
        palabra=input(f"Ingrese la palabra #{i+1}: ").lower()
        l_sinonimos=input(f"Ingrese sinónimos de '{palabra}' separados por comas: ").lower()
        sinonimos[palabra]=[s.strip() for s in l_sinonimos.split(",")]
    return sinonimos

def buscar_sin(diccionario):
    palabra=input("\nIngrese una palabra para buscar sus sinónimos: ").lower()
    if palabra in diccionario:
        print(f"Sinónimos de '{palabra}':{', '.join(diccionario[palabra])}")
    else:
        print(f"No se encontraron sinónimos para la palabra '{palabra}'")

def mostrar_pal(diccionario):
    print("\nPalabras registradas en el diccionario: ")
    for palabra in diccionario.keys():
        print(palabra)

diccionario_sinonimos=dic_sinonimos()
buscar_sin(diccionario_sinonimos)
mostrar_pal(diccionario_sinonimos)
