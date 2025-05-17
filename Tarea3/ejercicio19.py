
import random

def generar_numeros_aleatorios(n):
    lista = list()
    for i in range(n):
        lista.append(random.randint(1,100))
    return lista

resultado=generar_numeros_aleatorios(10)
print("Numeros aleatorios:", resultado)

'''''

- ¿Cuál es el propósito de la función 'generar_numeros_aleatorios(n)'? - C (crear una lista de numeros aleatorios de longitud n)
- ¿Cuál de las siguientes afirmaciones es verdadera sobre el uso de 'random.randint(1, 100)' dentro de la función? - A (es posible que genere numeros repetidos)
- ¿Qué tipo de dato retorna la función 'generar_numeros_aleatorios(n)'? - C (una lista con numeros enteros)
- Si se llama a 'generar_numeros_aleatorios(0)', ¿qué resultado se obtiene? - A (una lista vacia)
- ¿Qué se imprime en la consola si se ejecuta 'print('Números aleatorios:', resultado)' después de llamar a 'generar_numeros_aleatorios(10)? - C (numeros aleatorios entre 1 y 100)


'''''