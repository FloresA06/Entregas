
def obtener_elemento(lista, indice):
    try:
        elemento = lista[indice]
        return elemento
    except IndexError:
        return "El elemento con ese index no existe en la lista"

print(obtener_elemento(["azul", "rojo", "verde", "morado", "gris"], 7))
print(obtener_elemento([2, 7, 43, 8, 132], 3))
print(obtener_elemento(["azul", 6, "gris", 90, "&", "magenta"], 0))
