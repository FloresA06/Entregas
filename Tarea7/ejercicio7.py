
def dividir(a,b):
    try:
        resultado=a/b
        return resultado
    except ZeroDivisionError:
        print("\nNo es posible dividir entre cero")
        return None

print(dividir(5,0))
print(dividir(2,4))
print(dividir(8,8))
