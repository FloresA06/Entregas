
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
       	return "El archivo no existe"

print(leer_archivo("cal_pracial2.txt"))
print(leer_archivo("num_enteros.txt"))