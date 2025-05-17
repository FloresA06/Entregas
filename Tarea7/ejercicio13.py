
def dividir_elementos(lista, divisor):
    try:
        resultados=[elemento/divisor for elemento in lista]
        return resultados
    except ZeroDivisionError:
            return "El divisor no puede ser cero"

print(dividir_elementos([2,3,12,56,5,1], 0))
print(dividir_elementos([1,2,3,4,5,6,7,8], 3))
