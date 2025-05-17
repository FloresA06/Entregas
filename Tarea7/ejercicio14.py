
def escribir_archivo(nombre_archivo, contenido):
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(contenido)
    except IOError:
        return "El archivo no es accesible"

escribir_archivo("puntos.txt", ".........")
escribir_archivo("comas.txt", ",,,,,,")
escribir_archivo("guiones.txt", "-------")
