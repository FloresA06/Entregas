
def generar_fibonacci(n):
    fibonacci=[0,1]
    while len(fibonacci)<n:
        fibonacci.append(fibonacci[-1]+fibonacci[-2])
    return fibonacci

resultado=generar_fibonacci(10)
print("Serie de Fibonacci:",resultado)
