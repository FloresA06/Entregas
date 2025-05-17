
def obtener_valor(diccionario, clave):
    try:
        valor = diccionario[clave]
        return valor
    except KeyError:
        return "La clave no se encuentra en el diccionario"

print(obtener_valor({"rogelio":46, "Ernesto":29, "Laura":32},"Jose"))
print(obtener_valor({"platano":"fruta", "zanahoria":"vegetal", "tomate":"???"},"platano"))
