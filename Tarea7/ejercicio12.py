
import math
def raiz_cuadrada(numero):
    try:
        resultado=math.sqrt(numero)
        return resultado
    except ValueError:
        if numero<0:
            return "No es posible obtener la raiz cuadrada de un numero negativo"

print(raiz_cuadrada(3))
print(raiz_cuadrada(-1))
print(raiz_cuadrada(54.1))
print(raiz_cuadrada(49))
