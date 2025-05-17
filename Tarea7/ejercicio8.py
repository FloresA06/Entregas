
def convertir_a_entero(cadena):
    try:
        numero=int(cadena)
        return numero
    except ValueError:
        if "." in cadena:
            return "La cadena no puede llevar punto decimal"
        else:
            return "La cadena no puede contener caracteres que no sean dígitos"

print(convertir_a_entero("perro"))
print(convertir_a_entero("376"))
print(convertir_a_entero("3.1416"))
print(convertir_a_entero("5"))
